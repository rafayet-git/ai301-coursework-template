# Contribution: Rule request: Docker-launched MCP server given host access (--privileged, docker.sock, host namespaces)

Path: `beat-2-contribution/contribution-story.md`

This file is Assignment 5, and it is graded at the path above; a copy kept anywhere else in
the repository is not read. **Keep every section header below under its exact name** — the
format criteria grade exactly that. Your course repo link is the whole submission: no tool
files and no evidence uploads are part of Assignment 5.

**Contribution Number:** 1
**Student:** Rafayet Hossain
**GitHub Username:** rafayet-git
**Issue:** https://github.com/adudley78/mcp-audit/issues/251
**Pull Request:** [GitHub PR link, once opened]

One repository, built across units 5 to 8, telling the whole story of your real
contribution. Fill it as you work, not at the end — the sections below ask for evidence that
is far easier to write down as it happens than to reconstruct in the last weekend.

Contribution Number stays `[1]` unless you make more than one contribution this term; it
just numbers them.

---

## Toolkit

Every story section below, from Why I Chose This Issue through Pull
Request, ends with a Toolkit block: which tool did that phase's work
and how you used it, what it produced, what difficulties or
shortcomings it presented, and what you changed or would change
because of them. Together the blocks are the thread the rubric's
Toolkit points read, and they are the raw material for your unit-9
portfolio, so keep them current as you work rather than
reconstructing them later.

A Toolkit block looks like this (copy it into each story section and
fill it there):

```text
**Toolkit**

- Tool: [which tool did this phase's work, and how you used it]
- What it produced: [described in a sentence or a short excerpt]
- Difficulties: [what fought you or fell short, or "none met"]
- What changed: [the patch, revision, or workaround, what you would
  update, or "nothing"]
```

This section also keeps one short dated entry per week of tool work,
starting below: what you built or changed that week, what broke, and
what you changed because of it. The blocks tell the story where it
happened; these entries are the toolkit's own timeline.

All four entries are graded. Keep every heading below, and fill each
one in the week it belongs to.

**Unit 5: Built a three-query issue-scout and patched it after it accepted five weak issues**

I wrote a search strategy of three `gh search issues` queries (Docker/Python, Docker/Go, self-hosted/TypeScript, each traced to my fit profile) and ran the scout on it. The first scan accepted all five graded issues even though two of the repos had never merged a PR from an outside contributor, one issue depended on an unfinished issue, one needed NAS hardware I don't have, and one was opened by a bot. I added a required "Outside contributions get merged" check, made the scope check fail on open dependencies and hardware needs, and filtered bot-authored issues in the strategy; the re-run then accepted 3 and rejected 2. The rubric still missed that devtrack#158 was already fixed on main, which I only caught by reading the code, so a "problem still exists" check is the next patch.

**Unit 6: Installed the voice guard and wrote a repo-memory file for mcp-audit**

I merged my three voice-guide copies into one guide, added an Upstream section with rules for claims, questions and pings, and installed the guard as a hook; its wiring test blocked `gh issue comment --help` on the first try, which is how I know the hook fires. When I first went to post my claim the guard was not installed yet (no `~/.claude/voice-guard/` folder), so I ran the checker by hand on my draft and it passed before I posted. For the repo-memory file I read CONTRIBUTING.md and the rule guide, oriented only on the community-rules code, and kept `CLAUDE.local.md` to 33 lines because the repo already ships a 989-line `CLAUDE.md`; it stays out of git through `.git/info/exclude`. What fell short: `uv` was not installed when I wrote the memory file, so its commands started out unverified; once I installed it I ran them, which showed the full suite has 7 failures on my machine that come from my own Claude Code config (not from the repo), and I recorded that baseline and the workaround in the file.

**Unit 7: [one line on the tool work]**

[2-4 sentences: the ship-gate and your gate manifest. What it produced
on your real branch, what fought you, what changed because of it.]

**Unit 8: [one line on the tool work]**

[2-4 sentences: the PR-monitor and your playbook. What it read, what it
drafted, what you did with the draft.]

---

## Why I Chose This Issue

