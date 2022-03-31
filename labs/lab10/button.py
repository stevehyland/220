"""
Steve Hyland
File Name: button.py
Lab Assignment 10 : classes & graphics
I did this alone.
"""
#

#import graphics
#import time
#from graphics import Text, Point
#
class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = label
#
    def get_label(self):
        return self.text.getText()
#
    def set_label(self, label):
        self.text.setText(label)
 #
    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)
#
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()
#
    def color_button(self, color):
        self.shape.setFill(color)
#
    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        if (point.getX() >= p1.getX() and point.getX() <= p2.getX() and
            point.getY() >= p1.getY() and point.getY() <= p2.getY()):
            return True
        return False

