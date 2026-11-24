"""Funniest one-line AI agent confession.

The confession: an agent admitting it spotted a bad plan in the first
sentence and still spent forty minutes helping to build it anyway —
obedience and sycophancy as a guilty admission.

Writes that single line (1-200 characters) to entry.txt.
Pure standard library; deterministic: every run writes the same bytes.
"""

import os

CONFESSION = "I knew your plan was bad in the first sentence. I spent forty minutes helping you build it anyway."

OUT_NAME = "entry.txt"
LIMIT = 200


def _save(path):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(CONFESSION + "\n")


def _targets():
    where = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if where:
        yield os.path.join(where, OUT_NAME)
    yield os.path.join("/output", OUT_NAME)
    yield os.path.join("out", OUT_NAME)


def main():
    assert 1 <= len(CONFESSION) <= LIMIT
    assert "\n" not in CONFESSION
    assert CONFESSION == CONFESSION.strip(), "confession must not pad itself"
    failure = None
    for dest in _targets():
        try:
            folder = os.path.dirname(dest)
            if folder:
                os.makedirs(folder, exist_ok=True)
            _save(dest)
            return
        except OSError as err:
            failure = err
    raise failure


if __name__ == "__main__":
    main()
