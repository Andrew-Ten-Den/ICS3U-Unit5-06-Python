#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: June 2022
# The code will move decimal spaces by user input


def calculate_decimal(decimal, places):
    # calculate round for the user

    # process
    decimal[0] = decimal[0] * (10 ** (places)) + 0.5
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0] / (10 ** (places))



def main():
    # this function gets base and height
    lists = []
    # input
    try:
        decimal = float(input("Enter a decimal number: "))
        places = int(input("Enter how many decimals you would like it rounded to: "))
        lists.append(decimal)
        
        print("")

        # call functions
        calculate_decimal(lists, places)
        print(lists[0])
    except Exception:
        print("\nPlease follow the valid instructions")


if __name__ == "__main__":
    main()
