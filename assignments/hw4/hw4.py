"""
Name: <Steve Hyland>
stevehyland.py

Problem: <Create graphics window, draw fighures, respond to mouse clicks.>
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
#
import math
from graphics import *
#
def squares():
#
# Creates a graphical window
    width = 500
    height = 500
    win = GraphWin("Squares", width, height)
# create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)
#   number of times to click
    num_clicks = 5
# build first square
    shape = Polygon(Point(50,50), Point(50,100), Point(100,100), Point(100,50))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
# allows the user to click multiple times to draw a new square
    for _ in range(num_clicks):
        click = win.getMouse()
# move amount is distance from center of circle to the
        new_x = click.getX()
        new_y = click.getY()
#  draw the object
        shape = Polygon(Point(new_x,new_y),Point(new_x,new_y+50),\
                        Point(new_x+50,new_y+50),Point(new_x+50,new_y))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
# exit
    win.getMouse()
    win.close()
#
def rectangle():
    width = 500
    height = 500
    win = GraphWin("Rectangle", width, height)
    click1 = win.getMouse()
    click2 = win.getMouse()
    p1x = click1.getX()
    p1y = click1.getY()
    p3x = click2.getX()
    p3y = click2.getY()
    p2x = p1x + (p3x - p1x)
    p2y = p3y + (p1y - p3y)
    p4x = p1x
    p4y = p3y
    shape = Polygon(Point(p1x,p1y,),Point(p2x,p2y),Point(p3x,p3y),Point(p4x,p4y))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    #print(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y)
# now calculate the perimiter and area and display
    lengthx = math.fabs(p1x-p3x)
    widthy = math.fabs(p1y-p3y)
    perimeter = 2*(lengthx+widthy)
    area = lengthx*widthy
    print(perimeter,area)
# create a space to instruct user
    #inst_pt = Point(width / 2, height - 40)
    #inst_pt2 = Point(width / 2, height - 5)
# exit
    win.getMouse()
#
def circle():
# # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)
#create a space to instruct user
    inst_pt = Point(width / 2, height - 40)
    inst_pt2 = Point(width / 2,height - 5)
    click = win.getMouse()
    click_r = win.getMouse()
#calculate the radius
# calculate the values to use based on the clicks
    xval = (click.getX()-click_r.getX()) ** 2
    yval = (click.getY()-click_r.getY()) ** 2
    radius = math.sqrt(xval+yval)
    # builds a circle
    shape = Circle(Point(click.getX(),click.getY()),radius)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    instructions = Text(inst_pt, "Click again to close")
    instructions.draw(win)
#
    outputText = Text(Point(150, 395), "Radius:")
    outputText.draw(win)
    outputText2 = Text(Point(225,395),"")
    outputText2.draw(win)
    outputText2.setText(radius)
    win.getMouse()
    win.close()
#


#if __name__ == '__main__':
   # pass
#
def pi2():
    terms = eval(input("enter the number of terms to sum "))
    terms_left = terms // 2
    terms_right = terms // 2
    terms_left = terms_left + (terms % 2)  # is terms an odd number?
    #print(terms_left, terms_right)
    upper = terms * 2
# now, approximate pi
    pi4 = 0
    for n in range(1,upper+1,4):
        pi4 = pi4 + (4/n)
    for n in range(3,upper+1,4):
        pi4 = pi4 - (4/n)
    #
    accuracy = math.fabs(math.pi - pi4)
    print("pi approximation",pi4)
    print("accuaracy: ",accuracy)

if __name__ == '__main__':
    pi2()

    #from graphics import *


    # def oldsquares():
    #     # Creates a graphical window
    #     width = 400
    #     height = 400
    #     win = GraphWin("Clicks", width, height)
    #
    #     # number of times user can move circle
    #     num_clicks = 5
    #
    #     # create a space to instruct user
    #     inst_pt = Point(width / 2, height - 10)
    #     instructions = Text(inst_pt, "Click to move circle")
    #     instructions.draw(win)
    #
    #     # builds a circle
    #     shape = Circle(Point(50, 50), 20)
    #     shape.setOutline("red")
    #     shape.setFill("red")
    #     shape.draw(win)
    #
    #     # allows the user to click multiple times to move the circle
    #     for i in range(num_clicks):
    #         click = win.getMouse()
    #         center = shape.getCenter()  # center of circle
    #
    #         # move amount is distance from center of circle to the
    #         # point where the user clicked
    #         change_x = click.getX() - center.getX()
    #         change_y = click.getY() - center.getY()
    #         shape.move(change_x, change_y)
    #
    #     win.getMouse()
    #     win.close()
#
    if __name__ == '__main__':
        pass
    #circle()
    #squares()
    #oldsquares()
    #pi2()
    #rectangle()
