"""
Steve Hyland
File Name: lab6.py
Lab Assignment 6: Ciphers with input/output in a window.
I did this alone.

"""
from graphics import *
def vigenere_cipher():
#
    width = 500
    height = 500
    win = GraphWin("Vigenere", width, height)
#
    outputtext1 = Text(Point(100, 50), "Message to Code")
    outputtext1.draw(win)
    message_input = Entry(Point(300, 50), 30)
    message_input.setFill("orange")
    message_input.draw(win)
#
    outputtext2 = Text(Point(100, 75), "Enter Keyword")
    outputtext2.draw(win)
    keyword_input = Entry(Point(280, 75), 25)
    keyword_input.setFill("pink")
    keyword_input.draw(win)
#
    arectangle = Rectangle(Point(250,200),Point(350,275))
    arectangle.draw(win)
    rectangle_word = Text(Point(300,235), "Encode")
    rectangle_word.draw(win)
#
    win.getMouse()
    rectangle_word.undraw()
    arectangle.undraw()
# now, get the inputs and encode
    input_msg = message_input.getText()
    input_key = keyword_input.getText()
    upper_msg = input_msg.upper()
    upper_key = input_key.upper()
    upper1_msg = upper_msg.replace(" ","")
    upper1_key = upper_key.replace(" ","")
#
    len_key = len(upper1_key)
    len_msg = len(upper1_msg)
    msg_out = ""
    for idx_in in range(len_msg):
        key_off = idx_in % len_key
        new_ord = ord((upper1_msg[idx_in])) + (ord(upper1_key[key_off]) - 130)
        new_ord1 = (new_ord % 26) + 65
        msg_out = msg_out + chr(new_ord1)
    outputtext3 = Text(Point(250, 250), "Resulting Mesage")
    outputtext3.draw(win)
    outputtext4 = Text(Point(250, 275), "")
    outputtext4.setText(msg_out)
    outputtext4.draw(win)
    outputtext5 = Text(Point(250, 490), "Click Anywhere to Close Window")
    outputtext5.draw(win)
    win.getMouse()
    win.close()
#
#
vigenere_cipher()
