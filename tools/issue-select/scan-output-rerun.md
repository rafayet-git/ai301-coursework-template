Re-scan of 2026-11-01 after the rubric and strategy fixes: the same 3 queries returned 248 results. The new bot-author filter removed nexonic-tv-server#12 from the top 5, and li-ch/essun#1 took the fifth slot. Of the 5 graded, 3 are accepted and 2 rejected; the new "Outside contributions get merged" check and the extended scope check did the rejecting.

**Accepted, in fit order**

1. https://github.com/adudley78/mcp-audit/issues/251 - Rule request: Docker-launched MCP server given host access. Fit: Python, Docker and server/backend work. Surfaced by query 1 (Docker, Python); in the top 5 with 0 comments, no assignee, updated 2026-11-01 16:23. Outside PR #254 by Sainath-Reddy7 was merged by the owner on 2026-11-01.
2. https://github.com/bolubo/checkpoint-governor/issues/102 - docs: a first-ten-minutes page. Fit: Docker and executable software. Surfaced by query 2 (Docker, Go); in the top 5 with 0 comments, no assignee, updated 2026-11-01 14:12:10. Seven outside PRs merged between 2026-10-23 and 2026-10-27, all by the owner.
3. https://github.com/bolubo/checkpoint-governor/issues/108 - test: the README's code blocks should be executable. Fit: executable software only. Surfaced by query 2 (Docker, Go); in the top 5 with 0 comments, no assignee, updated 2026-11-01 14:12:27. Same merge history as #102.

**Rejected**

- https://github.com/knowndevice/knowndevice/issues/21 - failed "Scope fits a newcomer" (body says "Depends on: #11" and #11 is open) and "Outside contributions get merged" (0 merged PRs in the repo). Surfaced by query 2; ranked first on updated time.
- https://github.com/li-ch/essun/issues/1 - failed "Outside contributions get merged" (0 merged PRs in the repo). Surfaced by query 1; ranked fifth on updated time.

```json
[
  {
    "item": "https://github.com/adudley78/mcp-audit/issues/251",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Issue opened 2026-11-01 by the Owner (adudley78); recent commits by adudley78 the same day"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; latest release 2026-10-31"},
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "One bounded outcome: add one YAML rule, test it against two examples, update two docs files; no dependency stated"},
      {"name": "Outside contributions get merged", "grade": "pass", "evidence": "PR #254 by Sainath-Reddy7 merged by adudley78 on 2026-11-01"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; no open PRs in the repo; 0 comments; body says 'Comment here to claim it'"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md mentions cloud agents without banning AI; repo has CLAUDE.md"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "Python repo; the rule is about docker run flags"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/bolubo/checkpoint-governor/issues/102",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Issue opened 2026-11-01 by the Owner (bolubo); commits by bolubo the same day"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; latest release 2026-11-01"},
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "One documentation deliverable (docs/first-ten-minutes.md) with acceptance and boundary stated; no dependency"},
      {"name": "Outside contributions get merged", "grade": "pass", "evidence": "7 outside PRs merged by bolubo, e.g. #91 by bh-official on 2026-10-27 and #86 by Aaqibhafeezkhan on 2026-10-26"},
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
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "One bounded test with acceptance ('make verifyy' turns it red) and an explicit boundary; no dependency"},
      {"name": "Outside contributions get merged", "grade": "pass", "evidence": "7 outside PRs merged by bolubo, e.g. #91 by bh-official on 2026-10-27 and #86 by Aaqibhafeezkhan on 2026-10-26"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; open PRs #124 and #127 do not reference #108; 0 comments"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md is a conventions file with no AI ban; policy is silent"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "Go test over the ckptctl CLI; matches executable software only"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/knowndevice/knowndevice/issues/21",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Latest default-branch commit 2026-10-30 by karauda, within 90 days"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; no release, but the push is within 90 days"},
      {"name": "Scope fits a newcomer", "grade": "fail", "evidence": "Body says 'Depends on: #11 (KD-007)' and #11 is still open"},
      {"name": "Outside contributions get merged", "grade": "fail", "evidence": "gh pr list --state merged returns 0 PRs for the repo"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; open PRs #47-#50 do not reference #21; 0 comments"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md has no AI mention; policy is silent"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "Body says it requires Docker; it is backend work over an MQTT broker"}
    ],
    "verdict": "reject"
  },
  {
    "item": "https://github.com/li-ch/essun/issues/1",
    "checks": [
      {"name": "Maintainer is active", "grade": "pass", "evidence": "Issue opened 2026-11-01 by the Owner (li-ch); commits by Li Chen the same day"},
      {"name": "Repository is in use", "grade": "pass", "evidence": "Not archived; last push 2026-11-01; no release, but the push is within 90 days"},
      {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "One outcome: walk a reproduction card on a clean clone and report friction in a comment; no dependency"},
      {"name": "Outside contributions get merged", "grade": "fail", "evidence": "gh pr list --state merged returns 0 PRs for the repo"},
      {"name": "Work is available", "grade": "pass", "evidence": "assignees=0; no linked PR; 0 comments"},
      {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "CONTRIBUTING.md has no AI ban; policy is silent"},
      {"name": "Fits my skillset", "grade": "pass", "evidence": "Python repo (GPU network fabric simulator)"}
    ],
    "verdict": "reject"
  }
]
```
