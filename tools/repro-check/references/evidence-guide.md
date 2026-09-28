# Evidence guide: where proof lives in a reproduction package

<!--
THIS IS THE PART YOU WRITE (new this week: Unit 1 handed you this file
finished; the scaffolding fades). The skill uses this guide as its map:
for every kind of proof a rubric check names, this file says WHERE to
find it in a package and WHAT GOOD LOOKS LIKE when you do.

Under each family heading below, write:

- Where it lives: the exact places to look. In an eval bundle (which
  section of the package: the issue context, the repo-facts block, the
  claim comment, the repro report and its parts). In live mode (where
  on GitHub or in the draft: the issue thread, the repo's docs, the
  student's draft comment).
- What good looks like: one or two sentences someone else could apply.
  Prefer observable conditions ("the versions named match what the
  issue targets, or the difference is called out") over adjectives
  ("environment is thorough").

A rubric check whose evidence this guide cannot locate is a check
nobody else can execute; the rubric swap showed you what that feels
like. Write the map you wish your grader had.
-->

## Environment

<!-- Where the environment record lives, and what a sufficient one
looks like against the issue's stated target. -->

In eval bundles, read the repro report's environment section and compare it
with the issue context and repo-facts block. In live mode, read the student's
environment block and values shown in the draft comments or artifacts. Look
for the OS/platform, relevant tool or project version, and issue-specific
details such as shell, driver, runtime, dependency, feature flag, or
configuration. A mismatch is acceptable when the report names it and limits
the conclusion accordingly.

## Steps

<!-- Where the reproduction steps live, and what makes them followable
by a stranger, starting state to trigger. -->

In eval bundles, use the repro report's setup, commands, inputs, and trigger
sequence. In live mode, use the repro draft itself, not unstated files in the
student's workspace. Good steps identify the starting state, create or show
every required fixture, run the issue's exact trigger, and include a control
when it helps distinguish the behavior. A stranger must not need private
repositories, omitted configuration, or guessed commands.

## Behavior shown

<!-- Where the artifacts live (output excerpts, logs, screenshots),
and what it means for an artifact to show the issue's behavior rather
than an adjacent one. -->

In eval bundles, read the report's output excerpts, logs, screenshots, and
control artifacts alongside the issue body and thread highlights. In live
mode, read the artifacts quoted or linked by the repro draft. The decisive
artifact contains the issue's distinguishing symptom, error, exit status,
ordering, measurement, or visual state. A version banner, successful startup,
generic error, or altered input is not evidence unless the report explains why
it is the issue's expected symptom.

## Honesty

<!-- Where claims and their backing meet: how to tell a report that
says exactly what happened (including an honest cannot-reproduce) from
one that claims more than its evidence shows. -->

Compare the report's expected/actual section and conclusion with its artifacts,
the issue's target behavior, and any environment or version delta. "Reproduced"
requires the shown behavior to match; "cannot reproduce" is valid when the
report shows a real attempt and says what differed or remains unknown. Treat
root-cause guesses as hypotheses unless an artifact supports them, and reject
certainty about a crash, fix, or generality that the run does not establish.

## Comms

<!-- Where the words meet the repo: the claim comment against the
issue, the comments against the repo's stated templates and
contribution policy (including AI-use disclosure requirements), and
what specific-and-honest looks like next to boilerplate. -->

In eval bundles, read the claim comment and repro report against the repo-facts
block's bug-report template, contribution policy, and AI-use policy. In live
mode, read the drafts and the corresponding repository documents or issue
template. A usable claim names issue-specific work without promising a
guaranteed fix or deadline. A usable repro comment states what was tried, what
artifact resulted, and what conclusion follows. Include every disclosure the
repository requires; silence is not a disclosure requirement.
