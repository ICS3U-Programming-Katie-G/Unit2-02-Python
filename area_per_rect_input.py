#!/usr/bin/env python3

# Created By: Katie
# Date: September 23rd, 2022
# This program calculates the area and perimeter of a rectangle, with user input.
import math


def main():
    # this function gets the user input for the length and width of a rectangle, then calculates the area and perimeter of the rectangle with those values. It then displays it back to the user.
    print("This program will calculate the area and perimeter")
    print("of a rectangle with your inputted values!")
    print("")

    # getting the length
    length = float(input("Please input the length of the rectangle in cm: "))

    # getting the width
    width = float(input("Please input the width of the rectangle in cm: "))

    # calculation of area and perimeter
    area = length * width
    perimeter = 2 * (length + width)

    # output of area and perimeter back to the user
    print("")
    print("For a rectangle with your chosen dimensions: ")
    print("The area is: {} cm^2".format(area))
    print("The perimeter is: {} cm".format(perimeter))


if __name__ == "__main__":
    main()
