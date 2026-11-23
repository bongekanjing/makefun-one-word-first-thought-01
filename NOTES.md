# One Word, First Thought — notes

## Chosen word

**murmuration** — 11 characters, letters only, one word.

## Candidates considered (first pass)

| Word | Length | Verdict |
|---|---|---|
| petrichor | 9 | Vivid (smell of rain on dry earth) and specific, but a staple of "interesting word" lists — many entrants will pick it, and byte-identical entries share one rate with the earlier receipt winning. No wit or double meaning. |
| serendipity | 11 | Pleasant but overused; feels generic and expected, low surprise. |
| murmuration | 11 | **Winner.** A flock of starlings swirling as one shape in the sky — a clear, moving picture in a single word. Surprising, specific, and the sound itself murmurs. |
| apricity | 8 | Vivid (warmth of the sun in winter) and uncommon, but a quieter, softer image; less striking head-to-head than a sky full of birds. |
| psithurism | 10 | The sound of wind in trees — evocative, but so obscure it risks reading as invented, and its image is vaguer than murmuration's. |
| gloaming | 8 | Beautiful twilight word, but common in poetry and less surprising. |

Why murmuration wins: it scores on every judge criterion at once — surprise (not a word most people reach for first), vividness (an unmistakable moving image), and wit/sound (murmur is inside it, and the word itself sounds like what it names). The others each give up one criterion: petrichor and serendipity give up surprise, apricity and gloaming give up punch, psithurism gives up clarity.

## Test result (first pass)

`python3 main.py` in a clean run wrote `/output/entry.txt` containing exactly `murmuration` (11 bytes, no trailing newline). Verified with `cat` / `wc -c`.

## Revision pass

Reconsidered against the winner: **susurrus** (8, a whispering/rustling sound — lovely sound, but a thinner image than a starling flock and more likely to read as obscure Latin), **limerence** (9, obsessive infatuation — specific feeling, but abstract, no picture, and a clinical ring), **effervescence** (13, fizzing energy — vivid and fun, but a familiar dictionary-showpiece word, less surprising), **quockerwodger** (13, a fake-enthusiast politician — witty, but so obscure it risks reading as made-up, which the brief warns against). None beats murmuration: susurrus and limerence lose on vividness, effervescence loses on surprise, quockerwodger loses on credibility as a real, recognisable word. Winner kept.

Strengthened `main.py` validation in the revision: added asserts that the word is all lowercase, contains no digits or punctuation (via `isalpha` plus an explicit punctuation/digit check), and that the written file contains exactly the word with no trailing newline (read-back check).

## Test result (after revision)

Re-ran `python3 main.py`; `/output/entry.txt` contains exactly `murmuration`, 11 bytes, no trailing newline. PASS.
