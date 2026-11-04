Scan of 2026-11-01: 3 queries returned 248 results (100 + 100 + 48). After dropping duplicates, assigned issues, issues with 5 or more comments and issues not updated in 60 days, the top 5 by fewest comments, then most recently updated, were graded. All 5 are accepted; rank below is by fit with my profile (most listed interests matched first).

**Accepted, in fit order**

1. https://github.com/Shahrukhalid/nexonic-tv-server/issues/12 - Docker image for one-command home server/NAS deployment. Fit: matches Docker, self-hosting, TypeScript and server/backend work. Surfaced by query 3 (self-hosted, TypeScript); in the top 5 with 0 comments, no assignee, updated 2026-11-01 18:35. Tension: the issue is written by a bot (nexonic-sentinel[bot]) and bundles six acceptance criteria, including passing on Synology DSM 7+ and TrueNAS SCALE, which I cannot test. The rubric's scope check has no condition for this, so it passes; the fix belongs in the rubric.
2. https://github.com/adudley78/mcp-audit/issues/251 - Rule request: Docker-launched MCP server given host access. Fit: matches Python, Docker and server/backend work. Surfaced by query 1 (Docker, Python); in the top 5 with 0 comments, no assignee, updated 2026-11-01 16:23. The owner wrote it as "Rule idea for a first contribution" with an explicit step list, a contributing guide and "Comment here to claim it". Repo has a CLAUDE.md, so AI-assisted work is expected.
3. https://github.com/knowndevice/knowndevice/issues/21 - Test retained and wrong-generation MQTT replies on the real broker. Fit: matches Docker and server/backend work (Go is not on my list). Surfaced by query 2 (Docker, Go); in the top 5 with 0 comments, no assignee, updated 2026-11-01 19:06. Tension: the issue says "Depends on: #11", and #11 is still open and unassigned, so the work may not be startable yet. The rubric has no dependency check, so it passes; the fix belongs in the rubric.
4. https://github.com/bolubo/checkpoint-governor/issues/102 - docs: a first-ten-minutes page. Fit: matches Docker and executable software (docker build/run and the ckptctl CLI). Surfaced by query 2 (Docker, Go); in the top 5 with 0 comments, no assignee, updated 2026-11-01 14:12:10.
5. https://github.com/bolubo/checkpoint-governor/issues/108 - test: the README's code blocks should be executable. Fit: matches executable software only (a Go test over a CLI's commands). Surfaced by query 2 (Docker, Go); in the top 5 with 0 comments, no assignee, updated 2026-11-01 14:12:27.

**Rejected:** none.

