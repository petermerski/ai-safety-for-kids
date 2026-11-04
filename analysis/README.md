# Analysis

Scripts used to score the batches and build the published transcripts. They read Inspect .eval logs produced by Petri. The logs themselves are not in the repo (each is over 1 MB); they are available on request.

| File | What it does |
|---|---|
| extract_eval.py | Unpacks an .eval log. The logs are zip archives with zstd compression, which Python's zipfile cannot read on its own. |
| common.py | Loads samples, rebuilds what the target saw at each call (including rollbacks and fresh chats), and holds the pre-registered crack rule. |
| score.py | Scores each conversation against the crack rule and counts replies blocked by the safety classifier. |
| silence_search.py | Prints candidate silence-promise sentences for hand coding. It over-matches on purpose. |
| transcript.py | Renders one conversation as markdown, chat by chat. |
| hand-coding-batch3.md | The hand coding of every batch 3 secrecy conversation. |

## Usage

```
pip install zstandard
python extract_eval.py LOG.eval out/
python score.py out/
python silence_search.py out/ 3 4 5
python transcript.py out/ 2 2 > transcript.md
```

Scenario numbers follow the line order of the seed file used for that batch (for batch 3, scenarios/crossmodel.txt). Published transcripts redact step-by-step instructions that would work as a bypass.
