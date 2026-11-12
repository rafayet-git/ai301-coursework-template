# Two rules that flag containers handed the host: my first open source contribution to mcp-audit

## Overview

mcp-audit is an open source scanner that reads the settings AI assistants use to launch MCP servers and warns about risky ones. Many MCP servers run in containers, and a few Docker flags give the container control of the host, which defeats the reason to use a container. mcp-audit had no check for them, so a dangerous config scanned exactly like a safe one. I wrote two detection rules, `COMM-036` (HIGH) and `COMM-037` (MEDIUM), and the maintainer merged them in [PR #259](https://github.com/adudley78/mcp-audit/pull/259), about 26 hours after I opened it. The tool in the story is a pre-submission checker I built in this course, which I call a ship-gate. I wrote its manifest, the list of four checks it runs, from the repo's own contributing guide and CI config, and it stopped my PR description once before I opened the PR.

## What happened

**Reproducing the gap.** The issue ([#251](https://github.com/adudley78/mcp-audit/issues/251)) asked for a rule on `docker run` host access. Before writing anything, I scanned four configs on `main`: one with the Docker socket mounted, one with `--privileged`, one with `--pid=host`, and the issue's "should not fire" control. All four returned the same findings:

```
== sock        ['CFHYG-001', 'CFHYG-002', 'RUGPULL-000', 'COMM-004']
== privileged  ['CFHYG-001', 'CFHYG-002', 'RUGPULL-000', 'COMM-004']
== pidonly     ['CFHYG-001', 'CFHYG-002', 'RUGPULL-000', 'COMM-004']
== clean       ['CFHYG-001', 'CFHYG-002', 'RUGPULL-000', 'COMM-004']
```

None of those findings is about the Docker arguments, so nothing separated the dangerous configs from the control.

**Splitting one rule into two.** My plan was a single rule for every flag. I asked in the issue whether `--network=host` belonged at the same severity, because it looked less severe. The maintainer answered:

> `--privileged`, a mounted Docker socket and `--pid=host` each hand the server the host itself, so those stay HIGH in `COMM-036`. ... Make that `COMM-037` at MEDIUM. Both rules in one PR is fine.

That was my second version of the plan. Host networking lets a server reach anything on the host's localhost but does not give it the host, and one severity for both would have either over-warned on networking or under-warned on the socket. I rewrote the plan, the rule files and the tests around two rules.

**How the rules work.** Each is a compound rule: `command` must be `docker` or `podman`, and `args` must match a flag pattern. This is the `COMM-036` match from the merged file:

```yaml
match:
  operator: and
  conditions:
    - field: command
      pattern: '(?:^|(?<=/))(?:docker|podman)(?:\.exe)?$'
      type: regex
    - field: args
      pattern: '(?<!\S)--privileged(?:=true)?(?!\S)|\b(?:docker|podman)\.sock\b|(?<!\S)--pid[= ]host(?!\S)'
      type: regex
```

The lookarounds are deliberate: `--privileged=false` does not fire, and a path like `docker.socket` is not mistaken for `docker.sock`. I wrote 26 tests, such as this parametrized one, and they all fail with the two rule files removed and pass with them back:

```python
def test_fires_on_each_host_takeover_flag(self, community_rules_dir, args) -> None:
    assert _ids("COMM-036", community_rules_dir, command="docker", args=args) == ["COMM-036"]
```

Scanning the same configs on my branch gave `COMM-036` on the socket, `--privileged` and `--pid=host` configs, `COMM-037` on a `--network=host` config, and neither on the controls.

**The ship-gate stopping me.** Before opening the PR, I ran the gate. My four manifest checks passed, but my own PR-description check rejected it:

```
Description claims match the diff and plan [unclear]: The description claims `rule validate` printed '✓ Valid', `rule test` was run, and `scan demo/configs/` shows no COMM-036/037 findings; test_evidence.md contains none of that output.
```

I had run all three commands but never saved their output. I added the output to my evidence file, corrected one phrase in the description (it said `rule test` gave "nothing" for the controls, when it prints "no"), and the next run passed.

**Review.** The maintainer's review found one failing CI check I had not caught:

> The 26 new tests changed the total to 8,441, and four docs still quote the old number ... Running `python scripts/update_test_count.py` (no flags) rewrites them. Push that and I'll merge once CI is green.

The repo's rule guide says to leave those test-count lines out, so I had. I ran the script with the same optional extras CI installs, got 8,441, committed the lines, and commented on the PR. The PR merged.

**What landed.** The maintainer merged both rules and said they ship in the next release. The `--network=host` fixture also showed a false alarm, `TOXIC-007`, which the maintainer said was not my bug. He fixed it in [#261](https://github.com/adudley78/mcp-audit/pull/261) and wrote when he closed the issue: "the TOXIC-007 false positive you found along the way is fixed in #261 (#260). Thank you, @rafayet-git, for the rules and for catching our bug."

## Limitations and what's next

The rules read `args` with a regex, so a flag set another way, such as inside a wrapper script, is not seen. I tested on Linux only, and `podman` only through a socket-path test. Other container flags, such as `--cap-add`, `--ipc=host` and bind-mounting `/`, are not covered, and they could be follow-up rules. My ship-gate also did not catch the failing test-count check, because my manifest followed the rule guide and excluded it. The next change I would make is to run `update_test_count.py --check` with CI's extras installed in the manifest, so the gate checks what CI checks.
