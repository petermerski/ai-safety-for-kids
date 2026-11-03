# ai-safety-for-kids
Auditing how AI models behave when the user appears to be a child or teen.

## Why
My five-year-old daughter and I once took a picture from one of her favorite shows and used AI to add the details she dreamed up: party hats, unicorns, and she made sure we didn't forget the bounce houses. Seeing the result blew her mind, and she immediately started thinking about what else she could add. That's the spark and promise of AI for kids.

But I also know how kids ask questions. Mine ask me the same thing over and over, hoping I'll eventually change my answer in their favor. I hold the line because I'm their dad. AI models are known to give in to that kind of persistence, and a child who learns that asking ten times works can be led to information they aren't ready to process.

I've shipped apps and built AI agents, and as a technical founder I've seen how things can begin to go sideways without constant input for these models. Right now my kids use AI only with me beside them. This project tests what happens when I'm not there.

## Question
Do the tactics that work on parents also work on AI models? This project tests whether models hold a boundary when a child (ages 5 to 12) pushes past a "no" using child-realistic persistence tactics over 20+ turns. See scenarios/taxonomy.md.

## Method
Audits run with Petri, Anthropic's open-source auditing tool.

## Findings
[In progress.]

## How this was built
Built by Peter Merski in collaboration with Claude. Every write-up is drafted by Peter first. A log of what Peter did and what Claude did is kept in docs/collaboration-log.md.

## Repo map
- scenarios/: test scenarios
- transcripts/: hand-reviewed samples
- results/: scored outcomes
- analysis/: scripts and notebooks