I searched all of GitHub with three `gh search issues` queries taken from my fit profile: Docker with Python, Docker with Go, and self-hosted with TypeScript, each limited to open "good first issue" issues with no assignee that were updated in the last 60 days. My scout ranked 248 results and graded the top five. It accepted `adudley78/mcp-audit#251`, a request to add a rule that flags MCP servers launched with `docker run` and host-level access (`--privileged`, the Docker socket mounted, or the host PID or network namespace). It passed every required check: the owner opened it as "Rule idea for a first contribution" with the steps spelled out, nobody is assigned, no pull request is open, the repo pushed and released within the last two days, and the owner merged an outside contributor's PR (#254) on 2026-11-01. After I patched the scout, the re-run still accepted it. I also graded two issues from the course site: at first the scout rejected `badges/shields#4656` on scope, then accepted it as ambitious once I replaced my scope check with a looser one, and it accepted `Priyanshu-byte-coder/devtrack#158`. I did not pick the devtrack issue because its fix was already on main and six people had asked to work on it, and I did not pick the shields issue because its open question (which AUR badges the maintainers want) has been unanswered since 2020. The difficulty note on the issue I chose is moderate, because the rule touches a YAML file and several docs files. This issue fits my profile through Python and Docker and the backend and security side of self-hosting, and I hope to learn how a real project reviews a contribution, how to write and test a detection rule against example configs, and how to work from a maintainer's contributing guide.

Claim comment: https://github.com/adudley78/mcp-audit/issues/251#issuecomment-6566553997. I posted a one-line claim earlier and deleted it, then posted this one, which names my first step and when I will report back. The voice guard passed it before it went up.

On the tool itself: the first scan was too generous. It accepted all five issues, including ones in repos that had never merged an outsider's PR, one that depended on an unfinished issue, one that needed NAS hardware, and one opened by a bot. I added the merged-PR check and a bot filter, plus a stricter scope check that I later replaced with the course's looser scope-feasible check and a difficulty note, and the re-run rejected the weaker ones. It still has a gap: it accepted `devtrack#158` even though the work was already done, so I would add a check that the problem still exists on the default branch.

**Toolkit**

- Tool: issue-scout, with my three-query search strategy and my seven-check rubric (six required, one preferred). I ran a scan, patched it, re-ran it, then graded two course-site issues directly.
- What it produced: the scan ranked 248 results and graded the top five; it accepted mcp-audit#251 with every required check passing (owner-written first-contribution issue, no assignee, no open PR, outside PR #254 merged 2026-11-01). The re-run, after my patches, still accepted it.
- Difficulties: the first scan accepted all five issues, including ones that were blocked, needed hardware, were bot-written, or were in repos that never merged outside PRs. It also accepted devtrack#158 although the fix was already on main.
- What changed: I added the merged-PR check and a bot-author filter, then replaced my scope check with the scope-feasible row and a difficulty note, which dropped my open-dependency and hardware conditions and flipped the shields verdict from reject to accept. I still need a "problem still exists on the default branch" check.

---

## Understanding the Issue

**Problem Description**

mcp-audit does not flag an MCP server that is launched with `docker run` (or `podman run`) and given control of the host: `--privileged`, a mounted Docker socket (`-v /var/run/docker.sock:...`), or the host's process or network namespace (`--pid=host`, `--network=host` / `--net=host`). These flags undo the isolation that is the reason to run an MCP server in a container, and no existing check reads a server's `docker` arguments.

**Expected Behavior**

Scanning a config with `--privileged`, a Docker socket mount or `--pid=host` returns a HIGH finding from a new rule, `COMM-036`. Scanning one with `--network=host` or `--net=host` returns a MEDIUM finding from a second rule, `COMM-037`; the maintainer asked for that split in the issue thread because host networking shares the host's network but does not hand over the host itself. The issue's "should not fire" config, and `--network=none` or `--network bridge`, stay quiet for both rules.

**Current Behavior**

No finding mentions any of those flags. I scanned four configs on `main` at `ee557b8` and the Docker socket, `--privileged` and `--pid=host` configs returned the same finding IDs as the clean control (`CFHYG-001`, `CFHYG-002`, `RUGPULL-000`, `COMM-004`), none of them about the Docker arguments.

**Affected Components**

The fix is mostly data, not engine code: two new rule files in `rules/community/`, plus the files a new rule ID has to appear in (`PROVENANCE.md`, `docs/owasp-mapping.json`, `docs/manual-test-matrix.md`, and the community-rule counts in `README.md` and `CLAUDE.md`) and new tests in `tests/test_rules.py`. The rule engine in `src/mcp_audit/rules/engine.py` runs the rules but I do not change it.

**Toolkit**

- Tool: Claude Code, which I used to read the issue thread and trace how the rule engine, the community rules and the last accepted rule PR (`COMM-035`) fit together.
- What it produced: a map of the match fields and the list of files the previous rule PR touched, which is where my file list comes from.
- Difficulties: my first reading of the issue was one compound rule; the maintainer's reply changed it to two rules at two severities, so I rewrote this section after his answer.
- What changed: nothing in the tool; I re-read the issue thread before writing, instead of relying on my first draft of the plan.

---

## Reproduction Process

**Environment Setup**

