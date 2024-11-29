import os
import sys


def main() -> None:
    os.execv(sys.executable, [sys.executable] + sys.argv[1:])