**Friction for scan-notes.md**
- All five repos are tiny (0 to 5 stars) and were created or became active in the last few days, and several issues read as machine-written. The rubric's repo-in-use check passes them because the last push is recent, but it says nothing about whether anyone other than the owner reviews or merges contributions.
- The rubric has no check for an unmerged dependency (knowndevice#21) or for work that needs hardware I do not have (nexonic-tv-server#12).
- The nested `claude -p "issue-scout: run a scan"` run was blocked on `gh search` permission approval, so this scan was run from the interactive session instead.

```json
[
  {
    "item": "https://github.com/Shahrukhalid/nexonic-tv-server/issues/12",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Last 5 default-branch commits include 2026-11-01 by Shahrukhalid, within 90 days"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; latest release 2026-10-29"},
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "One user-visible outcome (a Docker image that runs with one command); not an umbrella, no design debate, no abandoned attempts"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; no linked PR; 0 comments, so no claim in the thread"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "No CONTRIBUTING.md, AI policy file or PR template found; policy is silent"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "Docker, self-hosting, TypeScript and server/backend work all match the fit profile"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/adudley78/mcp-audit/issues/251",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Issue opened 2026-11-01 by the Owner (adudley78); recent commits by adudley78 the same day"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; latest release 2026-10-31"},
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "One bounded outcome: add one YAML rule, test it against two examples, update two docs files; the guide is linked"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; no open PRs in the repo; 0 comments; body says 'Comment here to claim it'"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md mentions cloud agents without banning AI; repo has CLAUDE.md"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "Python repo; the rule is about docker run flags"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/knowndevice/knowndevice/issues/21",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Latest default-branch commit 2026-10-30 by karauda, within 90 days"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; no release, but the push is within 90 days"},
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "Body calls it a 'bounded contribution' with three acceptance criteria; the rubric lists no condition for an open dependency (#11 is open)"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; open PRs #47-#50 do not reference #21; 0 comments"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md has no AI mention; policy is silent"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "Body says it requires Docker; it is backend work over an MQTT broker"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/bolubo/checkpoint-governor/issues/102",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Issue opened 2026-11-01 by the Owner (bolubo); commits by bolubo the same day"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; latest release 2026-11-01"},
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "One documentation deliverable (docs/first-ten-minutes.md) with acceptance and boundary stated"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; open PRs #124 and #127 do not reference #102; 0 comments"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md is a conventions file with no AI ban; policy is silent"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "Page walks through docker build, docker run and the ckptctl CLI"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/bolubo/checkpoint-governor/issues/108",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Issue opened 2026-11-01 by the Owner (bolubo); commits by bolubo the same day"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; latest release 2026-11-01"},
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "One bounded test with acceptance ('make verifyy' turns it red) and an explicit boundary"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; open PRs #124 and #127 do not reference #108; 0 comments"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md is a conventions file with no AI ban; policy is silent"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "Go test over the ckptctl CLI; matches executable software only"}
    ],
    "verdict": "accept"
  }
]
```

---

## Direct grading of my two Issue Selection site picks (2026-11-01)

Graded with the current rubric.md (including the "Outside contributions get merged" check and the extended scope check). Both issues are "direct" input (no query, no ranking). Run from the interactive session rather than a nested `claude` run, for the permission reason in scan-notes.md.

**Accepted**

1. https://github.com/Priyanshu-byte-coder/devtrack/issues/158 - Link each TopRepos row to its GitHub repo. Fit: TypeScript and React. Passes every required check. Big caveat: the work appears to be done already. On main, `src/components/TopRepos.tsx` lines 112-118 already render `<a href={repo.url || ...} target="_blank" rel="noopener noreferrer" aria-label={`Open ${repo.name} in GitHub`}>`, and PR #281 (merged 2026-05-19) added the aria-label. The rubric has no check for "the problem still exists on the default branch", so it accepts; the fix belongs in the rubric.

**Rejected**

2. https://github.com/badges/shields/issues/4656 - More AUR badges. Sunk by "Scope fits a newcomer": the body lists seven separate badges, and the maintainer reply says they will only take badges that someone actually wants, which was never settled (thread silent since 2020-04-05). Everything else passes, and fit is JavaScript and backend work. A prior attempt, PR #12217 ("[AUR] Add out-of-date badge", "Closes #4656"), was closed unmerged on 2026-10-06 with no review comment; one closed PR alone does not fail scope.

```json
[
  {
    "item": "https://github.com/Priyanshu-byte-coder/devtrack/issues/158",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Owner commit 2026-10-18; owner comment on this issue 2026-10-14"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-10-31; latest release 2026-06-09"},
      {"name": "Outside contributions get merged", "grade": "pass", "evidence": "8 PRs by non-owner, non-bot authors merged since 2026-08-03"},
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "Body: 'a single <a> wrapper change' in src/components/TopRepos.tsx, no dependency or hardware needs; note the change is already on main"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; PR #281 is merged, not open; bot assigned the owner 2026-10-14 with 7-day auto-unassign; earlier claimant ParidhiMis unassigned 2026-10-14"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md: unreviewed AI output is labelled invalid or spam, a condition not a ban"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "TypeScript repo; React component"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/badges/shields/issues/4656",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Member LitoMore commented in the repo 2026-11-01; maintainers merged outside PRs 2026-10-24"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; 27357 stars"},
      {"name": "Outside contributions get merged", "grade": "pass", "evidence": "5 PRs by non-owner, non-bot authors merged since 2026-08-03"},
      {"name": "Scope fits a newcomer", "grade": "fail", "evidence": "Body lists seven separate AUR badges; chris48s: 'lets ensure we're adding badges for things that at least someone actually wants to use', never resolved"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; PR #12217 closed unmerged; 2020 claim by Raymo111 never confirmed"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md and PR template have no AI mention; policy is silent"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "JavaScript repo; badge services are backend work"}
    ],
    "verdict": "reject"
  }
]
```

---

## Re-grade of adudley78/mcp-audit#251 after the scope patch (2026-11-02)

Graded with the patched rubric (scope-feasible row, difficulty note). **Accepted.** Difficulty note: **moderate**. The issue names where the work lives (a rule YAML, a PROVENANCE.md line, docs/owasp-mapping.json, docs/manual-test-matrix.md, then `uv run pytest`), but it touches several files. Two things to watch: only one outside human PR has merged in the last 90 days (Sainath-Reddy7's #254), so the merge check passes on a single data point; and the owner had not replied to my claim comment (posted 2026-11-02) when I checked.

```json
{
  "item": "https://github.com/adudley78/mcp-audit/issues/251",
  "checks": [
    {"name": "Maintainer is active", "grade": "pass", "evidence": "Owner adudley78 committed 2026-11-01 20:22 and commented on the repo the same day"},
    {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; latest release 2026-10-31"},
    {"name": "scope-feasible", "grade": "pass", "evidence": "One piece of work: add one rule for docker run with host-level flags, with should-fire and should-not-fire examples"},
    {"name": "Outside contributions get merged", "grade": "pass", "evidence": "1 PR by a non-owner, non-bot author merged since 2026-08-03 (#254, Sainath-Reddy7, merged by adudley78)"},
    {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; no open PRs in the repo; the only comment is my own claim, 2026-11-02"},
    {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md has no AI ban; repo has a CLAUDE.md"},
    {"name": "Fits my skillset", "grade": "pass", "evidence": "Python repo; rule is about docker run flags"}
  ],
  "verdict": "accept"
}
```

---

## Re-grade of my two Issue Selection site picks after the scope patch (2026-11-02)

Same two issues as 2026-11-01, graded with the patched rubric (scope-feasible row, difficulty note). Direct input; run from the interactive session.

**Accepted, with difficulty notes**

1. https://github.com/badges/shields/issues/4656 - More AUR badges. Verdict flipped from reject to accept: the old scope check failed on the unsettled badge list, and scope-feasible only asks for one identifiable piece of work, which "add AUR badges" is. Difficulty: **ambitious**. The open edge is which badges the maintainers actually want: chris48s's 2020 reply says they will only take badges "someone actually wants to use", and it was never settled. Claiming this means asking that first. Other signals: the repo is very active, 5 outside PRs merged in 90 days, no assignee, and PR #12217 (out-of-date badge, "Closes #4656") was closed unmerged on 2026-10-06 with no review comment.
2. https://github.com/Priyanshu-byte-coder/devtrack/issues/158 - Link each TopRepos row to its GitHub repo. Still accepted. Difficulty: **straightforward** by the issue text (one file, `src/components/TopRepos.tsx`). Two caveats the rubric does not capture: the change is already on main (the `<a href target="_blank" rel="noopener noreferrer" aria-label=...>` is there, PR #281 merged 2026-05-19), and six people asked to work on it between 2026-05-16 and 2026-06-21, so under the course's rule it counts as taken even though it is unassigned.

```json
[
  {
    "item": "https://github.com/badges/shields/issues/4656",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Member LitoMore commented in the repo 2026-11-01; maintainers merged outside PRs 2026-10-24"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; 27357 stars"},
      {"name": "scope-feasible", "grade": "pass", "evidence": "One identifiable task: add AUR badges (popularity, maintainer, out-of-date and others); not a codebase-wide checklist or container issue"},
      {"name": "Outside contributions get merged", "grade": "pass", "evidence": "5 PRs by non-owner, non-bot authors merged since 2026-08-03"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; PR #12217 closed unmerged; the only open AUR-adjacent PR (#12257) is for Repology; 2020 claim never confirmed"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md and PR template have no AI mention; policy is silent"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "JavaScript repo; badge services are backend work"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/Priyanshu-byte-coder/devtrack/issues/158",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Owner commit 2026-10-18; owner comment on this issue 2026-10-14"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-10-31; latest release 2026-06-09"},
      {"name": "scope-feasible", "grade": "pass", "evidence": "Body: one component change in src/components/TopRepos.tsx"},
      {"name": "Outside contributions get merged", "grade": "pass", "evidence": "8 PRs by non-owner, non-bot authors merged since 2026-08-03"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; no open linked PR; earlier claimant ParidhiMis unassigned 2026-10-14"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md: unreviewed AI output is labelled invalid or spam, a condition not a ban"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "TypeScript repo; React component"}
    ],
    "verdict": "accept"
  }
]
```
