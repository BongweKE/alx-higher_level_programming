#!/usr/bin/python3
from sys import argv


def main():
    result = 0
    for arg in argv:
        if argv.index(arg) == 0:
            continue
        result += int(arg)
    print(result)


if __name__ == "__main__":
    main()
