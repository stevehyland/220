import graphics
import time
from graphics import Circle, Line, Point


class Face:
    def __init__(self, window, center, size):
#
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)
#
    def smile(self):
#
        mid_smile = self.mouth.getCenter()
        smile_x = mid_smile.getX()
        smile_y = mid_smile.getY() + 50
        new_point = Point(smile_x, smile_y)
        left_point = self.mouth.getP1()
        right_point = self.mouth.getP2()
        smile1 = Line(left_point, new_point)
        smile1.draw(self.window)
        smile2 = Line(right_point, new_point)
        smile2.draw(self.window)
#
    def shock(self):
#
        shock_center = self.mouth.getCenter()
        self.mouth.undraw()
        shocked = Circle(shock_center, 20)
        shocked.draw(self.window)
#
    def wink(self):
#
        lefti = self.left_eye
        wink = lefti.getCenter()
        winkx = wink.getX()
        winky = wink.getY()
        wink_line = Line(graphics.Point(winkx -25, winky), graphics.Point(winkx + 25, winky))
        self.left_eye.undraw()
        wink_line.draw(self.window)
        self.smile()
#

