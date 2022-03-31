"""
Steve Hyland
File Name: lab10.py
Lab Assignment : classes & graphics
I did this alone.
"""
#
from graphics import GraphWin, Point, Rectangle, Text
from button import Button
from door import Door
def main():
##
    width_px = 700
    height_px = 700
    win = GraphWin("Text", width_px, height_px)
    rect1_p1 = Point(250,150)
    rect1_p2 = Point(450,250)
    rect1 = Rectangle(rect1_p1, rect1_p2)
    rect1.setFill('LightCyan')
    text1 = Text(rect1.getCenter(), "Exit")
    button = Button(rect1, text1)
    button.draw(win)
#
    rect2_p1 = Point(250, 300)
    rect2_p2 = Point(450, 650)
    rect2 = Rectangle(rect2_p1, rect2_p2)
    rect2.setFill('pink')
    text2 = Text(rect2.getCenter(), "Closed")
    door = Door(rect2, text2)
    door.draw(win)
#
    exit_button = False
    while exit_button is False:
        clicked = win.getMouse()
        exit_button = button.is_clicked(clicked)
        if exit_button is True:
            break
        door_click = door.is_clicked(clicked)
        if door_click is True:
            door_label = door.get_label()
            if door_label == 'Closed':
                door.open('alice blue', 'Open')
                door.set_label('Open')
            elif door_label == 'Open':
                door.close('pink', 'Closed')
    win.close()
#

main()