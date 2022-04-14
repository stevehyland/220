"""
Steve Hyland
File Name: algorithms.py
Lab Assignment 12 : functions, lists
I did this alone.
"""
#

#
def read_data(filename):
    num_list = []
    infile = open(filename, 'r')
    line = infile.readline()
    while line:
        work_list = line.split()
        line = infile.readline()
        indx = 0
        while indx < len(work_list):
            num_list.append(eval(work_list[indx]))
            indx += 1
    infile.close()
    return num_list
#
def is_in_linear(search_val, values):
    indx = 0
    while indx < len(values):
        if values[indx] == search_val:
            return True
        indx += 1
    return False
#
# def main():
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
#
# main()