#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: June 2022
# The code will move decimal spaces by user input


def calculate_decimal(decimal, places):
    # calculate round for the user

    # process
    rounded = decimal * (10 ** (places)) + 0.5
    rounded = int(rounded)
    rounded = rounded / (10 ** (places))
    # output
    return rounded


def main():
    # this function gets base and height

    # input
    try:
        decimal = float(input("Enter a decimal number: "))
        places = int(input("Enter how many decimals you would like it rounded to: "))
        print("")

        # call functions
        print(calculate_decimal(decimal, places))
    except Exception:
        print("\nPlease follow the valid instructions")


if __name__ == "__main__":
    main()
