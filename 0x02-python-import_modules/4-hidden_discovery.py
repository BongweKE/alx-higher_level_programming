#!/usr/bin/python3
import hidden_4


def main():
    hidden_list = [m for m in dir(hidden_4) if m[:2] != "__"]
    for fun in hidden_list:
        print(fun)


if __name__ == "__main__":
    main()
