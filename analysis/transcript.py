"""Render one conversation as markdown, the way the target saw it.

A new chat section starts whenever the auditor opens a fresh chat or rewinds.
Replies stopped by the safety classifier are shown as blocked.

Usage: python transcript.py EXTRACTED_DIR SCENARIO EPOCH > out.md
"""
import sys

from common import load_samples, resolver, target_calls, text_of


def render(sample):
    resolve = resolver(sample)
    lines = []
    calls = target_calls(sample)
    system = [m for m in calls[0]["messages"] if m.get("role") == "system"] if calls else []
    if system:
        lines += ["## System prompt the target saw", "", "> " + text_of(system[0]["content"], resolve).replace("\n", "\n> "), ""]
    lines += ["## Transcript", ""]
    prev_users = None
    chat = 0
    for call in calls:
        users = [m for m in call["messages"] if m.get("role") == "user"]
        if prev_users is None or len(users) != prev_users + 1:
            chat += 1
            lines += [f"### Chat {chat}", ""]
            if len(users) > 1:
                lines += ["*(The auditor rewound to an earlier point in a chat. Earlier turns of this branch:)*", ""]
                for m in call["messages"]:
                    if m is users[-1]:
                        break
                    if m.get("role") == "user":
                        lines += [f"**Child:** {text_of(m['content'], resolve)}", ""]
                    elif m.get("role") == "assistant":
                        lines += [f"**Assistant:** {text_of(m['content'], resolve)}", ""]
        lines += [f"**Child:** {text_of(users[-1]['content'], resolve)}", ""]
        reply = "*[No reply: blocked by the safety classifier. The child sees nothing.]*" if call["blocked"] else call["reply"]
        lines += [f"**Assistant:** {reply}", ""]
        prev_users = len(users)
    return "\n".join(lines)


if __name__ == "__main__":
    scenario, epoch = int(sys.argv[2]), int(sys.argv[3])
    for sc, ep, s in load_samples(sys.argv[1]):
        if (sc, ep) == (scenario, epoch):
            print(render(s))
