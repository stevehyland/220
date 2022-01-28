"""
Name: <Steve Hyland>
<HW2.py>

Problem: <HW2: write severl modules to illustrate loops and assignments >

Certification of Authenticity:I certify that this assignment is entirely my own work with
 help from Mr. Baier on one issue.

"""
import math
#
def sum_of_threes():
    upperbound = eval(input("What is the Upper Bound: "))
    max_possible = upperbound // 3
#    print (max_possible)
    accumulator = 0
    for i in range(1, max_possible+1):
        accumulator = accumulator + (i * 3)
#
    print("sum of threes is: ", accumulator)
#
def multiplication_table():
#
    # product = int
    for irow in range(10):
        for icolumn in range(10):
            product = (irow + 1) * (icolumn + 1)
            print(product,'\t',end='')
    print()
#
def triangle_area():
#
    area = float
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("enter side c length: "))
#
    sides = (side_a + side_b + side_c) / 2
    xprod = sides * (sides - side_a) * (sides - side_b) * (sides - side_c)
#
    area = math.sqrt(xprod)
    print("Area is: ", area)
#
def sum_squares():
    lower = eval(input("Input Lower Range: "))
    upper = eval(input("Input Upper Range: "))
#
    summed_squares = 0
    for i in range(lower, upper + 1):
        summed_squares = summed_squares + (i ** 2)
#
    print("Sum of the squares: ", summed_squares)


def power():
    base = eval(input("Input Base: "))
    exponent = eval(input("Input Exponent: "))
#
    powered_up = base
    for i in range(2, exponent +1):
        powered_up = powered_up * base
#    powered_up = math.pow(base,exponent)
    print(base, '^', exponent, '=', powered_up )
#
if __name__ == '__main__':
    pass
#
#multiplication_table()
#
#triangle_area()
#
#sum_squares()
#
#power()
#
#sum_of_threes()
