#!/usr/bin/python3
from sys import argv

def main():
    count = len(argv) - 1
    if count <= 0:
        print("0 arguments.")
    else:
        print(f"{count} argument{'s' if count > 1 else ''}:")
        for arg in argv:
            if argv.index(arg) == 0:
                continue
            print(f"{argv.index(arg)}: {arg}")


if __name__ == "__main__":
    main()
