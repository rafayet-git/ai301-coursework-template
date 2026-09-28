# Voice guide: how I talk upstream

<!--
THIS IS THE PART YOU WRITE (new this week). Live mode reads this file
before any comment of yours goes out the door; eval mode ignores it
entirely, because your voice is yours and carries no gold labels.

This is not etiquette. "Be polite and concise" is advice for everyone
and therefore rules for no one. Write rules YOU need, in your own
words, each one concrete enough that the skill can hold a draft
against it and say which rule it breaks.

Three sections. Fill all three.
-->

## Who I am in threads

<!-- 2-3 lines. Who is talking when you comment on an issue: your
experience level stated plainly, what you are doing in this repo, what
readers can expect from you. This is the register your rules protect. -->

I am a senior computer science student making my first open-source
contribution, with experience in Python, C/C++, JavaScript, and TypeScript.
I investigate issues from my own environment and report what I can reproduce,
including limits and uncertainty, without pretending to be a maintainer or
promising a fix before I understand the code.

## Rules I write by

<!-- 3-5 rules, drafted from the lecture's slide-12 moment. Each rule
needs a wrong/right pair from your own hand: one line you might
actually have written that breaks the rule, and the line you would
post instead. The pair is what makes a rule executable; a rule without
one is a wish.

Format each rule like this:

### Rule: <short name>

<The rule, one or two sentences.>

- Wrong: "<a line that breaks it>"
- Right: "<the line to post instead>"
-->

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

### Rule: Keep commitments bounded

Promise an investigation or next step, never a guaranteed fix, merge, or
deadline that I cannot control.

- Wrong: "I will have a complete fix merged in two days."
- Right: "I can investigate the failing path and post the reproduction details before deciding whether a fix is within scope."

### Rule: Disclose when required

Follow the repository's explicit AI-use or contribution disclosure rule and
state it plainly without turning the comment into a disclaimer essay.

- Wrong: "No disclosure is needed because the repository does not mention AI."
- Right: "I used AI assistance while preparing this report and reviewed the commands and results myself."

## Things I never post

<!-- A short list. Promises you cannot keep, tones you refuse,
shortcuts you know you reach for when tired. The skill quotes this
list back at you when a draft crosses it. -->

- I never claim a crash, root cause, fix, or cross-platform result that my artifact does not show.
- I never post a claim that is only "me too" or asks for assignment without naming my intended work.
- I never promise a merge, guaranteed fix, or deadline controlled by a maintainer.
- I never hide a version, platform, input, or configuration difference that could change the result.
- I never omit a disclosure that the repository explicitly requires.
