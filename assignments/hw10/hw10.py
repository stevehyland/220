"""
Name: <Steve Hyland>
HW10.py

Problem: Fibonacci, Suracuse, etc - Functions, decisions, and graphics

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
#
import sympy
from graphics import GraphWin, Point
import face
#
def fibonacci(num):
#
    fibs = []
    #fibs.append(1)
    #fibs.append(1)
    idx = 0
    while idx <= num:
        if idx <2:
            fibs.append(1)
            idx = idx + 1
        else:
            next_fib = fibs[idx - 2] + fibs[idx - 1]
            fibs.append(next_fib)
            idx = idx + 1
    return fibs[num - 1]
#
def double_investment(principle: float, rate: float):
    double_prin = principle * 2
    amt = principle
    years = 0
    while amt <= double_prin:
        #print(amt, years)
        if amt == double_prin:
            #print(years)
            return years
#
        amt = amt * (1 + rate)
        years = years + 1
    #print(amt, years)
    return years
#
def syracuse(num: int):
#
    #print('In Syracuse')
    syr_n = num
    odd_or_even = syr_n // 2
    syr_seq = []
    syr_seq.append(syr_n)
    #print(syr_n)
    while syr_n > 1:
        odd_or_even = syr_n % 2
        if odd_or_even == 0:
            syr_n = syr_n//2
            syr_seq.append(syr_n)
            #print(syr_n)
        else:
            syr_n = 3 * syr_n + 1
            syr_n = syr_n //1
            syr_seq.append(syr_n)
            #print(syr_n)
#
    return syr_seq
#
def goldbach(num):
    prime_nums = []
    factors = []
    odd_test = num % 2
    if odd_test != 0:
        return None
# get the prime numbers in the range 2 = num
    idx = 2
    while idx < num:
        if sympy.isprime(idx):
            prime_nums.append(idx)
        idx = idx + 1
    #print(prime_nums)
    num_nums = len(prime_nums)
# now, find out which one add to num
    idx = 1
    while idx < num_nums:
        id2 = idx + 1
        while id2 < num_nums:
            if prime_nums[idx] + prime_nums[id2] == num:
                factors.append(prime_nums[idx])
                factors.append(prime_nums[id2])
                #print(factors)
                return factors
            id2 = id2 + 1
        idx = idx + 1
#
def face_on():
    width_px = 700
    height_px = 700
    win = GraphWin("Face", width_px, height_px)
    pic = face.Face(win, Point(350, 350), 200)
    pic.smile()
    win.getMouse()
    win.close()
#

#face_on()


#double_investment(100.00, .10 )
#syracuse(5)
#goldbach(10)
#goldbach(100000)
# fibonacci(3)
# fibonacci(4)
# fibonacci(5)
# fibonacci(6)
# fibonacci(7)
# fibonacci(22)
#my_spheroid()
