#!/usr/bin/env python3
# Created By: Brandon Brandhuber
# Date: November 26th, 2025
# Program to show all valid color combos


def main():

    for red in range(0, 256, 1):
        for green in range(0, 256, 1):
            for blue in range(0, 256, 1):
                print(
                    f"\033[1;38;2;{red};{green};{blue}mRGB({red}, {green}, {blue})\033[0m"
                )


if __name__ == "__main__":
    main()
