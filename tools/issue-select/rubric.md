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
| scope-feasible | Issue body: the work it asks for | The issue describes one identifiable piece of work someone could start: a behavior, a gap, or a task you can point at. It fails only when there is no single piece of work in it: a codebase-wide checklist, an "improve X everywhere", or a container issue tracking many sub-tasks. An open design edge, an "etc.", or several files involved never fails this check; that raises the difficulty note instead. | required |
| Outside contributions get merged | The repo's merged PRs (`gh pr list -R <repo> --state merged --limit 100 --json author,mergedBy,mergedAt`) | Pass if at least one PR merged within 90 days before capture was authored by someone who is neither the repo owner, nor the person who merged it, nor a bot (login ending in `[bot]` or author type Bot). Fail if every recent merged PR is the owner's or a bot's, or none has merged. | required |
| Work is available | The repo-facts block's assignees and linked PRs, plus the issue comment thread and label events | Pass if there is no open linked PR, no assignee, and no maintainer-confirmed active claim in the thread. A closed unmerged PR or an unconfirmed claim does not fail this check. | required |
| Contribution policy permits the workflow | The repo-facts block's contribution policy, including CONTRIBUTING.md, AI policy files, linked contributor docs, and PR/issue templates | Pass if the policy is silent or permits AI-assisted contributions under stated conditions; fail if it explicitly bans AI-generated or AI-assisted contributions. | required |
| Fits my skillset | The issue body and repo-facts block's language/framework and contribution-policy details, compared with my fit profile in scope.md | Pass if the issue or repository matches at least one listed skill or interest: C/C++, Python, JavaScript, TypeScript, React, Next.js, Flutter, Docker, server/backend work, self-hosting, or executable software. | preferred |


## Difficulty note

With each accepted candidate, report a one-line difficulty note in the
read-out summary:

- **straightforward**: the issue names where the change lives and the
  change is bounded.
- **moderate**: the location is yours to find, or several files are
  involved.
- **ambitious**: an open design edge, or an unfamiliar subsystem; name
  the edge, because claiming this issue means raising it with the
  maintainer early.

The note is information for the chooser, never a verdict input: it does
not appear in the fenced JSON block, it never changes accept or reject,
and in eval mode it is skipped entirely.

## Verdict rule

<!-- State how the grades above combine into accept or reject, and how
unclear is treated. Example shape (write your own): "accept if every
required check passes; preferred checks never change the verdict, they
rank accepted issues; unclear counts as fail." -->

Accept only when every required check passes. Preferred checks never change
the verdict; they rank issues that are accepted. Treat `unclear` as a fail
for required checks and as a non-passing preference for preferred checks.
