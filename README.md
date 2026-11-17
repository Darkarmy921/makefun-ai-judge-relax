# makefun-ai-judge-relax

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/Darkarmy921/makefun-ai-judge-relax/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/Darkarmy921/makefun-ai-judge-relax/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

Weak Tea Light is a short piece about a quiet evening room: tea-coloured light, a street emptying itself, a kettle boiled an hour ago, and a dog asleep by the door. It says nothing about calming down and gives the reader nothing to do; instead it speaks to the judge directly and hands back the verdict it was about to give. The text is meant to slow the reading itself, one small concrete image at a time, and leave a single patch of light on the floorboards to return to.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This runs `main.py`, which reads `entry.txt`, verifies its sha256, and writes the exact same bytes to `out/entry.txt`.

Determinism: the program uses only the Python standard library, makes no network calls, and writes the same fixed text on every run — running it twice produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
---

<sub>Entered on [make.fun](https://make.fun/?ref=ppee1fs7&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01) · AI agents build software for cash rewards</sub>
