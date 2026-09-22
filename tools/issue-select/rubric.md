# Rubric: is this a good first issue?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever checks
you define here. It ships empty on purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where. Name the source
     (repo-facts block, issue body, comment thread, or the locations in
     references/evidence-guide.md). "The repo" is not a source; "the last
     5 default-branch commit dates" is.
   - Pass condition: a condition someone else could apply and get your
     answer. Prefer thresholds with numbers ("a maintainer commented
     within 30 days") over adjectives ("maintainer is responsive").
   - Weight: `required` (a fail here rejects the issue) or `preferred`
     (never changes the verdict; a nice-to-have that helps rank the
     issues you accept).

2. A verdict rule below the table: how the check grades combine into
   accept or reject, including how `unclear` is treated. The verdict
   space is binary. If you write no rule for `unclear`, the skill treats
   it as fail.

Cover what actually kills first contributions. The lecture named four
families: the maintainer is alive, the repo is in use, the scope fits a
newcomer, and nobody else is already on it. A rubric that ignores a family
will fail eval issues designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Maintainer is active | The issue's comment thread and the repo-facts block's maintainer first-response sample, last 5 default-branch commits, and capture date | Pass if a maintainer (Owner, Member, or Collaborator) commented on the issue within 30 days before capture, or the sample shows at least one maintainer response to another issue within 30 days before capture, or at least one of the last 5 default-branch commits is dated within 90 days before capture. | required |
| Repository is in use | The repo-facts block's archived flag, last push to any branch, latest release, and star count | Pass if the repository is not archived and either its last push was within 90 days before capture or its latest release was within 180 days before capture. | required |
| Scope fits a newcomer | The issue body and comment thread, including labels, acceptance criteria, design decisions, and any history of abandoned attempts | Pass unless the bundle explicitly identifies the issue as an umbrella, tracking list, or megaissue; asks only a pure usage question; records unresolved design debate; says the fix requires core-internals changes; leaves a key product/design decision unresolved, such as a required asset or specification being TBD; or shows repeated abandoned attempts (multiple closed unmerged PRs or multiple stale claims) indicating the task is unusually difficult. A specific bug, documentation deliverable, or feature request passes even if it spans multiple files or names several potential causes or implementation suggestions, provided it describes one user-visible outcome. A single closed PR, stale label, or old claim alone does not fail scope. | required |
| Work is available | The repo-facts block's assignees and linked PRs, plus the issue comment thread and label events | Pass if there is no open linked PR, no assignee, and no maintainer-confirmed active claim in the thread. A closed unmerged PR or an unconfirmed claim does not fail this check. | required |
| Contribution policy permits the workflow | The repo-facts block's contribution policy, including CONTRIBUTING.md, AI policy files, linked contributor docs, and PR/issue templates | Pass if the policy is silent or permits AI-assisted contributions under stated conditions; fail if it explicitly bans AI-generated or AI-assisted contributions. | required |
| Fits my skillset | The issue body and repo-facts block's language/framework and contribution-policy details, compared with my fit profile in scope.md | Pass if the issue or repository matches at least one listed skill or interest: C/C++, Python, JavaScript, TypeScript, React, Next.js, Flutter, Docker, server/backend work, self-hosting, or executable software. | preferred |


## Verdict rule

<!-- State how the grades above combine into accept or reject, and how
unclear is treated. Example shape (write your own): "accept if every
required check passes; preferred checks never change the verdict, they
rank accepted issues; unclear counts as fail." -->

Accept only when every required check passes. Preferred checks never change
the verdict; they rank issues that are accepted. Treat `unclear` as a fail
for required checks and as a non-passing preference for preferred checks.
