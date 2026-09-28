# Procedure: how this skill grades a plan package

<!--
THIS IS THE PART YOU WRITE, and it is a new kind of part. Weeks 1 and
2, SKILL.md carried a numbered workflow and you only wrote judgment
files. This week the workflow is gone from the frame: SKILL.md says
"execute procedure.md", and these are the operating steps you author.
The machinery is in your hands now.

Your operator swap is the design brief. When your executor stalled
because your rubric said WHAT to decide but not HOW to find the
evidence, that was a procedure gap. This file is where those gaps get
closed: a complete procedure lets someone who has never seen a plan
package before (a groupmate, or the skill itself) grade one exactly the
way you would.

Under each stage heading below, write the concrete steps for that
stage. The one-line note under each heading says what a complete
procedure must decide there. Write steps, not intentions: "read the
repro evidence before the plan, and note what behavior it pins down"
is a step; "understand the context" is a wish.
-->

## Read order

<!-- What gets read, in what order, before any check is graded, and
what to note down from each part while reading. A complete procedure
decides the order (issue first? repro evidence first?) and says why
the order matters for the checks that come later. -->

1. Read the issue context and thread highlights first. Record the requested
	behavior, explicit constraints, maintainer directions, prior-art PRs, and
	repository conventions named in the package.
2. Read the entire repro-evidence block next. Record the environment, exact
	trigger, control run, artifact, observed outcome, and limitations. This
	establishes what the plan must explain and what its tests must repeat.
3. Read the candidate plan from scope and diagnosis through implementation,
	tests, risks, and deviations. Then read the candidate plan comment. Do not
	infer missing content from files outside the package.

## Evidence gathering

<!-- For each evidence family your rubric's checks name, the concrete
gathering move: which part of the package (or, live, which page or
thread location per your evidence guide) to pull the fact from, and
what to record. A complete procedure leaves no check whose evidence an
executor would have to hunt for. -->

1. For diagnosis, compare the stated cause with the repro trigger, control,
	and artifact. Record one supporting observation or one contradiction.
2. For scope, compare every named file, subsystem, migration, redesign, and
	follow-up with the issue request. Record the core change and deferred work.
3. For executability, extract the first implementation step, each named file or
	symbol, the order of data-flow changes, and any unresolved architecture
	choice. Record whether a stranger can begin without asking the author.
4. For tests, pair each proposed test with the repro trigger or control. Record
	the fixture or command, observable assertion, and expected result.
5. For honesty, list facts, hypotheses, risks, and deviations separately.
	Record any promise that exceeds the evidence or unknown with no decision
	point.
6. For conventions, compare the comment with thread directions, prior-art
	work, contribution templates, branch rules, and AI disclosure policy.

## Check execution

<!-- How one check runs against gathered evidence: in what order the
checks execute, what an executor does when evidence for a check is
genuinely absent, and when a check may be graded without re-reading
the whole package. A complete procedure makes two executors grade the
same package the same way. -->

Execute checks in this order: diagnosis, scope, executability, test plan,
honesty, then thread/conventions. For each check, use only the evidence
recorded in the corresponding gathering step and quote the deciding fact in
one line. Grade `pass` when its condition is met, `fail` when evidence
contradicts it or an explicit element is missing, and `unclear` only when the
package genuinely lacks the evidence needed to decide. Do not treat headings,
length, or polished prose as evidence.

## Verdict assembly

<!-- How the per-check grades become the final accept or reject:
apply your rubric's verdict rule, state how unclear grades enter it,
and say what gets quoted in the output for the deciding check. A
complete procedure produces the same verdict from the same grades,
every time. -->

1. Preserve one output entry for every rubric check, in execution order, with
	its grade and one evidence sentence naming the deciding observation.
2. Apply the rubric rule after all checks: accept only if every required check
	is `pass`; otherwise reject. Treat every `unclear` as a required failure.
3. In the readable summary, identify the first or most consequential failed
	check and quote its deciding evidence. End with exactly one fenced JSON
	object containing the item, all check entries, and the binary verdict.
