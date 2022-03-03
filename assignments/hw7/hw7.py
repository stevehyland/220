"""
Name: <Steve Hyland>
HW7.py

Problem: File processing, functions, modular programming

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
#
from encryption import encode, encode_better
#

def number_words(in_file_name, out_file_name):
    input_words = []
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    input_lines = infile.read()
    input_lines = input_lines.replace("\n", " ")
    input_lines = input_lines.rstrip()
    input_words = input_lines.split(" ")
    for idx in range(len(input_words)):
        print(idx+1, input_words[idx], file = outfile)
#
    infile.close()
    outfile.close()
#
def hourly_wages(in_file_name, out_file_name):
#
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    in_emps = infile.readlines()
    num_emps = len(in_emps)
    for idx in range(num_emps):
        each_emp = in_emps[idx].split(" ")
        rate = float(each_emp[2])
        hours = float(each_emp[3])
        total_pay = (hours * (rate + 1.65))
        print(each_emp[0], each_emp[1], "{0:0.2f}".format(total_pay), file=outfile)
    infile.close()
    outfile.close()
#
def calc_check_sum(isbn):
#
    new_isbn = isbn.replace("-", "")
    checksum = 0
    for idx in range(10):
        digit = int(new_isbn[idx])
        checksum = checksum + (digit * (10 - idx))
    return checksum
#
def send_message(file_name, friend_name):
    newfile = friend_name + ".txt"
    infile = open(file_name, "r")
    outfile = open(newfile, "w")
    file_in = infile.readlines()
    len_in = len(file_in)
    for idx in range(len_in):
        print(file_in[idx], end=(""), file = outfile)
    infile.close()
    outfile.close()
#
def send_safe_message(file_name, friend_name, key):
    friend_file = friend_name + ".txt"
    file_in = open(file_name, "r")
    outfile = open(friend_file, "w")
    in_lines = file_in.readlines()
    len_in = len(in_lines)
#
    for idx in range(len_in):
        string_out = in_lines[idx].replace("\n","")
        string_in = encode(string_out, key)
        print(string_in, file = outfile)
    file_in.close()
    outfile.close()
#
def send_uncrackable_message(file_name, friend_name, pad_file_name):
    out_file_name = friend_name + ".txt"
    in_file = open(file_name, "r")
    out_file = open(out_file_name, "w")
    pad_in = open(pad_file_name)
    key = pad_in.read()
    pad_in.close()
    in_string = in_file.read()
    coded_msg = encode_better(in_string, key)
    print(coded_msg, file = out_file)
    in_file.close()
    out_file.close()
#
if __name__ == '__main__':
    pass
#
#number_words("scratch_1.txt", "number_words_1_expected.txt")
#hourly_wages("hourly_wages.txt", "hourly_wages_out.txt")
#cksum = calc_check_sum("0-072-94652-0")
#print(cksum)
#send_message("my_msg.txt", "tyrone")
#send_safe_message("safer.txt", "safest", ord("A"))
#send_uncrackable_message("uncrackable.txt", "jimbo", "pad.txt")
