"""
Name: <Steve Hyland>
HW6.py

Problem: <Strings, formatting, functions>

Certification of Authenticity: I certify that this assignment is entirely my own work.

"""

import math
def cash_converter():
    int_in = eval(input("enter an integer: "))
    print("That is ${0:0.2f}".format(int_in))

def encode():
    message_in = input("enter a message: ")
    key_in = eval(input("enter a key: "))
    new_string = ""
    for letter in message_in:
        new_ord = ord(letter) + key_in
        new_chr = chr(new_ord)
        new_string = new_string + new_chr
    print(new_string)

#
def sphere_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

#
def sphere_volume(radius):
    sphere_vol = 4/3 * math.pi * radius ** 3
    return sphere_vol

#
def sum_n(number):
    sum_num = 0
    for i in range(number):
        sum_num = sum_num + (i + 1)
    return sum_num

#
def sum_n_cubes(number):
    sum_num_cubes = 0
    for i in range(number):
        sum_num_cubes = sum_num_cubes + (i +1) ** 3
    return sum_num_cubes

#
def encode_better():
    msg_in = input("enter a message: ")
    key_in = input("enter a key: ")
    len_key = len(key_in)
    len_msg = len(msg_in)
    msg_out = ""
    for idx_in in range(len_msg):
        key_off = idx_in % len_key
        new_ord = ord((msg_in[idx_in])) + (ord(key_in[key_off]) - 130)
        new_ord1 = (new_ord % 58) + 65
        msg_out = msg_out + chr(new_ord1)
    print(msg_out)

#
if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
#cash_converter()
#encode()
#encode_better()
#
