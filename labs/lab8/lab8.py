"""
Steve Hyland
File Name: lab8.py
Lab Assignment : graphics and decisions.
I did this alone.
"""
import math
import random
from graphics import *
import time
#
def get_random(move_amount: int):
    amt = random.randint(-move_amount, move_amount)
    return amt
#
def get_random_color():
    rand_red = random.randint(0,255)
    rand_green = random.randint(0,255)
    rand_blue = random.randint(0,255)
    rand_color = color_rgb(rand_red, rand_green, rand_blue)
    return rand_color
#
def did_collide(ball: Circle , ball2: Circle ):
    radii_tot = ball.getRadius() + ball2.getRadius()
# now calculate the distance between the two center points
    center1 = ball.getCenter()
    center2 = ball2.getCenter()
    big_radius = math.sqrt(
     (center1.getX() - center2.getX()) ** 2 +
     (center1.getY() - center2.getY()) ** 2)
    return bool(radii_tot >= big_radius)
#
def hit_vertical(ball: Circle, win: GraphWin):
#  where are we?
    radius = ball.getRadius()
    center1 = ball.getCenter()
    cen_y = center1.getY()
    height = win.getHeight()
# now see if we hit a wall
    return bool((cen_y - radius <= 0) or (cen_y + radius >= height))
#
def hit_horizontal(ball: Circle, win: GraphWin):
#  where are we?
    radius = ball.getRadius()
    center1 = ball.getCenter()
    cen_x = center1.getX()
    width = win.getWidth()
#check left/right
    return bool((cen_x + radius >= width) or (cen_x - radius <= 0))
#
def bumper():
# now, draw circles and set initial positions move.
    width_px = 700
    height_px = 700
    win = GraphWin("Collision Control", width_px, height_px)
#
    circle_one = Circle(Point(100,100),75)
    circle_one.setFill(get_random_color())
    circle_one.draw(win)
#
    circle_two = Circle(Point(600,600), 75)
    circle_two.setFill(get_random_color())
    circle_two.draw(win)
    time.sleep(1)
#
    while win.checkMouse() == None:
#   move circles from starting positions
        x1_delta = get_random(75)
        y1_delta = get_random(75)
        x2_delta = get_random(75)
        y2_delta = get_random(75)
        circle_one.move(x1_delta, y1_delta)
        time.sleep(.1)
        circle_two.move(x2_delta, y2_delta)
# did 1 hit top or bottom?
        if hit_vertical(circle_one, win):
            y1_delta = y1_delta * -2
            circle_one.move(0, y1_delta)
        time.sleep(.1)
# did 1 hit a side?
        if hit_horizontal(circle_one, win):
            x1_delta = x1_delta * -2
            circle_one.move(x1_delta, 0)
            time.sleep(.1)
# did we collide?
        if did_collide(circle_one, circle_two):
            x1_delta = x1_delta * -2
            y1_delta = y1_delta * -2
            circle_one.move(x1_delta, y1_delta)
#
            x2_delta = x2_delta * -2
            y2_delta = y2_delta * -2
            circle_two.move(x2_delta, y2_delta)
            time.sleep(.1)
# did 2 hit top or bottom?
        if hit_vertical(circle_two, win):
            y2_delta = y2_delta * -2
            circle_two.move(0, y2_delta)
            cpoints = circle_two.getP1()
            time.sleep(.1)
            # did we hit a side?
        if hit_horizontal(circle_two, win):
            x2_delta = x2_delta * -2
            circle_two.move(x2_delta, 0)
            time.sleep(.5)
# are the circles overlapping?
        if did_collide(circle_one, circle_two):
            x1_delta = x1_delta * -2
            y1_delta = y1_delta * -2
            circle_one.move(x1_delta, y1_delta)
#
            x2_delta = x2_delta * -2
            y2_delta = y2_delta * -2
            circle_two.move(x2_delta, y2_delta)
#
#bumper()