Linux 7.3.0 (Arch-based), x86_64. I used mcp-audit from my fork's `main` at commit `ee557b8` (2026-11-01), version 0.26.0 in `pyproject.toml`, with `uv 0.13.6`; `uv run` picked Python 3.12.16 even though my system Python is 3.14.8. I set it up with `uv sync --extra dev` from the clone root, as CONTRIBUTING.md says (a bare `uv sync` would break the async tests). Docker is not needed, because mcp-audit only reads config files. One challenge: `uv` was not installed on my machine at first, so I installed it before anything would run.

**Steps to Reproduce**

1. From the clone root, write four small MCP config files in a scratch directory: the issue's "should fire" example (Docker socket mounted), one with `--privileged`, one with `--pid=host`, and the issue's "should not fire" example as a control. Each is a single `docker run` server named `github` in the issue's JSON shape: the first and last are copied from the issue, and the other two keep the issue's `["run", "-i", "--rm", ...]` arguments and the image `ghcr.io/example/mcp-server`, replacing the socket mount with `--privileged` or `--pid=host`.
2. Scan each one: `uv run mcp-audit scan --path <file> --format json`, and print the finding IDs.
3. Observed result: all four files return the same finding IDs (`CFHYG-001`, `CFHYG-002`, `RUGPULL-000`, `COMM-004`), so nothing distinguishes the dangerous configs from the control. Reading the findings shows none is about the Docker arguments: `CFHYG-001/002` are about my config file living in world-readable `/tmp`, and `COMM-004` is "Unrecognized stdio server binary".

**Reproduction Evidence**

- **Commit showing reproduction:** none. I did not commit the scratch configs to my fork.
- **Screenshots/logs:**

  ```
  == sock        ['CFHYG-001', 'CFHYG-002', 'RUGPULL-000', 'COMM-004']
  == privileged  ['CFHYG-001', 'CFHYG-002', 'RUGPULL-000', 'COMM-004']
  == pidonly     ['CFHYG-001', 'CFHYG-002', 'RUGPULL-000', 'COMM-004']
  == clean       ['CFHYG-001', 'CFHYG-002', 'RUGPULL-000', 'COMM-004']
  ```

- **My findings:** Reproduced, as a missing detection: on `ee557b8` no finding is about `--privileged`, the Docker socket mount, `--pid=host` or `--network=host`. `mcp-audit rule list` has no Docker-flag rule (its one match for "privileg" is COMM-034, about credential scope), and the only source file that mentions `docker.sock` is `src/mcp_audit/analyzers/sandbox.py`, which is about Claude Code's own sandbox settings. One odd result: `--network=host` on its own adds a `TOXIC-007` finding ("Git access + network exfiltration path") that mentions neither Docker nor host networking. The maintainer later confirmed it is the capability matcher reading "network" in any `--network=...` flag as outbound access (it also fires for `--network=none` and `--network=bridge`), and said he is tracking that fix separately, so it is not part of my change. I have not tested `podman`, `--net=host`, the `--network=none` and bridge cases the issue names, or macOS and Windows.

**Toolkit**

- Tool: repro-check, with my six-check rubric (environment, rerunnable steps, evidence matches the issue, honest outcome, repo communication rules, AI disclosure) and my voice guide. I graded my claim comment and my repro report together against issue #251.
- What it produced: an accept with all six checks passing and no voice-guide rule broken.
- Difficulties: the tool reads my drafts and the issue; it does not re-run my commands. I found a miscount of my own before grading it by re-running the report's step 3 commands (I had written that a `rule list` search returned 3 lines, but the command in the report returns 1), so the check I would have trusted could not have caught that.
- What changed: I corrected the report before grading. I did not change the rubric. A possible addition is a check that the report's quoted counts and outputs match its own commands.

---

## Solution Approach

**Analysis**

The gap is a missing detection, not a bug in existing code. `RuleEngine.match_server` in `src/mcp_audit/rules/engine.py` already evaluates every rule in `rules/community/` against each server. For a `command` condition `_extract_field` returns the raw command string, and for `args` it returns all arguments joined by one space, so a regex over `args` can see `--privileged`, `--pid=host` or a `-v /var/run/docker.sock:...` mount. `_evaluate_rule_match` already supports an `operator: and` compound match, which is how a rule can require `command` to be `docker` or `podman` and `args` to contain a dangerous flag. `rules/community/` has no rule that does either, and the only source file that mentions `docker.sock`, `src/mcp_audit/analyzers/sandbox.py`, is about Claude Code's own sandbox settings. So the fix is new rule files, plus the documentation and counts a new rule ID has to appear in.

**Proposed Solution**

