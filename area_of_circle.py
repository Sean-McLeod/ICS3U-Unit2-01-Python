#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This program can calculate the area and perimeter of a circle with
# a radius of 15mm

import math


def main():
    # This function calculates the area and perimeter of a circle

    print("If a circle has a radius of 15mm:")
    print("")
    print("Area is {}mm²".format(math.pi*15**2))
    print("Perimeter is {}mm".format(2*math.pi*15))


if __name__ == "__main__":
    main()
