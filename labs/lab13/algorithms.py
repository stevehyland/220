"""
Steve Hyland
File Name: algorithms.py
Lab Assignment 12 : functions, lists
I did this alone.
"""
#
from graphics import Rectangle, Point
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
def selection_sort(in_list):
    list_len = len(in_list)
    index = 0
    for indx in range(list_len):
       min = in_list[indx]
       index = indx
       for indx1 in range(indx + 1, list_len):
            if in_list[indx1] < min:
                min = in_list[indx1]
                index = indx1
       temp = in_list[indx]
       in_list[indx] = in_list[index]
       in_list[index] = temp
    #print(in_list)
#
def calc_area(rect):
# input is a rectangle object
    p1 = rect.getP1()
    p2 = rect.getP2()
    x1 = p1.getX()
    x2 = p2.getX()
    xl = abs(x2 - x1)
    y1 = p1.getY()
    y2 = p2.getY()
    yl = abs(y1-y2)
    area = xl * yl
    return area
#
def rec_sort(rectangles):
    rect_work = []
    unsorted_areas = []
    areas = []
    for indx in range(len(rectangles)):
        area = calc_area(rectangles[indx])
        areas.append(area)
        rect_work.append(area)
        rect_work.append(rectangles[indx])
        unsorted_areas.append(rect_work)
        rect_work = []
    selection_sort(areas)
    sorted_by_area = []
    for indx in range(len(areas)):
        indx1 = unsorted_areas.index(unsorted_areas[indx])
        sorted_by_area.append(rectangles[indx1])
        indx1 = 0
    rectangles = sorted_by_area
    #print(sorted_by_area)
    #print(rectangles)
#
#def main():
#     print(read_data('data_sorted.txt'))
#     values = []
#     values.append('Steve')
#     values.append(123)
#     values.append('123')
#     values.append(float(3.1416))
#     #print(values)
#     found = is_in_linear('3.1416', values)
#     print(found)
#     selection_sort([99,3,1,6,8, 56,22,101,999])
#
    # rectangles = [Rectangle(Point(100,150), Point(200,240)),
    #               Rectangle(Point(0, 20), Point(20, 40)),
    #               Rectangle(Point(10, 20), Point(20, 40)),
    #               Rectangle(Point(5,5), Point(10,10))]
    # rec_sort(rectangles)
#main()