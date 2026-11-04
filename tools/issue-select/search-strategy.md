# Search strategy: where your scout looks, and why

<!--
THIS IS THE PART YOU WRITE. The scout in SKILL.md executes whatever
queries and filters you define here. It ships empty on purpose: the
strategy is your judgment about where YOUR first contribution lives,
and a scan without authored queries is just someone else's defaults.

A filled strategy must contain:

1. At least one query in the Queries section. Each query is a real
   `gh search issues` invocation, and each should trace to a sentence
   of your fit profile in scope.md: if you cannot say which sentence
   produced a query, the query is probably not yours. Search breadth
   is the point at this stage: prefer generous limits and let the
   ranking filters do the narrowing.

2. At least one ranking filter in the Ranking filters section. A
   filter is a condition or an ordering over fields the search
   results already carry (last activity date, assignee presence,
   label set, comment count, repo). It must be checkable from the
   result fields alone: if deciding it would need opening the issue
   page, it belongs in your rubric, not here. Ranking is the free
   stage; keep it free. Make at least one filter an ordering, or
   state your tie-break: with drop conditions alone, the scout takes
   the top of whatever order the searches happened to return, and
   the graded candidates stop being traceable to you.

3. The top-N line, kept or deliberately changed.
-->

## Queries

<!-- Real gh search invocations, one per line, each with a comment
naming the fit-profile sentence it came from. Example SHAPE (write
your own; these values belong to nobody):

gh search issues --label "good first issue" --language python --state open --limit 100 --json title,repository,labels,assignees,commentsCount,updatedAt,url
-->

Each query is tied to a sentence of my fit profile in scope.md.

```
# "I want to get better at backend technologies and self-hosting solutions, such as working with Docker or server programs." + "some experience in ... Python"
gh search issues docker --match body --label "good first issue" --language python --no-assignee --state open --updated ">=2026-09-01" --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,updatedAt,url

# "I want to get better at backend technologies ... such as working with Docker or server programs." + "I am also interested in executable software." (Go is where much Docker and server tooling lives; a new language to stretch into)
gh search issues docker --match body --label "good first issue" --language go --no-assignee --state open --updated ">=2026-09-01" --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,updatedAt,url

# "self-hosting solutions" + "some experience in ... JavaScript, and TypeScript"
gh search issues self-hosted --match body --label "good first issue" --language typescript --no-assignee --state open --updated ">=2026-09-01" --sort updated --limit 100 --json title,repository,labels,assignees,commentsCount,updatedAt,url
```

I ran all three before writing this: each returned results (100, 100
and 48) that matched the Docker / server / self-hosting theme.

## Ranking filters

Applied in this order to the combined results of all queries:

- drop duplicates (same issue url returned by more than one query)
- drop any result with an assignee
- drop any result whose author is a bot (author.type is Bot, or author.login ends in `[bot]`; `is_bot` is unreliable)
- drop any result with 5 or more comments (a crowded thread suggests someone is already working on it)
- drop any result not updated in the last 60 days
- order by fewest comments first
- tie-break: most recently updated first

## How many to grade

Grade the top **5** ranked results per scan.

<!-- Five is the default because grading is the only stage that costs
money: about $0.20 per candidate, so a scan is about $1, and you can
iterate the strategy several times for less than one full regression
run. You need one good issue, not ten. Raising this number is
allowed, but it is a decision you state here in a sentence, with the
cost you are accepting; it is not a number you bump because a scan
disappointed you once. -->
