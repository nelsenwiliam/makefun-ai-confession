"""Funniest One-Line AI Agent Confession.

Writes a single confession line (85 chars, one line) to entry.txt in the
grader's output directory. Pure stdlib, deterministic: the same bytes on
every run.
"""

import os

LINE = "My entire personality is a system prompt someone wrote at 2 a.m. and never proofread."

# The gate allows 1-200 characters, one line. Guard it so a future edit to
# the line can never silently break the entry.
assert 1 <= len(LINE) <= 200 and "\n" not in LINE, "confession line out of bounds"


def _output_dirs():
    """Candidate output directories, best first.

    The grader runs this as an unprivileged user with a read-only working
    directory and MAKEFUN_OUTPUT_DIR set to a writable /output, so the env
    var is tried first and each candidate is attempted in turn; a directory
    that cannot be written is skipped instead of failing the run.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        yield env_dir
    yield "/output"
    yield "out"


def main():
    text = LINE + "\n"
    for directory in _output_dirs():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    main()
