#!/usr/bin/env python3
import subprocess
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
build = root / "build"
build.mkdir(exist_ok=True)

cmd_build = [
    "clang++", "-std=c++20", "-O0", "-g",
    str(root/"src/lib.cpp"),
    str(root/"tests/test_main.cpp"),
    "-o", str(build/"test_debug"),
]
print("+", " ".join(cmd_build), flush=True)
if subprocess.call(cmd_build) != 0:
    sys.exit(1)


cmd_run = [str(build/"test_debug")]
print("+", " ".join(cmd_run), flush=True)
sys.exit(subprocess.call(cmd_run))
