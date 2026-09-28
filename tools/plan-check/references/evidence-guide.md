# Evidence guide: where evidence lives in a plan package

<!--
THIS IS THE PART YOU WRITE (second week running: the judgment files
stay in your hands). The skill uses this guide as its map: for every
kind of evidence a rubric check names, this file says WHERE to find it
in a plan package and WHAT GOOD LOOKS LIKE when you do.

Under each family heading below, write:

- Where it lives: the exact places to look. In an eval bundle (which
  section of the package: the issue context, the repro-evidence block,
  the candidate plan's scope statement or test plan, the plan comment,
  the repo-facts block). In live mode (where on GitHub or in the
  draft: the issue thread, the student's posted repro comment, the
  repo's docs, the draft plan and comment).
- What good looks like: one or two sentences someone else could apply.
  Prefer observable conditions ("the stated cause cites behavior the
  repro evidence actually shows") over adjectives ("diagnosis is
  solid").

A rubric check whose evidence this guide cannot locate is a check
nobody else can execute, and this week that cuts twice: your
procedure.md tells the skill WHEN to gather each family, and this
guide tells it WHERE. Write the map you wish your executor had.
-->

## Diagnosis and grounding

<!-- Where the plan states its cause, and where the repro evidence
pins down the behavior that cause must explain. What it means for a
diagnosis to follow from the evidence rather than contradict or
ignore it. -->

In eval bundles, read the issue context first, then the repro-evidence block's
environment, trigger, control, and observed output, and finally the plan's
diagnosis. In live mode, read the issue page and thread, the student's posted
repro comment, and the draft plan. Record the exact behavior the diagnosis must
explain and any control that rules out a tempting cause. A contradiction or an
unexplained control is a fail unless the plan labels it an open hypothesis and
proposes a check.

## Scope

<!-- Where the plan bounds itself: the in-scope statement, the
not-in-scope line, the files or areas named. What one bounded change
looks like next to a drive-by rewrite. -->

Read the plan's scope statements and named files against the issue request and
the smallest change that addresses the reproduced behavior. Record additions
that are not needed for the issue, such as migrations, redesigns, unrelated
refactors, or broad abstraction work. A bounded plan may defer a follow-up when
it says why and preserves the issue's requested outcome.

## Executability

<!-- Where the plan says what will actually be done: files or areas,
approach, order of work. What it means for a stranger to be able to
start executing without asking the author anything. -->

Read the plan's ordered steps, file and symbol references, data flow, and
dependencies. Record the first concrete implementation action and whether each
later action follows from it. A stranger should not have to choose between
multiple architectures, locate an unnamed layer, or infer how the change reaches
the failing path.

## Test plan

<!-- Where the plan says how success will be observed, and how that
maps onto the repro evidence's steps and artifacts. What a decisive
test plan names that a vague one does not. -->

Read the plan's tests, fixtures, commands, controls, and expected results next
to the repro evidence's trigger and artifact. Record the exact observable that
proves the fix, such as an exit code, output value, log event, request count, or
UI state, and the control that must remain unchanged. A generic full-suite
promise without a fix-specific assertion is not decisive evidence.

## Honesty

<!-- Where claims meet uncertainty: risks, unknowns, and deviations.
How to tell stated unknowns from false confidence, and where an
honest mid-build deviation gets recorded. -->

Read the plan's assumptions, risks, alternatives, and fallback choices. A good
plan distinguishes what the repro established from what still needs discovery,
sets a decision point for unresolved tool or compatibility questions, and does
not turn a proposed cause or future result into a fact. In live mode, a later
deviation must be recorded in the updated plan before another plan comment is
posted.

## Comms

<!-- Where the words meet the thread and the repo: the plan comment
read against the issue's maintainer signals (thread highlights, or
the live thread) and against the repo-facts block's stated templates,
contributing asks, and contribution policy (including AI-use
disclosure requirements). What thread-aware looks like next to
boilerplate. -->

In eval bundles, read the plan comment against thread highlights and the
repo-facts block. In live mode, read the issue thread, repository contribution
docs/templates, and the draft comment. Record maintainer directions, prior-art
PRs, requested tests, branch conventions, and disclosure requirements before
grading. A compliant comment names its approach and scope in its own words and
acknowledges relevant thread guidance; "same as above" or a generic promise does
not pass.
