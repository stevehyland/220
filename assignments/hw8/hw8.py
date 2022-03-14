"""
Name: <Steve Hyland>
HW8.py

Problem: Functions and decisions

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""

import math
from graphics import GraphWin,Point,Text,Circle

def add_ten(nums: list[int]):
    for idx in range(len(nums)):
        nums[idx] = nums[idx] + 10
#
def square_each(nums:list):
    for idx in range(len(nums)):
        nums[idx] = nums[idx] ** 2
#
def sum_list(nums:list):
    sum_nums = 0
    for number in nums:
        sum_nums = sum_nums + number
    return sum_nums
#
def to_numbers(nums:list[str]):
    for idx in range(len(nums)):
        nums[idx] = eval(nums[idx])
#
def sum_of_squares(nums:list[str]):
    summed_up = []
    for idx in range(len(nums)):
        num_char_str = nums[idx]
        num_char_str = num_char_str.replace(" ", "")
        num_list = num_char_str.split(",")
        to_numbers(num_list)
        square_each(num_list)
        summed_up.append(sum_list(num_list))
    return summed_up
#
def starter(weight, wins):
#
    return (weight >= 150 and weight < 160 and wins >= 5) or weight > 199 or wins > 20
#
def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4  == 0:
        return True
    return False
#
def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)
#
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 +
        (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
#
    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 +
        (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("coral1")
    circle_two.draw(win)
    t_or_f = did_overlap(circle_one, circle_two)
# now, inform user
# create a space to greet user
    inst_pt1 = Point(width / 2, height - 8)
    inst_pt = Point(width / 2, height - 9)
    instructions = Text(inst_pt, "Click again to exit.")
    instructions.draw(win)
    if t_or_f is True:
        message_t = Text(inst_pt1, "The circles overlap.")
        message_t.draw(win)
    else:
        message_f = Text(inst_pt1, "The circles do not overlap.")
        message_f.draw(win)
    win.getMouse()
#
def did_overlap(circle_one: Circle , circle_two: Circle ):
    radii_tot = circle_one.getRadius() + circle_two.getRadius()
# now calculate the distance between the two center points
    center1 = circle_one.getCenter()
    center2 = circle_two.getCenter()
    big_radius = math.sqrt(
     (center1.getX() - center2.getX()) ** 2 +
     (center1.getY() - center2.getY()) ** 2)
#
    return bool(radii_tot >= big_radius)
#
if __name__ == '__main__':
    pass
#
def leap_year_test(year):
    true_or_false = leap_year(year)
    return true_or_false

#
#add_ten([1,2,3,4,5,6])
#square_each([1,2,3,4,5, 6.2])
#sum_list([2,4,6,8.5])
#my_nums.append()
#to_numbers(['3', '7.2', '9'])
#test_to_numbers()
#sum_of_squares(['3,7.2,9'])
#torf = leap_year(int(2400))
#print(torf)
#circle_overlap()
#starter(210.2, 12)
#test_sum_of_squares()
#
