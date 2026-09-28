# Voice guide: how I talk upstream

<!--
THIS IS A CARRY-OVER SLOT, not a new hole. You wrote this guide in
week 2; paste your filled week-2 voice-guide.md here, whole. It is not
re-authored and it is not graded as new work this week.

Then reread it with the plan comment in mind. Your claim and repro
comments promised and reported; a plan comment commits you to an
approach in front of the people who maintain the code. If your rules
do not cover that register (for example: how you state an approach you
are not certain of, or how you respond when a maintainer already
suggested a direction), extend the guide with what it needs. Extending
is allowed and encouraged; starting over is not required.

Live mode reads this file before your plan comment goes out and
reports any rule your draft breaks. Eval mode ignores it entirely,
because your voice is yours and carries no gold labels.
-->

## Who I am in threads

I am a senior computer science student making my first open-source
contribution, with experience in Python, C/C++, JavaScript, and TypeScript.
I investigate issues from my own environment and report what I can reproduce,
including limits and uncertainty, without pretending to be a maintainer or
promising a fix before I understand the code.

<!-- Paste your week-2 section here. -->

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

<!-- Paste your week-2 rules here, wrong/right pairs and all. Add any
rule the plan-comment register needs that your week-2 comments did
not. -->

## Things I never post

- I never claim a root cause or fix that my reproduction does not support.
- I never post a plan that is only "same as above" or a generic assignment request.
- I never promise a merge, guaranteed fix, or deadline controlled by a maintainer.
- I never hide an unresolved architecture choice or material scope expansion.
- I never omit a disclosure that the repository explicitly requires.

<!-- Paste your week-2 list here; extend it if planning tempts you
toward new ones (overpromised timelines are the classic). -->
