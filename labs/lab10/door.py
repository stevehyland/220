"""
Steve Hyland
File Name: door.py
Lab Assignment Lab 10: classes & graphics
I did this alone.
"""
#
#
import graphics
import time
from graphics import Circle, Line, Text


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = label
        self.secret_door = False

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
        self.text.setTextColor('white')
    #
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()
    #
    def color_door(self, color):
        self.shape.setFill(color)
    #
    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)
        self.text.setTextColor('black')
    #
    def close(self,color,label):
        self.shape.setFill(color)
        self.text.setText(label)
    #
    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        if (point.getX() >= p1.getX() and point.getX() <= p2.getX() and
                point.getY() >= p1.getY() and point.getY() <= p2.getY()):
            return True
        return False
    #
    def set_secret(self, state):
        self.secret_door = state
    #
    def is_secret(self):
        return self.secret_door
