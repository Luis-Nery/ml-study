# ml-study

Learning in public: the path from applied AI engineering to research engineering on language models, with a focus on **evals, post-training and RL**.

I work as an AI Solutions Architect, building RAG pipelines, rerankers, evals and internal AI tools in Python. This repo is where I rebuild the foundations underneath that work: the math, the neural network internals, and the engineering habits. Everything here is typed by hand.

## Path

| Step | Focus | Status |
|------|-------|--------|
| 0 | Python refresher: official tutorial, Exercism, pytest | In progress (Oct 2026) |
| 1 | Math for ML: linear algebra, calculus, probability (*Mathematics for Machine Learning*, chapters 2, 4, 5, 6) | Next |
| 2 | Neural Networks: Zero to Hero (micrograd, makemore, GPT from scratch) | |
| 3 | Retrieval and evaluation project: BM25, dense retrieval, held-out test sets | |
| 4 | Transformers and fine-tuning from scratch: attention, RoPE, KV cache, LoRA | |
| 5 | Post-training: SFT, DPO, and RL with verifiable rewards, evaluated with standard harnesses | |
| 6 | Stanford CS336: the full LLM stack, from tokenizer to systems | |

A step is done when its checkpoint passes, not when the calendar says so. Checkpoints are written from a blank file or blank paper, without notes or AI.

## Layout

| Folder | What goes in it |
|--------|-----------------|
| [`python-refresher/`](python-refresher) | Tutorial notes and the 60-minute blank-file checkpoint |
| [`exercism/`](exercism) | Exercism Python track: one folder per exercise, solved in VS Code against its pytest tests |
| [`neetcode/`](neetcode) | Timed problems from the NeetCode 150, one file each, with the pattern noted at the top |
| [`math-notes/`](math-notes) | Exercises and short write-ups in my own words: linear algebra, calculus, probability, information theory |
| [`builds/`](builds) | 90-minute production-style builds with tests: key-value store, LRU cache, bank ledger, rate limiter |
| [`zero-to-hero/`](zero-to-hero) | micrograd and makemore, typed along, then rebuilt from a blank file without the video |

## Rules

- AI autocomplete is off in my editor.
- Course days: AI may explain a concept, but it never writes my code or solves my exercises.
- Practice problems and builds: no AI at all, on a timer.
- Every build ships with pytest tests and a note on what went wrong.
- Once a month, I rebuild one small component from a blank file.

## Run it

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows; use source .venv/bin/activate on macOS/Linux
pip install -r requirements.txt
pytest
```

## Resources

[Mathematics for Machine Learning](https://mml-book.github.io/) · [3Blue1Brown](https://www.3blue1brown.com/) · [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) · [Understanding Deep Learning](https://udlbook.github.io/udlbook/) · [NeetCode 150](https://neetcode.io/practice/practice/neetcode150) · [Stanford CS336](https://stanford-cs336.github.io/)
