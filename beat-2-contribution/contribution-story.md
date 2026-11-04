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
**Pull Request:** https://github.com/adudley78/mcp-audit/pull/259

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

**Unit 7: Wrote a ship manifest for mcp-audit and ran the ship-gate on my branch before opening the PR**

My manifest lists four checks from the repo's own CONTRIBUTING.md and CI config (pytest, ruff check, ruff format --check, the OWASP mapping validator) and excludes two with dated reasons: the 7 shadow tests that fail from my machine's own Claude Code config, and the test-count sync. The gate's first run on my branch stopped at my pr-precheck: my description said `rule validate` printed "✓ Valid", `rule test` was run and the demo scan was clean, but `test_evidence.md` held none of that output. I had run all three but never saved the output, so I added it to the evidence file and changed one phrase in the description that said `rule test` gave "nothing" for the controls, when it prints "no". The second run passed, and when the 30-minute pass expired the hook ran the gate again as I opened the PR, and it passed again. The gate also made me wait about two minutes each time for the full test run, which is why I opened the PR right after.

**Unit 8: Installed the PR-monitor, wrote my playbook, and ran it on a PR that had already merged**

The monitor's free state check found PR #259 on `adudley78/mcp-audit`, not on my fork, because I had run `gh repo set-default`, and it read MERGED with 29 checks passing and the maintainer's merge comment as the last activity. I wrote my playbook from my own rules (acknowledge the response and then state the result, a nudge about 2 days after the repo's 7-day review window, once, with something new and no @-mentions, and no closing a PR just because it is quiet), and the full run drafted a "merged follow-up" comment from the merged-PR form. The draft's paragraph saying #251 "should be closable now" was wrong, because the issue had closed by itself at the same second as the merge, which the monitor could not see; its thank-you opening repeated the thanks I had already posted, and its one new line offered `--cap-add` and `--ipc=host` as a follow-up. I have not posted the draft, and I would change the monitor to read the linked issue's state as well as the PR's.

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

Deviations (2026-11-02):

- Added `author: rafayet-git` to both rule files. The template lists it as optional, and it was not in the plan.
- Named the test fixtures and the `command` forms the plan left open: `command` matches `docker` or `podman` also by full path or `.exe`, a `docker.socket` lookalike path does not fire, and the podman socket is covered by a test.
- `update_test_count.py` changed the community-rule numbers but left "37 real" and "36 run by default" stale in two lines of `README.md` and `CLAUDE.md`, and it rewrote the test counts. I fixed the two stale numbers by hand and put the test-count lines back, as the rule guide asks.
- Two commits, not one: the rules with everything a new rule ID must appear in, then the tests.

**Toolkit**

- Tool: plan-check, with my six-check rubric and my written procedure, graded `plan.md` and my draft plan comment (`plan-comment.md`) against issue #251, using my posted update comment as the repro evidence. I also ran the draft comment through my voice guard, which passed it. Claude Code drafted both files from the code I had traced.
- What it produced: an accept on the first run with all six checks passing and no voice-guide rule broken.
- Difficulties: my procedure does not say what counts as the repro evidence in live mode when I posted one combined update instead of a separate repro comment, so the grader had to choose; and two weak spots passed that I would tighten anyway: step 4 of my plan does not list the test fixtures one by one, and the plan does not say how `command` paths like `/usr/bin/docker` or `docker.exe` are handled.
- What changed: I made no plan edits for the run. I will add the procedure line about live-mode repro evidence to `procedure.md`, and I will name the fixtures and the `command` forms in the plan when I build, recording them as deviations if they change anything.

---

## Testing Strategy

Four observable checks, all saved in `test_evidence.md`:

1. **My reproduction, before and after.** I scanned the same six configs with `uv run mcp-audit scan --path <file> --format json` on `main` at `ee557b8` and on my branch: the Docker socket, `--privileged` and `--pid=host` configs, a `--network=host` config, and two controls (`--network=none` and the issue's "should not fire" config). Before: no COMM-036 or COMM-037 exists, and the dangerous configs return the same finding IDs as the control. After: the socket, `--privileged` and `--pid=host` configs return `COMM-036` (HIGH), the `--network=host` config returns `COMM-037` (MEDIUM), and both controls return neither.
2. **New tests that fail without the fix.** `TestComm036HostTakeoverFlags` and `TestComm037HostNetwork` in `tests/test_rules.py` (26 tests) assert on each rule's own finding, not the full list, so the `TOXIC-007` false positive cannot make them flaky. With `COMM-036.yml` and `COMM-037.yml` moved away all 26 fail; with them back all 26 pass.
3. **The repo's own checks, from `ship-manifest.md`.** `uv run pytest -q --deselect tests/test_shadow.py::TestShadowCommandIntegration` gives 8314 passed, 82 skipped; `ruff check` passes; `ruff format --check` reports 358 files already formatted; `validate_owasp_mapping.py` reports all 201 finding IDs mapped. Each runs in a clean shell with no virtual environment and exits 0.
4. **The guide's own steps.** `mcp-audit rule validate` passes on both files, `rule test` shows a YES for the matching config and "no" for the control, `rule list` reports 40 bundled community rules (matching the manual test matrix), and `scan demo/configs/` produces no COMM-036 or COMM-037 findings.

What I did not test: macOS or Windows, `podman` end to end (only its socket path in a test), and other container flags such as `--cap-add`, which are outside this PR. The full suite still shows 7 failures in `tests/test_shadow.py::TestShadowCommandIntegration`; they fail the same way on unchanged `main` on my machine and are excluded in my manifest with that reason.

**Toolkit**

- Tool: Claude Code ran the reproduction on both branches, the manifest checks in a clean shell and the new tests, and assembled `test_evidence.md` from the saved outputs. The ship-gate ran later, when I prepared the PR (see Unit 7).
- What it produced: `test_evidence.md` with the before output, the after output, the fails-then-passes proof for the new tests, the four manifest checks and the two excluded ones.
- Difficulties: the full suite takes over two minutes and I ran it several times; my "after" scans lost the `RUGPULL-000` first-run note only because the "before" scan had already created its state file, which could be misread as a side effect of my change, so I wrote that into the evidence file; and 7 shadow tests still fail from my machine's own config.
- What changed: I deselect that one test class in the manifest and record it as excluded with a dated reason, and I note the `RUGPULL-000` difference next to the output instead of leaving it unexplained.

---

## Implementation Notes

[A running log, added to as you work. Date each entry. What you
built, decisions you made when you made them, wrong turns included.]

**2026-11-02**

Made the branch `feat/comm-036-comm-037-docker-host-access` (CONTRIBUTING.md names no branch convention) and wrote the two rules as compound `and` rules: `command` is docker or podman, and `args` matches the flags. I used lookarounds like `(?<!\S)--privileged(?:=true)?(?!\S)` instead of `( |$)` groups so the matched value in the finding is the bare flag, not the flag with spaces around it, and `\bdocker\.sock\b` so a `docker.socket` path does not fire. `rule validate` passed on both, and I scanned 17 variant configs (the issue's examples plus `--privileged=true`, `--pid host`, a podman socket, a `--mount` socket, a full path to docker, `--network=none`, bridge, `--privileged=false` and a non-docker command carrying the same flags): the eight "fire" configs hit COMM-036, the three host-network configs hit COMM-037, and the six quiet ones hit neither. `git fetch` from my fork failed because my SSH key is a hardware key and this session could not unlock it, so I checked through the GitHub API that upstream `main` is still `ee557b8`.

**2026-11-02 (tests, docs and counts)**

Added `TestComm036HostTakeoverFlags` and `TestComm037HostNetwork` to `tests/test_rules.py` (26 tests). I moved the two rule files away and re-ran them to check the step's "a test that fails without the fix": all 26 failed, then all 26 passed with the files back. Then the registrations: `PROVENANCE.md` (two table rows, the counts, and the next free ID, now `COMM-038`), `docs/owasp-mapping.json` (MCP05, proposed), `docs/manual-test-matrix.md`, and the counts in `README.md` and `CLAUDE.md`. Wrong turn: `update_test_count.py` rewrote the test counts and left two "real" and "run by default" numbers stale, so I put the test counts back and fixed those numbers by hand. Results: ruff check, ruff format --check and `validate_owasp_mapping.py` pass; the full suite is 7 failed, 8320 passed, 82 skipped, and the 7 failures are the same `test_shadow.py` ones that fail on unchanged main because of my own Claude Code config; `scan demo/configs/` produces no COMM-036 or COMM-037 findings. Committed locally in two commits; nothing is pushed.

**2026-11-02 (testing)**

Ran my reproduction again on `main` and on the branch and saved both outputs, along with the manifest checks, in `test_evidence.md`. To get the "before" I switched the clone to `main`, scanned, and switched back; the branch was clean, so nothing carried over. The fix does what the issue asked: COMM-036 fires on the three host-takeover flags, COMM-037 fires on host networking, and the issue's "should not fire" config and `--network=none` stay quiet for both rules. Nothing failed that was not already failing on `main`.

**Toolkit**

- Tool: Claude Code, which wrote the two rule files, the tests and the registrations from my plan, and ran the project's own checks from `ship-manifest.md` by hand and saved the output in `test_evidence.md`. The ship-gate ran later, when I prepared the PR (see Unit 7).
- What it produced: two rule files, 26 tests, the documentation and count edits in two commits with messages that say what each does, and the evidence file.
- Difficulties: `update_test_count.py` left stale numbers and changed test counts it should not; a fetch from my fork failed because my SSH key is a hardware key; the full suite shows 7 failures from my own machine's config.
- What changed: I fixed the stale numbers by hand and restored the test counts, recorded the plan deviations in `plan.md`, and will push from my own terminal with the key plugged in.

**2026-11-02 (opening the PR)**

Ran the ship-gate by hand (it stopped once, see Unit 7), pushed the branch from my own terminal, ran `gh repo set-default adudley78/mcp-audit` so the PR would go to the original repo and not my fork, and opened PR #259 through Claude Code with the same title and `pr_draft.md`.

**2026-11-03 (review)**

The maintainer's review found one failing CI check, `update_test_count.py --check`. I ran the script with the extras CI installs, committed the four test-count lines (`d4ccedd`), merged `main` into the branch and commented on the PR. The PR was merged at 02:49 UTC on 2026-11-04.
---

## Pull Request

**PR Link:** https://github.com/adudley78/mcp-audit/pull/259

**PR Description:** Title: `feat(rules): add COMM-036 and COMM-037 for containers launched with host access`. It begins `Fixes #251` and adds two community rules, split as the maintainer asked in the issue thread: COMM-036 (HIGH) for `--privileged`, a mounted `docker.sock` or `podman.sock`, and `--pid=host`; COMM-037 (MEDIUM) for `--network=host` / `--net=host`. Both are compound `and` rules on `command` and `args`, with no engine changes, and `TOXIC-007` is left to the maintainer. The description fills in the rule-submission template, shows the finding IDs for six configs before and after, lists the checks with their results (26 new tests, ruff, format, OWASP mapping, and the 7 `test_shadow.py` failures that also happen on unchanged `main` on my machine), says what I did not test (macOS, Windows, podman end to end), and has an AI-assistance paragraph.

**Maintainer Feedback:**

- 2026-11-02: none yet; the PR was opened this day.
- 2026-11-03: the maintainer said the rules and tests look good and the full suite passes in CI, but the `scripts/update_test_count.py --check` step failed: my 26 new tests moved the total to 8,441, and `CLAUDE.md`, `README.md` and `.github/release-notes-template.md` still quoted 8,415. They said they would merge once CI is green. Two macOS jobs were also cancelled after about 15 minutes, with no failing step.
- 2026-11-03: I ran the script with the same optional extras CI installs, which gave 8,441, the same number the maintainer quoted, and committed the four changed lines (`d4ccedd`). I had left those lines out before because the rule guide says to commit only the community-rule lines. I merged current `main` into the branch, pushed, and posted a comment on the PR saying so: https://github.com/adudley78/mcp-audit/pull/259#issuecomment-6620712918.
- 2026-11-03 (02:49 UTC on 2026-11-04): the maintainer merged the PR (merge commit `ff87f5d`) and commented that COMM-036 and COMM-037 ship in the next release, and that the `TOXIC-007` `--network=` false positive is noted for a separate fix.

**Status:** Merged

**Toolkit**

- Tool: the ship-gate, which ran my manifest checks and then my pr-precheck on the branch, title and `pr_draft.md`; the voice guard checked the description when I opened the PR.
- What it produced: a PASS in `gate-log.md` for the branch at commit `6e3ad03`, with the four manifest checks passing and all six pr-precheck checks passing, and PR #259 on `adudley78/mcp-audit`. The log also carries an advisory that a phrase in my `owasp-mapping.json` notes ("the maintainer confirms the code on review") reads as process talk.
- Difficulties: the first run stopped because the description claimed output that my evidence file did not contain; each run takes about two minutes for the tests; the pass lasts 30 minutes, which ran out before I opened the PR, so the hook ran the gate again.
- What changed: I saved the `rule validate`, `rule test`, demo scan and `rule list` output in `test_evidence.md` as section 6 and corrected one phrase in the description. I did not change the manifest or the rubric, because the check that stopped me was asking for something this repo's PR template also asks for.

---

## Learnings and Reflections

**Technical Skills Gained**

I learned how mcp-audit's rule engine matches a server: `args` are joined into one string and tested by a regex, and a compound `and` rule can require that `command` is `docker` or `podman` before the flag pattern counts. I learned to write the patterns with lookarounds (`(?<!\S)--privileged(?:=true)?(?!\S)`) so `--privileged=false` and a `docker.socket` path do not fire. I also learned what a rule needs besides its YAML file in this repo: a `PROVENANCE.md` entry, an OWASP mapping, a manual-test-matrix entry, and counts in two docs. And I learned to prove a test works by removing the fix: all 26 new tests fail without the rule files and pass with them.

**Challenges Overcome**

The scout accepted five weak issues in unit 5, including one whose repo had never merged an outside PR, so I added a required check for that and re-ran it. I took down my first claim comment and posted a new one after reading the whole thread and running the voice guard on it. In the build, `update_test_count.py` rewrote the test counts and left two community numbers stale, so I reverted the counts and fixed those numbers by hand. Seven `test_shadow.py` tests fail on unchanged `main` on my machine because `mcp-audit shadow` also finds my own Claude Code servers, so I excluded that class in my manifest with a dated reason and said so in the PR. The ship-gate stopped my description once because it claimed output I had not saved in my evidence file. At review, the check I had left out on purpose (the test-count lines) was the one that failed CI, and I fixed it the same day.

**What I'd Do Differently Next Time**

I would save the output of every command my description mentions as I run it, not after the gate asks for it. I would run `update_test_count.py --check` with the extras CI installs before opening the PR, and when a repo's guide and its CI disagree I would ask the maintainer on the thread first, since the guide's "leave those lines out" cost a review round. I would also run the test suite once with an empty home directory at the start, so the environment-only failures are known on day one. I would add the "problem still exists on the default branch" check to my scout rubric, which I have not added yet.

---

## Resources Used

- `CONTRIBUTING.md` and `docs/contributing-rules.md` in adudley78/mcp-audit: the rule-submission steps, the registrations a new rule needs and the checks to run.
- `rules/community/COMM-035.yml` and `src/mcp_audit/rules/engine.py`: the rule file I copied the shape from and the code that decides how `args` are matched.
- Issue thread https://github.com/adudley78/mcp-audit/issues/251: the maintainer's decision to split the work into COMM-036 (HIGH) and COMM-037 (MEDIUM), the test guidance and the `TOXIC-007` note.
- Docker's "Docker daemon attack surface" page, https://docs.docker.com/engine/security/#docker-daemon-attack-surface: the source cited for COMM-036's severity.
- PR #259's review comment from adudley78, which named the failing check and the script to run: https://github.com/adudley78/mcp-audit/pull/259.
