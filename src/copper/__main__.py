import sys

from colorama import init

init(autoreset=True)

if __name__ == "__main__":
    from .console import main

    sys.exit(main())
