#!/usr/bin/python3
import sys


def print_arguments():
    args = sys.argv[1:]
    num_args = len(args)

    print("Number of argument(s):", num_args, end="")
    if num_args == 0:
        print(".")
    else:
        print("\nArguments:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
        print_arguments()
