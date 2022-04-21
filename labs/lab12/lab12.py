"""
Steve Hyland
File Name: lab12.py
Lab Assignment 12 : functions, lists
I did this alone.
"""
#
#
from random import randint
from algorithms import *
#
def num_digits():
    in_num = eval(input('Input a number (0 or negative to stop):'))
    #annual_rate = eval(input("Enter your Annual Interest Rate: "))
    while in_num > 0:
        #remainder = 1
        num_digits = 0
        while in_num != 0:
            in_num = in_num // 10
            num_digits += 1
        print('The number entered contained : ', num_digits)
        in_num = eval(input('Input a number (0 or negative to stop):'))
#
def hi_low_game():
    ran_num = randint(1,100)
    print(ran_num)
    guesses_left = 7
    guesses_used = 0
    won = False
    while guesses_left > 0:
        wag = eval(input("Enter your guess (between 1 and 100 inclusive) "))
        if wag == ran_num:
            guesses_left -= 1
            guesses_used += 1
            print('Correct! It took you ', guesses_used, 'to win!')
            won = True
            guesses_left = 0
        else:
            guesses_left -= 1
            guesses_used += 1
            if wag < ran_num:
                print('your guess is low')
            else:
                print('your guess is high')
    if won is False:
        print('Sorry, you didn\'t win, the number was:', ran_num)
#
def good_input():
    good = False
    while good is False:
        num_in = eval(input("Enter a number between 1 and 10 inclusive: "))
        if num_in >= 1 and num_in <= 10:
            print('good number (', num_in, ') returned!')
            return
        elif num_in > 10:
            print('The number entered (', num_in,  ') is too high.  The range is 1 - 10 inclusive.')
        else:
            print('The number entered (', num_in, ') is too low.  The range is 1 - 10 inclusive.')
#
def find_and_remove_first(list_in, val):
    indx = list_in.index(val)
    list_in.remove(val)
    list_in.insert(indx, 'Steve')

#
#def main():
#
#     num_digits()
#     hi_low_game()
#     good_input()
#     my_list = [1, 3, 5, 7, 22, 55, 98]
#     find_and_remove_first(my_list, 22)
#     find_and_remove_first(my_list, 1)
# # test imported modules
#     print(read_data('data_sorted.txt'))
#     values = []
#     values.append('Steve')
#     values.append(123)
#     values.append('123')
#     values.append(float(3.1416))
#     #print(values)
#     found = is_in_linear('3.1416', values)
#     print(found)
#
#main()

