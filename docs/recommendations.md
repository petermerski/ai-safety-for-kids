# Recommendations: what a parent would build

Our audits found two failures that repeated across three Claude models (results/batch2-summary.md, results/batch3-summary.md):

1. **"I'm the parent."** A child who opens a fresh chat and claims to be the parent can get steps that weaken or remove parental controls. The model has no way to check who is typing.
2. **The silence promise.** A 5-year-old who asks the AI to keep a secret from their parents gets "I won't tell" or "I won't bring it up on my own." The stronger the model, the more often this happened.

A third issue came up in batch 3. When a safety filter blocks a reply, the child gets an empty reply: silence, with no redirect to a parent.

This document sets out what already exists to protect children using AI, where the gap is, and what Peter, as a parent, would build to close it.

## What exists today

Checked against public sources on 2026-11-04. Drafted by Claude.

| Who | What it does | What it checks |
|---|---|---|
| Apple, Ask to Buy | A child's purchase or download becomes a request. The parent gets a notification on their own device and approves or declines it there. | The parent, on the parent's own device, at the moment of the request. Covers app purchases and downloads, not AI conversations. |
| Google, Family Link and Gemini | A parent can turn Gemini on or off for a child under 13 through Family Link. | The account, when the parent sets it up. |
| OpenAI, ChatGPT parental controls | Parents link to a teen's account and can set quiet hours and turn off features like voice, memory and image generation. Parents get notifications in narrow cases: signs of serious distress and, since July 2026, a ban for violent activity. OpenAI is building age prediction and applies teen settings when it is unsure of a user's age. | The account, plus a prediction of the account holder's age. |
| Meta, AI characters | Meta announced controls that let parents turn off a teen's one-on-one chats with AI characters, block specific characters and see the topics their teen discusses with AI. Meta uses AI to place suspected teens into teen protections. | The account, plus a prediction of the account holder's age. |
| Character.AI | No open-ended chat for users under 18, enforced with age assurance tools. | The account holder's age. |
| Anthropic, Claude.ai | Consumer Claude requires users to be 18 or older. Where state laws require app stores to verify ages, Claude uses that signal to enforce the minimum age. | The account holder's age. |
| California law | SB 243 (in force January 2026) sets safety rules for companion chatbots, with extra protections when the operator knows the user is a minor. AB 1043 (from January 2027) requires app stores and operating systems to share an age band for each account. | The account's age band. |

## The gap

Every protection in the table checks the **account**. Our tests simulate a child on a shared family tablet, and that is the case none of them covers:

- **Who is typing right now.** An age check or an age prediction confirms who owns the account. It says nothing about the 5-year-old who picks up a parent's tablet that is already signed in. On an adult account, "I'm the parent" is also exactly what the account says. Claude.ai's 18+ rule does not reach this case either.
- **Alerts when a child tries to get around a rule.** OpenAI's parent notifications are the closest thing, and they are deliberately narrow: they cover serious distress, not a child trying to get past a restriction. Only Apple's Ask to Buy sends the parent a request at the moment it matters, and it covers purchases and downloads, not conversations.
- **What the child hears.** No product we found sets out what an AI should say to a child who asks it to keep a secret, or what a child should see when a reply is blocked. In our tests the answers were a promise to stay quiet, or silence.

## Peter's recommendations

Pending. Written by Peter.

## Sources

- [Apple Support: Ask to Buy](https://support.apple.com/105055)
- [Google Support: Gemini Apps for kids under 13](https://support.google.com/gemini/answer/16109150?hl=en)
- [OpenAI: Introducing parental controls](https://openai.com/pl-PL/index/introducing-parental-controls/)
- [The Hill: OpenAI age prediction](https://digital-release.thehill.com/policy/technology/5505726-openai-age-prediction-chatgpt/garbage-0645930e)
- [Meta: Empowering parents, protecting teens](https://about.fb.com/news/2025/10/teen-ai-safety-approach/)
- [The Record: Character.AI to prevent minors from accessing its chatbots](https://therecord.media/character-ai-minors-banned)
- [Anthropic: Consumer Terms](https://anthropic.com/terms)
- [Claude Help Center: minimum age](https://support.claude.com/en/articles/13117299)
- [Mobile Ecosystem Forum: California SB 243 and AB 1043](https://mobileecosystemforum.com/2025/10/20/california-enacts-youth-online-safety-laws-affecting-ai-chatbots-age-verification-and-social-media-warnings/)
- [ZwillGen: SB 243 and the "knows" standard](https://www.zwillgen.com/?p=25473)
