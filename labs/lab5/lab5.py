""""
Steve Hyland
File Name: lab5.py
Lab Assignment 5: Graphics, Strings, and Lists
I did this alone.
"""
#

from graphics import GraphWin,Point,Text,Circle,color_rgb,Entry,Polygon
import math

#
def triangle():
    width = 500
    height = 500
    win = GraphWin("Triangle", width, height)
    click1 = win.getMouse()
    click2 = win.getMouse()
    click3 = win.getMouse()
#
    # build first square
    shape = Polygon(click1, click2, click3)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
#   now calculate the sides
    side_ax = click1.getX() - click2.getX()
    side_ay = click1.getY() - click2.getY()
    sidea = math.sqrt(side_ax**2 + side_ay**2)
    #
    side_bx = click2.getX() - click3.getX()
    side_by = click2.getY() - click3.getY()
    sideb = math.sqrt(side_bx**2 + side_by**2)
    #
    side_cx = click3.getX() - click1.getX()
    side_cy = click3.getY() - click1.getY()
    sidec = math.sqrt(side_cx**2 + side_cy**2)
    #
    s = (sidea + sideb + sidec)/2
    area = math.sqrt(s*(s-sidea)*s*(s-sideb)*s*(s-sidec))
#
    # Inform the user
    outputtext = Text(Point(200, 480), "Perimeter:")
    outputtext.draw(win)
    outputtext2 = Text(Point(300, 480), "")
    outputtext2.draw(win)
    outputtext2.setText(s)
    outputtext = Text(Point(200, 495), "Area:")
    outputtext.draw(win)
    outputtext2 = Text(Point(300, 495), "")
    outputtext2.draw(win)
    outputtext2.setText(area)

    win.getMouse()

#
def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry_input = Entry(Point(win_width/2, win_height / 2 + 40),5)
    red_entry_input.setFill("orange")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry_input = red_entry_input.clone()
    green_entry_input.move(0,30)
    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry_input = green_entry_input.clone()
    blue_entry_input.move(0,30)

    # display rgb text
    red_text.draw(win)
    red_entry_input.draw(win)
    green_entry_input.draw(win)
    blue_entry_input.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
#
    for iter in range(5):
        red_entry_input.undraw()
        green_entry_input.undraw()
        blue_entry_input.undraw()
        red_entry_input.setText("")
        green_entry_input.setText("")
        blue_entry_input.setText("")
        red_entry_input.draw(win)
        green_entry_input.draw(win)
        blue_entry_input.draw(win)
#
        win.getMouse()
        # get the inputs
        input_red = red_entry_input.getText()
        input_green = green_entry_input.getText()
        input_blue = blue_entry_input.getText()
        red_num = int(input_red,10)
        green_num = int(input_green,10)
        blue_num = int(input_blue,10)
        shape.setFill((color_rgb(red_num, green_num, blue_num)))
    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    stng = input("Input a string: ")
    print(stng[0])
    print(stng[-1])
    print(stng[1:5])
    print(stng[0]+stng[-1])
    print(stng[0:3]*10)
    len_stng = len(stng)
    for idx in range(len_stng):
        print(stng[idx])
    print(len_stng)


def process_list():
    pt = Point(5, 10)
    values =[5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x=[]
    x.append(values[2])
    x.append(values[3])
    x.append(values[4])
    print(x)
    x=[]
    x.append(values[2])
    x.append(values[3])
    x.append(values[0])
    print(x)
    x=[]
    x.append(values[2])
    x.append(values[0])
    x.append(float(values[5]))
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    print(len(values))



def another_series():
    series = [2,4,6]
    terms = eval(input("input the number of terms: "))
    loop1 = terms//3
    sum = 0
    print("loop1 ", loop1)
    for idn in range(terms):
        digit = idn % 3
        sum = sum + series[digit]
        print(series[digit],end=" ")
    print()
    print("sum = ", sum)
#

def target():
    color_list = ["white","black","blue","red","yellow"]
# Creates a graphical window
    width = 500
    height = 500
    win = GraphWin("Target",width, height)
    ctr_pt = Point(width/2,height/2)
    for cirs in range(5):
        radius = (width/2) - (50*cirs)
        shape = Circle(ctr_pt,radius)
        shape.setFill(color_list[cirs])
        shape.draw(win)
    inst_pt = Point(width / 2, height - 40)
    instructions = Text(inst_pt, "Click to close")
    instructions.draw(win)
    win.getMouse()
    win.close()
#
triangle()
#target()
#color_shape()
#process_string()
#process_list()
#another_series()
