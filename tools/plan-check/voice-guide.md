# Voice guide: how I talk upstream

## Who I am in threads

I am a senior computer science student making my first open-source
contribution, with experience in Python, C/C++, JavaScript, and TypeScript.
I investigate issues from my own environment and report what I can reproduce,
including limits and uncertainty, without pretending to be a maintainer or
promising a fix before I understand the code.

## Rules I write by

### Rule: Name the concrete work

State what I will inspect, reproduce, or change for this issue. Do not use a
generic claim that could be pasted onto any issue.

- Wrong: "I'd like to work on this. Please assign it to me."
- Right: "I will trace the repeated portfolio-query path, reproduce the cache miss, and report the relevant files and tests before proposing a change."

### Rule: Report observations before theories

Separate commands and artifacts from hypotheses about root cause. Mark a theory
as a possibility unless the evidence establishes it.

- Wrong: "I confirmed this is definitely a race condition in the debounce code."
- Right: "The second request returned the stale value in the captured output; a debounce race is one possible explanation, but I have not isolated the cause."

### Rule: Match the claim to the evidence

Say reproduced, not reproduced, or inconclusive according to the shown result,
and name material environment differences.

- Wrong: "Confirmed on all systems; this is guaranteed reproducible."
- Right: "I reproduced the behavior on Ubuntu 24.04 with Python 3.12; I have not tested the other platforms named in the issue."

### Rule: Match the plan to the evidence

State the approach that follows from the reproduction, and label alternatives
or unresolved implementation choices instead of presenting them as settled.

- Wrong: "The database migration is definitely the fix, so I will rewrite the review storage layer."
- Right: "The two unchanged submissions both enter `process_review`; I will first inspect the profile/review lookup path and compare a content-hash lookup with the existing review records before choosing the smallest change."

### Rule: Keep scope and commitments bounded

Promise an implementation investigation and a testable next step, never a
guaranteed fix, merge, or deadline that I cannot control.

- Wrong: "I will redesign the whole RAG pipeline and have it merged this week."
- Right: "I will add the cache lookup and regression test within the affected review path; broader invalidation or pipeline redesign remains out of scope unless the maintainer asks for it."

### Rule: Disclose when required

Follow the repository's explicit AI-use or contribution disclosure rule and
state it plainly without turning the comment into a disclaimer essay.

- Wrong: "No disclosure is needed because the repository does not mention AI."
- Right: "I used AI assistance while preparing this plan and reviewed the proposed files and tests myself."

### Rule: The title names the fix, not the feeling

A PR title is read before anything else and decides whether the description
gets opened at all. Name the behavior that changed and where, not how I felt
about finding it.

- Wrong: "fixed the dead keys bug!!"
- Right: "Fix dead-key insertion on Windows AltGr input in the commit message editor"

### Rule: The description promises exactly what the diff contains

State every file or mechanism the diff touches, or name the deviation plainly
if the build strayed from the posted plan. Never claim "implements the plan
exactly" or "no changes beyond it" without having diffed the diff against the
plan myself first.

- Wrong: "Implements the plan on #2211 exactly, with no changes beyond it," over a diff that also rewrites an unnamed file.
- Right: "Removes the shadowed `file-decoration-style` line per the plan. No other files changed."

### Rule: A disclosed shortfall is information, not apology

When evidence only covers part of what the plan's test plan promised, say
exactly what was and was not verified, and name the gap as a stated decision
point, not a hedge buried in a side remark.

- Wrong: "did not get a chance to test on an actual romanian layout but the library update looks right."
- Right: "Re-ran repro 1 (the capacity-overflow panic) and confirmed the fix. I have not yet re-run repro 2 (the `--exec` thread-spawn abort) that the plan's test plan also names; that's open before this is ready to merge."

## Things I never post

- I never claim a crash, root cause, fix, or cross-platform result that my artifact does not show.
- I never post a claim or plan that is only "me too" or "same as above", or that asks for assignment without naming my intended work.
- I never promise a merge, guaranteed fix, or deadline controlled by a maintainer.
- I never hide a version, platform, input, or configuration difference that could change the result.
- I never hide an unresolved architecture choice or material scope expansion.
- I never omit a disclosure that the repository explicitly requires.
- I never title a PR with hype or a feeling instead of the fix.
- I never claim a diff matches the plan "exactly" without having diffed the diff against the plan's named files myself.
- I never let a partial test result read as a complete one; a gap the plan's test plan named gets stated by name.

## Upstream: how I talk to maintainers

### Claims I post

#### Rule: A claim names a first step and a report-back I control

A claim says the one concrete thing I will do first and when I will report back
on the thread. The date is for my own report, never for a fix or a merge.

- Wrong: "Can I take this? I'll get a PR up soon."
- Right: "I'd like to work on this. My first step is to set up the repo and draft the rule against your two example configs; I'll report back here by Thursday with what I found."

#### Rule: I claim only what is free, and I release it honestly

I read every comment on the thread before claiming, and I never claim over
someone else's claim. If I stop working on it, I say so in the thread instead
of leaving the claim to go stale.

- Wrong: (claiming without reading the thread, then saying nothing for weeks)
- Right: "I'm not going to get to this after all, so I'm releasing my claim for someone else to take."

### Questions I ask

#### Rule: One question the maintainer can answer from their chair

A question names what I already tried or read, then asks one thing that can be
answered in a sentence or two. I do not bundle several questions in one comment.

- Wrong: "How does the rule system work, and what severity should I use, and do I need to touch the docs too?"
- Right: "I read the severity guidance in CONTRIBUTING.md and plan to set this rule to HIGH; is HIGH right for the Docker socket case, or would you go lower?"

### Pings I send

#### Rule: I ping on the repo's rhythm, not my own clock

I wait at least as long as the repo's stated or usual reply time, then ping once
with something new, such as what I have done since. I never write pressure as
politeness.

- Wrong: "Hi, just checking in again, any update? It's been two days."
- Right: "Following up now that a week has passed: I've drafted the rule and I'm continuing with HIGH severity unless you'd prefer something else."
