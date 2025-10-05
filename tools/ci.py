#!/usr/bin/env python3
import os, sys, subprocess
from pathlib import Path
from time import perf_counter

root = Path(__file__).resolve().parents[1]
build = root / "build"
build.mkdir(exist_ok=True)

VERBOSE = os.environ.get("CI_VERBOSE") == "1"

def run(cmd: list[str]) -> None:
    if VERBOSE:
        print("+", " ".join(cmd), flush=True)
        r = subprocess.run(cmd)
    else:
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print("✖ Command failed:\n  ", " ".join(cmd))
            if r.stdout:
                print("\n— stdout —\n" + r.stdout)
            if r.stderr:
                print("\n— stderr —\n" + r.stderr, file=sys.stderr)
    if r.returncode != 0:
        sys.exit(r.returncode)

build_start = perf_counter()
run([
    "g++", "-std=c++20", "-O0", "-g",
    str(root / "src/lib.cpp"),
    str(root / "tests/test_main.cpp"),
    "-o", str(build / "test_debug"),
])
build_ms = (perf_counter() - build_start) * 1000

test_start = perf_counter()
run([str(build / "test_debug")])
test_ms = (perf_counter() - test_start) * 1000

print(f"✅ All Tests passed  (build: {build_ms:.0f} ms, run: {test_ms:.0f} ms)")
