# Simple Calculator Demo

## CI Status

[![CI (branches)](https://github.com/aviduya/SimpleCalculator/actions/workflows/ci-branches.yml/badge.svg)](https://github.com/aviduya/SimpleCalculator/actions/workflows/ci-branches.yml)
[![CI (daily on main)](https://github.com/aviduya/SimpleCalculator/actions/workflows/ci-daily.yml/badge.svg?branch=main)](https://github.com/aviduya/SimpleCalculator/actions/workflows/ci-daily.yml)

This project shows how to:

- Write a tiny **C++ library** (`src/lib.cpp`) with a bug.
- Test it using **assert** in a small `main` program (`tests/test_main.cpp`).
- Orchestrate builds/tests with a single **Python script** (`tools/ci.py`).
- Run everything in **GitHub Actions** on Linux (both on pushes/PRs and on a daily schedule).

## How it works

1. **Test**:
   `tests/test_main.cpp` runs a couple of `assert()` calls.
   A failure aborts with non-zero exit → CI job fails.

2. **Python entry point**:
   `tools/ci.py` compiles the C++ code and runs the test executable.
   - Debug build (asserts ON)
   - Release build (asserts OFF with `-DNDEBUG`)

3. **GitHub Actions**:
   - `ci-branches.yml` runs on pushes / PRs.
   - `ci-daily.yml` runs once a day on the `main` branch.

## Local usage

```bash
# build & run debug test
python tools/ci.py
