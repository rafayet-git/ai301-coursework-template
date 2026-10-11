---
name: pr-precheck
description: Grade a PR package (a candidate pull request read against the plan it claims to implement and the issue that plan belongs to) and decide whether it is ready to submit. Use when checking your own branch, draft PR title, and description before opening the pull request, or when grading an eval package bundle.
---

# pr-precheck: rubric-driven PR grading

<!--
THIS IS THE PART YOU WRITE, and it is the last one: the frame itself.
Weeks 1 through 3 handed you a working SKILL.md and you filled the
files behind it; this week the frame ships as headings, and you write
what it says. The frontmatter above and the section headings below are
fixed (CONTRACT.md's layout rule); the instructions under each heading
are yours. Write instructions to the tool, in the imperative, the way
weeks 1-3's frames spoke to you: what to read, in what order, what to
refuse, what to emit. Your executor in the rotation is the test: a
frame gap they hit (cannot tell what the tool reads, or how a verdict
gets assembled) is a missing sentence here.

One section is not yours: the JSON schema in "Verdict and output" is
reproduced from CONTRACT.md verbatim and may not be altered. Your
words decide everything around it.
-->

## The question

<!-- State, in your words, the one question this tool answers and what
a PR package is: what artifacts it contains and what they are read
against. CONTRACT.md fixes the question; your frame has to say it so
the tool cannot wander into grading something else. -->

Answer one question: is this PR package ready to submit? A package is
the candidate PR title and description, the branch diff, its commits and
test evidence, read against the posted plan and the issue that plan belongs
to. Judge whether the proposed change implements the plan, stays within the
issue's scope, and has credible verification; do not review unrelated code or
predict whether a maintainer will merge it.

## Inputs and modes

<!-- Define both modes. Live mode: name every input (your plan.md with
its deviation notes, your branch's diff, your draft PR title and
description, your test evidence, your issue), where each comes from,
and what a house-chain student reads instead. The branch's diff is
everything the branch changes relative to the repo's default branch:
`git diff main...HEAD` (three dots), run from the working copy, is
the command that produces it; name the source that concretely. Eval
mode: state that the bundle is the whole world, nothing is fetched,
and every check runs with the full verdict rule. -->

Use exactly one of these modes:

- **Live mode:** read `plan.md` from the working folder, including its
  deviations section; read the draft PR title and description from the files
  named in the user's command; read the branch's commits and the complete
  `git diff main...HEAD` from the working copy; read the test evidence named in
  the draft or command; and gather the issue thread, PR template, and
  `docs/CONTRIBUTING.md` from the scoped GitHub repository. Read the plan
  before the diff so implementation is judged against the promised scope.
  For a house-chain student, use the house plan and house repro pack quoted
  in the package instead of inventing a personal plan or repro.
- **Eval mode:** read one frozen package bundle supplied by the harness. The
  bundle is the entire world: use only its issue, plan, PR title/description,
  commits, diff, tests, repo-facts, and policy text. Do not fetch GitHub, read
  local files, or fill gaps from memory. Grade every rubric check and apply the
  full verdict rule.

## The scope seam (live mode only)

<!-- Tell the tool when to read scope.md, what to do with the rules it
finds there, what to refuse, and what to do when the scope's repo line
is an unfilled placeholder. State that eval mode ignores scope.md
entirely. CONTRACT.md names the required behavior; your frame has to
instruct it. -->

In live mode, read `scope.md` before the issue or drafts. Confirm that the issue
and PR target belong to its `Repo:` line and apply every house rule it states,
including fork, branch, template, and shared-issue rules. If the repo line is
an unfilled placeholder, stop and tell the user to obtain the cohort scope
file; never guess the repository. Refuse work outside the scoped repository.
In eval mode, ignore `scope.md` completely because the package bundle defines
the world.

## The voice seam (live mode only)

<!-- Tell the tool when to read voice-guide.md, which outgoing text it
gates (the PR title and description), how to report a broken rule, and
why it never changes the verdict on its own. State that eval mode
ignores it entirely. -->

In live mode, read `voice-guide.md` before grading the draft PR title and
description. Report each broken voice rule in the readable summary, quoting the
rule and the offending wording. Voice findings do not change the verdict unless
the rubric includes a communication check that makes them consequential. In
eval mode, ignore `voice-guide.md`; universal communication requirements come
from the rubric and package evidence only.

## Component reads

<!-- Tell the tool how the pieces connect: rubric.md defines the
checks and the verdict rule, references/evidence-guide.md maps where
each evidence family lives, procedure.md is executed as written. Say
what the tool does when the procedure is silent on a step (report the
gap, never improvise around it) and what it does when rubric.md or
procedure.md has no content (the refusal rule, stated as an
instruction). -->

Read `rubric.md` to obtain the checks, weights, and verdict rule. Read
`references/evidence-guide.md` to locate each evidence family. Execute
`procedure.md` exactly as written for read order, evidence gathering, check
execution, and verdict assembly. If the procedure is silent or ambiguous,
report the procedure gap and do not invent a replacement step. If the rubric
has no filled checks or no verdict rule, or if the procedure has no authored
steps, refuse to grade and say which component is empty.

## Verdict and output

<!-- State the binary verdict space (accept means submit, reject means
hold) and instruct the tool to end its reply with the fenced JSON
block below, valid and last, with nothing after it. The schema is
CONTRACT.md's, verbatim; do not edit it. -->

The verdict is binary: `accept` means the PR is ready to submit and `reject`
means hold it for revision. Execute every required check, name the fact or
quote that decided each grade, and apply the rubric's treatment of `unclear`.
Before the JSON block, provide only a concise per-check summary and any live
voice-rule findings. End with exactly one valid fenced JSON block using the
schema below, with nothing after it.

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

## Grading discipline

<!-- Write the standing rules the tool grades under: evidence first,
grade the thing not the polish, the rubric decides, the procedure
decides how, and how unclear grades are treated when the rubric's
verdict rule is silent. CONTRACT.md states each as a guarantee; your
frame has to make them instructions. -->

- Gather evidence before assigning a grade; every check needs one deciding
  fact or quote.
- Grade the actual diff, tests, title, and description against the plan and
  issue, not their headings, length, formatting, or confidence.
- Let `rubric.md` decide pass/fail and let `procedure.md` decide how evidence
  is gathered; report gaps instead of silently compensating for them.
- Treat `unclear` according to the rubric; if the rubric is silent, treat it as
  a failure.
- Never use outside live information in eval mode, and never use a local file
  that the live command did not name as package evidence.