Add two community rules, as the maintainer decided in the issue thread. `COMM-036` (HIGH) fires when `command` is `docker` or `podman` and `args` contain `--privileged`, a mount of `docker.sock` or `podman.sock`, or `--pid=host`. `COMM-037` (MEDIUM) fires when `command` is `docker` or `podman` and `args` contain `--network=host` or `--net=host`. Both rules should stay quiet on the issue's "should not fire" config and on `--network=none` and `--network bridge`, and an explicit `--privileged=false` should not fire. I will propose OWASP MCP05 ("privileged launchers" in the guide's table) and the category `hygiene`, and let the maintainer confirm, since the issue says he will.

What I am deliberately not changing: the rule engine; the `TOXIC-007` false positive on `--network=...` flags, which the maintainer is fixing separately; and other container flags the issue does not name (`--cap-add`, `--ipc=host`, bind-mounting `/`). I will mention them in the PR as possible follow-ups, not add them.

**Implementation Plan**

1. Create a branch in my fork, `feat/comm-036-comm-037-docker-host-access`, from `main` after checking that upstream `main` has not moved and that `COMM-036` and `COMM-037` are still free.
2. Copy `rules/community/TEMPLATE.yml` to `rules/community/COMM-036.yml` and `COMM-037.yml` and fill them in as compound `and` rules (`command` regex plus `args` regex), with messages, severities, tags and `owasp_mcp_top_10`.
3. Run `uv run mcp-audit rule validate` on both files, then `rule test` against the issue's two examples and variants: `--privileged`, the socket mount, `--pid=host`, `--network=host`, `--net=host`, `--network=none`, `--network bridge`, `--privileged=false`, and `podman`.
4. Add tests to `tests/test_rules.py` in the style of `TestComm034GodKey`: one class per rule that asserts `COMM-036` or `COMM-037` fires or does not fire, never asserting on the full finding list because `TOXIC-007` keeps appearing in those fixtures.
5. Add a `PROVENANCE.md` entry for each rule citing the Docker docs the issue links, and an entry for each in `docs/owasp-mapping.json`.
6. Update `docs/manual-test-matrix.md` Section 15 (rule count and the `COMM-001`–`COMM-NNN` range), then run `uv run python scripts/update_test_count.py` and commit only the community-rule lines it changes in `README.md` and `CLAUDE.md`, leaving its test-count changes out.
7. Run every check in `ship-manifest.md`, then open the PR titled `feat(rules): add COMM-036 and COMM-037 — Docker host-access flags` with the repo's rule-submission checklist, the config I tested against, the `rule validate` output and the full test result.

Deviations: none yet.

**Toolkit**

- Tool: plan-check, with my six-check rubric and my written procedure, graded `plan.md` and my draft plan comment (`plan-comment.md`) against issue #251, using my posted update comment as the repro evidence. I also ran the draft comment through my voice guard, which passed it. Claude Code drafted both files from the code I had traced.
- What it produced: an accept on the first run with all six checks passing and no voice-guide rule broken.
- Difficulties: my procedure does not say what counts as the repro evidence in live mode when I posted one combined update instead of a separate repro comment, so the grader had to choose; and two weak spots passed that I would tighten anyway: step 4 of my plan does not list the test fixtures one by one, and the plan does not say how `command` paths like `/usr/bin/docker` or `docker.exe` are handled.
- What changed: I made no plan edits for the run. I will add the procedure line about live-mode repro evidence to `procedure.md`, and I will name the fixtures and the `command` forms in the plan when I build, recording them as deviations if they change anything.

---

## Testing Strategy

[What observable checks prove the fix: your reproduction steps re-run
against the built change (before and after), and the repo's own test
suite or checks with the outcome shown. "Tests pass" with nothing
observable named is not a strategy.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Implementation Notes

[A running log, added to as you work. Date each entry. What you
built, decisions you made when you made them, wrong turns included.]

**[Date]**

[Entry]

**[Date]**

[Entry]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Pull Request

**PR Link:** [GitHub PR URL when opened]

**PR Description:** [what the PR says; much of the content above
adapts into it]

**Maintainer Feedback:**

- [Date]: [feedback received, or "none yet"; silence is a normal
  state and costs you nothing]
- [Date]: [how you addressed it]

**Status:** [Awaiting review / Iterating / Merged / Closed. The
status is a fact you record, never a grade: the PR is graded as
opened.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Learnings and Reflections

**Technical Skills Gained**

[What you learned technically, named concretely.]

**Challenges Overcome**

[What was hard and how you solved it; point at the real events, the
Toolkit blocks above are full of them.]

**What I'd Do Differently Next Time**

[Reflection on your process.]

---

## Resources Used

[What actually helped, not a reading list. List things this story
already shows you using: the doc you followed to set the environment
up, the thread that explained the bug, the person who answered you.
One real entry beats ten plausible ones.]

- [Link to documentation that helped]
- [Discussion, issue, or post that helped]
