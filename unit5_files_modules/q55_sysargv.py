"""Q55(a): Demonstrate command-line arguments using sys.argv."""

import sys


def main():
    print("Number of arguments:", len(sys.argv))

    for index, argument in enumerate(sys.argv):
        print(f"Argument {index}: {argument}")


if __name__ == "__main__":
    main()
