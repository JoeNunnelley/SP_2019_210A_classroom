#! /usr/bin/env python3

import sys, getopt

def print_inner(scale, dimension):
    """This function prints the inner row pattern"""
    open_row_start = "|" + ("   " * scale)
    middle_row = (open_row_start * dimension) + "|"

    for i in range(scale):
        print(middle_row)

def print_grid(dimension, scale):
    """This function prints the vertical edge pattern"""
    side = "+" + (" - " * scale)
    vertical_side  = (side * dimension)  + "+"

    for i in range(dimension):
        print(vertical_side)
        print_inner(scale, dimension)

    print(vertical_side)

# Decided to make this a little more fun and work with inputs
def main(argv):
    dimension = ''
    scale = ''

    try:
        opts, args = getopt.getopt(argv, "hd:s:", ["dimension", "scale"])
    except getopt.GetoptError:
        print("Invalid options. Run <script> -h for help")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('Syntax: <script> -d <dimension> -s <scale>')
            print('Inputs must be positive numbers')
            sys.exit(1)
        elif opt in ("-d", "--dimension"):
            dimension = int(arg)
        elif opt in ("-s", "--scale"):
            scale = int(arg)

    print("Dimesion : ", dimension)
    print("Scale    : ", scale)
    print()

    # make that grid
    # you may specify unique values for dimension and scale
    # or you may simply specify dimension and it will be used
    # for the scale value
    # dimensnion = # of columms/rows
    # scale = the segments count between column/row lines
    print_grid(dimension, scale=dimension)

if __name__ == "__main__":
    main(sys.argv[1:])