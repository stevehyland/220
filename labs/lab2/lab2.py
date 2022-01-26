"""
Steve Hyland
File Name: lab2.py
Lab1 Assignment 2: Calculate Mean value of entered data.
I did this alone.
"""
import math
def means():
    accumulator = 0
    rms_sum = 0
    rms = 0
    har_mean_sum = 0
    har_mean = 0
    geo_mean_sum = 1
    geo_mean = 0
    numbers = eval(input("Enter the values to be enterd: "))
    print("Numbers to enter", numbers)
    for i in range(1,numbers+1):
        inval = eval(input("enter value: "))
        accumulator = accumulator + inval
# do summations
        rms_sum = rms_sum + (inval**2)
        har_mean_sum = har_mean_sum + (1/inval)
        geo_mean_sum = geo_mean_sum * inval
#
    rms = math.sqrt(rms_sum/numbers)
    har_mean = numbers/har_mean_sum
    geo_mean = geo_mean_sum **(1/numbers)

    print("RMS :", rms)
    print("Harmonic Mean: ", har_mean)
    print("Geometric Mean: ", geo_mean)


means()
