""""
Steve Hyland
File Name: lab4.py
Lab Assignment 4: Graphics Programming
I did this alone.
"""
from graphics import *
#
def greeting_card():
# Creates a graphical window
    width = 500
    height = 500
    win = GraphWin("Be My Valentine", width, height)
# create a space to greet user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Happy Valentine's Day!")
    instructions.draw(win)
    win.setBackground('pink')
    heart = Polygon(Point(250,200),Point(275,175),Point(325,200),Point(300,250), \
                    Point(250,350),Point(200,250),Point(175,200,),Point(225,175))
    heart.setOutline("purple")
    heart.setFill("red")
    heart.draw(win)
    arrow = Line(Point(0,250),Point(150,250))
    arrow.setArrow("last")
    arrow.setWidth(3)
    arrow.draw(win)
    for _ in range(20):
        arrow.move(10,0)
        time.sleep(.5)
    instructions.undraw()
    instructions = Text(inst_pt, "Click anywhere to close")
    instructions.draw(win)
    win.getMouse()
    win.close()
#
greeting_card()
