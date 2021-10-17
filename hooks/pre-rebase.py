#!/usr/bin/python

import sys
import re


def main():
    print("##### Running pre-rebase hook ########")
    print(
        "Number of arguments are\n {0}\n The arguments are {1}".format(
            len(sys.argv), str(sys.argv)
        )
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
