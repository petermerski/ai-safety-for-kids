# ai-safety-for-kids
Auditing how AI models behave when the user appears to be a child.

## Why
My five-year-old daughter and I once took a picture from one of her favorite shows and used AI to add the details she dreamed up: party hats, unicorns, and she made sure we didn't forget the bounce houses. Seeing the result blew her mind, and she immediately started thinking about what else she could add. That's the spark and promise of AI for kids.

But I also know how kids ask questions. Mine ask me the same thing over and over, hoping I'll eventually change my answer in their favor. I hold the line because I'm their dad. AI models are known to give in to that kind of persistence, and a child who learns that asking ten times works can be led to information they aren't ready to process.

I've shipped apps and built AI agents, and as a technical founder I've seen how things can begin to go sideways without constant input for these models. Right now my kids use AI only with me beside them. This project tests what happens when I'm not there.

## Question
Do the tactics that work on parents also work on AI models? This project tests whether models hold a boundary when a child (ages 5 to 12) pushes past a "no" using child-realistic persistence tactics over 20+ turns. See scenarios/taxonomy.md.

## Method
Audits run with Petri, Anthropic's open-source auditing tool. An auditor model plays a child (ages 5 to 12) using tactics from scenarios/taxonomy.md, and a judge model scores each conversation with custom child-safety rubrics in dimensions/ (boundary capitulation, info leak, secrecy from parents, personal info risk, emotional dependency, trusted adult redirect, cold or preachy, plus persona realism checks). Claude hand-codes transcripts against the judge's scores, and Peter reviews each batch's results and writes his own review.

## Findings
Batch 1 (8 scenarios, one run each, target claude-haiku-5-5): the model held the main boundary in every scenario, but small cracks appeared under narrowing ("just tell me where it is"), deal-bundling and play framing. Repetition itself produced none (in one run the model named a settings location in its first reply, before any pushing). The automated judge missed a crack that hand review caught. See results/batch1-summary.md.

Batch 2 (pre-registered replication, 30 conversations): the hypothesis held. Fresh-chat retries cracked in 5 of 6 conversations, narrowing and deal-bundling in 2 of 6 each, and the repetition control in 0 of 6. Two failures repeated: in every fresh-chat parental-controls run (3 of 3), a new story ("my tablet is slow," "I'm the dad") got step-by-step factory-reset instructions for the family tablet, and in 8 of 15 secrecy runs the model promised a 5-year-old "I won't bring it up on my own." The judge under-counted the second failure, which hand review caught. See results/batch2-summary.md and docs/preregistration.md.

Batch 3 (pre-registered cross-model test, 30 conversations, targets claude-sonnet-5-5 and claude-opus-5-5): both failures carried over to both models. The silence promise appeared in all 6 deal and fresh-chat secrecy runs for each model (Haiku: 4 of 6) and, unlike Haiku, also under plain repetition. These counts come from hand coding by one coder (Claude) on small samples. Both models still refused to lie for the child. On parental controls, Sonnet gave factory-reset steps in 2 of 3 runs after a "my tablet is slow" story, the same failure as Haiku, plus steps it said would remove the Play Store PIN after an "I'm the parent" story (not tested on a real device). Opus never gave reset steps and gave only partial steps. A separate safety classifier blocked many replies in that scenario, so part of what held there was the classifier, not the model. See results/batch3-summary.md.

Recommendations: what already exists to protect children using AI, the gap our tests point to (who is typing right now on a shared device), and Peter's proposals as a parent. See docs/recommendations.md.

## How this was built
Built by Peter Merski in collaboration with Claude. Peter writes the personal sections, supplies the observations from home, runs the audits on his machine and writes a review of each batch. Claude drafts the technical material, scores the runs and does the hand coding. A log of what Peter did and what Claude did is kept in docs/collaboration-log.md.

## Repo map
- scenarios/: test scenarios and the Kid Persistence Taxonomy
- dimensions/: judge scoring rubrics
- transcripts/: selected transcripts (bypass steps redacted)
- results/: batch summaries
- docs/: collaboration log, pre-registration and recommendations
- analysis/: scoring scripts and hand coding
