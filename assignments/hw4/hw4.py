"""
Name: <Steve Hyland>
hw4.py

Problem: <Create graphics window, draw fighures, respond to mouse clicks.>
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
#
import math
from graphics import GraphWin,Point,Text,Polygon,Rectangle,Circle
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
        shape = Polygon(Point(new_x, new_y), Point(new_x, new_y+50), \
                        Point(new_x+50, new_y+50), Point(new_x+50, new_y))
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
#  display the object
    shape = Rectangle(click1,click2)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
# now calculate the perimiter and area and display
    lengthx = math.fabs(click1.getX()-click2.getX())
    widthy = math.fabs(click1.getY()-click2.getY())
    perimeter = 2*(lengthx+widthy)
    area = lengthx*widthy
# Inform the user
    outputtext = Text(Point(215, 480), "Perimeter:")
    outputtext.draw(win)
    outputtext2 = Text(Point(260, 480), "")
    outputtext2.draw(win)
    outputtext2.setText(perimeter)
    outputtext = Text(Point(215, 495), "Area:")
    outputtext.draw(win)
    outputtext2 = Text(Point(255, 495), "")
    outputtext2.draw(win)
    outputtext2.setText(area)
# exit
    win.getMouse()
# #
def circle():
# # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)
#create a space to instruct user
    inst_pt = Point(width / 2, height - 40)
    #inst_pt2 = Point(width / 2,height - 5)
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
    outputtext = Text(Point(150, 395), "Radius:")
    outputtext.draw(win)
    outputtext2 = Text(Point(225,395),"")
    outputtext2.draw(win)
    outputtext2.setText(radius)
    win.getMouse()
    win.close()
#
def pi2():
    terms = eval(input("enter the number of terms to sum "))
    upper = terms * 2
# now, approximate pi
    pi4 = 0
    for num in range(1,upper+1,4):
        pi4 = pi4 + (4/num)
    for num in range(3,upper+1,4):
        pi4 = pi4 - (4/num)
    #
    accuracy = math.fabs(math.pi - pi4)
    print("pi approximation",pi4)
    print("accuaracy: ",accuracy)
#
#if __name__ == '__main__':
#    pass
#
    #circle()
    #squares()
    #oldsquares()
    #pi2()
    #rectangle()
