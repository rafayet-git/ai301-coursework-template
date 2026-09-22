# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

Record of the issue carried into Unit 2, and of the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in
the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the
wrong label is not graded.

---

## Selected issue

**Issue link**

[Issue #9: Implement a caching layer for repeated identical portfolio queries](https://github.com/codepath/pathreview-ai301-fa26-s3/issues/9)

**Verdict output**

Accepted candidates, ranked by fit:

1. Issue 9: Python backend caching work, closest to my backend and self-hosting interests.
2. Issue 7: Python backend RAG work, with a somewhat more open-ended debugging scope.
3. Issue 11: A bounded documentation task, with less direct backend implementation experience.

```json
[
   {
      "item": "https://github.com/codepath/pathreview-ai301-fa26-s3/issues/9",
      "checks": [
         {"name": "Maintainer is active", "grade": "pass", "evidence": "The last default-branch commit was 2026-09-16, and maintainer Aburke225 commented on issues #52 and #43 on 2026-09-16."},
         {"name": "Repository is in use", "grade": "pass", "evidence": "The repository is not archived and was pushed to on 2026-09-16, six days before capture."},
         {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "The issue specifies a cache keyed by profile content hash, names two files, and has one user-visible outcome; it has no comments or unresolved design debate."},
         {"name": "Work is available", "grade": "pass", "evidence": "The issue has no comments, no assignee, and the repository has zero open pull requests."},
         {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "docs/CONTRIBUTING.md and .github/PULL_REQUEST_TEMPLATE.md are silent on AI-generated and AI-assisted contributions."},
         {"name": "Fits my skillset", "grade": "pass", "evidence": "The issue is Python backend caching work labeled devops/rag, matching my backend and self-hosting interests."}
      ],
      "verdict": "accept"
   },
   {
      "item": "https://github.com/codepath/pathreview-ai301-fa26-s3/issues/7",
      "checks": [
         {"name": "Maintainer is active", "grade": "pass", "evidence": "The repository has a maintainer-authored commit and maintainer comments dated 2026-09-16."},
         {"name": "Repository is in use", "grade": "pass", "evidence": "The repository is not archived and was pushed to on 2026-09-16."},
         {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "The issue describes one stale-embedding bug with one user-visible outcome and has no comments or unresolved design debate."},
         {"name": "Work is available", "grade": "pass", "evidence": "The issue has no comments, no assignee, and the repository has zero open pull requests."},
         {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "The contribution policy is silent on AI use."},
         {"name": "Fits my skillset", "grade": "pass", "evidence": "The issue concerns Python RAG retriever and ingestion files, matching my Python and backend interests."}
      ],
      "verdict": "accept"
   },
   {
      "item": "https://github.com/codepath/pathreview-ai301-fa26-s3/issues/11",
      "checks": [
         {"name": "Maintainer is active", "grade": "pass", "evidence": "The repository has a maintainer-authored commit and maintainer comments dated 2026-09-16."},
         {"name": "Repository is in use", "grade": "pass", "evidence": "The repository is not archived and was pushed to on 2026-09-16."},
         {"name": "Scope fits a newcomer", "grade": "pass", "evidence": "The issue is a bounded documentation change to docs/ARCHITECTURE.md with no comments or unresolved design debate."},
         {"name": "Work is available", "grade": "pass", "evidence": "The issue has no comments, no assignee, and the repository has zero open pull requests."},
         {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "The contribution policy is silent on AI use."},
         {"name": "Fits my skillset", "grade": "pass", "evidence": "The repository is a Python/React backend project, matching my general server and backend interests."}
      ],
      "verdict": "accept"
   }
]
```

## Eval iterations

**Run history**

1. `15/20` (initial complete run)
2. `2/5` (focused disagreement run)
3. `2/5` (focused disagreement run)
4. `5/5` (focused disagreement run)
5. `18/20` (complete run)
6. `2/2` (focused issue-15 and issue-19 run)
7. `19/20` (complete run)
8. `3/3` (focused issue-09, issue-15, and issue-19 run)
9. `20/20` (final complete run)

**Issue analysis**

For `issue-09`, my rubric decided `accept`, and the gold label was also `accept`. The issue describes a specific `conda config --clear` feature, the repository is active, there is no assignee, and the only linked PR is closed. My rubric treats recent repository activity as evidence that maintainers are available and treats one old closed attempt as insufficient by itself to reject a bounded issue.

**Check rationale**

> **Scope fits a newcomer** | The issue body and comment thread, including labels, acceptance criteria, design decisions, and any history of abandoned attempts | Pass unless the bundle explicitly identifies the issue as an umbrella, tracking list, or megaissue; asks only a pure usage question; records unresolved design debate; says the fix requires core-internals changes; leaves a key product/design decision unresolved, such as a required asset or specification being TBD; or shows repeated abandoned attempts (multiple closed unmerged PRs or multiple stale claims) indicating the task is unusually difficult. A specific bug, documentation deliverable, or feature request passes even if it spans multiple files or names several potential causes or implementation suggestions, provided it describes one user-visible outcome. A single closed PR, stale label, or old claim alone does not fail scope. | required |

This check distinguishes a bounded task with one stale historical attempt from a task whose repeated abandoned attempts indicate that its real difficulty is higher than its label suggests. The final form was made after revisions from previous eval iterations, to provide clarity on certain disagreements.

**Trade-offs**

The scope check may accept a difficult issue with several implementation causes, such as `issue-19`, because it describes one user-visible outcome. I re-ran the boundary cases `issue-09`, `issue-15`, and `issue-19` with `--only`: they produced `accept`, `reject`, and `accept`, respectively. This preserves the stale-single-attempt case while rejecting repeated abandoned attempts.

## Selection rationale

**Selection rationale**

1. Issue 9 fits my interest in backend and server-side work because a caching layer involves query behavior and improving performance. I believe its scope is narrow enough to investigate and implement within the available time.

2. The verdict correctly identifies the issue as a concrete backend-oriented contribution in the PathReview repository. I also weighed whether the caching behavior and test coverage would make the task larger than the short issue title suggests, which the rubric cannot fully measure that implementation detail.

3. The likely difficulty in claiming it is moderate: I need to confirm that nobody else has claimed it, understand the existing query path, and agree on cache keys and invalidation with the maintainer before coding. I will not comment or claim it until Unit 2 provides the claiming workflow.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/issue-select/`.
