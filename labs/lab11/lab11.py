"""
Steve Hyland
File Name: button.py
Lab Assignment 11 : Random Numbers, graphics
I did this alone.
"""
#
from graphics import GraphWin, Point, Rectangle, Text
from random import randint
from lab10.button import Button
from lab10.door import Door
#
def main():
##
    wins = 0
    losses = 0
    width_px = 700
    height_px = 700
    win = GraphWin("Three Door Game", width_px, height_px)
    rect1_p1 = Point(500,50)
    rect1_p2 = Point(650,150)
    rect1 = Rectangle(rect1_p1, rect1_p2)
    rect1.setFill('pink')
    text1 = Text(rect1.getCenter(), "Quit")
    button = Button(rect1, text1)
    button.draw(win)
    msg1 = Text(Point(340, 200), 'I have a secret door!')
    msg1.draw(win)
    msg2 = Text(Point(330, 650), 'Click to guess which is the secret door!')
    msg2.draw(win)
#
    wscore_p1 = Point(50, 50)
    wscore_p2 = Point(100, 100)
    wscore = Rectangle(wscore_p1, wscore_p2)
    wscore.setFill('white')
    text_wins = Text(wscore.getCenter(), str(wins))
    wscore = Button(wscore, text_wins)
    wscore.draw(win)
    wins_msg = Text(Point(75, 40), "Wins")
    wins_msg.draw(win)
#
    lscore_p1 = Point(100, 50)
    lscore_p2 = Point(150, 100)
    lscore = Rectangle(lscore_p1, lscore_p2)
    lscore.setFill('white')
    text_losses = Text(lscore.getCenter(), str(losses))
    lscore = Button(lscore, text_losses)
    lscore.draw(win)
    losses_msg = Text(Point(125, 40), "Losses")
    losses_msg.draw(win)
#
    door1_p1 = Point(135, 260)
    door1_p2 = Point(250, 610)
    door1_rec = Rectangle(door1_p1, door1_p2)
    door1_rec.setFill('saddle brown')
    door1_txt = Text(door1_rec.getCenter(), "Door 1")
    door1 = Door(door1_rec, door1_txt)
    door1.draw(win)
#
    door2_p1 = Point(285, 260)
    door2_p2 = Point(400, 610)
    door2_rec = Rectangle(door2_p1, door2_p2)
    door2_rec.setFill('saddle brown')
    door2_txt = Text(door2_rec.getCenter(), "Door 2")
    door2 = Door(door2_rec, door2_txt)
    door2.draw(win)
#
    door3_p1 = Point(435, 260)
    door3_p2 = Point(550, 610)
    door3_rec = Rectangle(door3_p1, door3_p2)
    door3_rec.setFill('saddle brown')
    door3_txt = Text(door3_rec.getCenter(), "Door 3")
    door3 = Door(door3_rec, door3_txt)
    door3.draw(win)
    clicked = win.getMouse()
#  Now. lets play the game!
    while not button.is_clicked(clicked):
        msg2.setText('Click anywhere to play again!')
        secret_door = randint(1,3)
        if secret_door == 1:
            door1.set_secret(True)
        elif secret_door == 2:
            door2.set_secret(True)
        else:
            door3.set_secret(True)
        if door1.is_clicked(clicked):
            if door1.is_secret():
                door1_rec.setFill('green')
                wins += 1
                text_wins.setText(str(wins))
                msg1.setText('You win!')
            else:
                door1_rec.setFill('red')
                losses += 1
                text_losses.setText(str(losses))
                msg1.setText('Sorry, incorrect')
                if secret_door == 2:
                    door2_rec.setFill('green')
                else:
                    door3_rec.setFill('green')
#
        if door2.is_clicked(clicked):
            if door2.is_secret():
                door2_rec.setFill('green')
                wins += 1
                text_wins.setText(str(wins))
                msg1.setText('You win!')
            else:
                door2_rec.setFill('red')
                losses += 1
                text_losses.setText(str(losses))
                msg1.setText('Sorry, incorrect')
                if secret_door == 1:
                    door1_rec.setFill('green')
                else:
                    door3_rec.setFill('green')
#
        if door3.is_clicked(clicked):
            if door3.is_secret():
                door3_rec.setFill('green')
                wins += 1
                text_wins.setText(str(wins))
                msg1.setText('You win!')
            else:
                door3_rec.setFill('red')
                losses += 1
                text_losses.setText(str(losses))
                msg1.setText('Sorry, incorrect')
                if secret_door == 1:
                    door1_rec.setFill('green')
                else:
                    door2_rec.setFill('green')
#
        clicked = win.getMouse()
        door1_rec.setFill('saddle brown')
        door2_rec.setFill('saddle brown')
        door3_rec.setFill('saddle brown')
        msg1.setText('I have a secret door!')
        door1.set_secret(False)
        door2.set_secret(False)
        door3.set_secret(False)
    win.close()

main()