"""
Name: <Steve Hyland>
HW9.py

Problem: Hangman - Functions, decisions, while loops, and graphics

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work with input from Prof. Baier.

"""
#
import random
from graphics import GraphWin, Circle, Line, Point, Entry, Text
#
def get_words(file_name):
# open the file and get the words, then close the file
    infile = open(file_name, "r")
    words_in = infile.readlines()
    infile.close()
    #words = words_str.split('\n')
    #words = words_str.split()
    return words_in
#
def get_random_word(words):
# select a word randomly and return
    num_words = len(words)
    word_num = random.randint(0, (num_words -1))
    new_secret_word = words[word_num].strip('\n')
    #print(secret_word)
    return new_secret_word
#
def letter_in_secret_word(letter, secret_word):
    #print('In letter_in_secret_word', secret_word)
    for idx in range(len(secret_word)):
        if secret_word[idx] == letter:
            #print('Found letter', letter)
            return True
    return False
#
def already_guessed(letter, guesses):
    #print('in already guessed', letter,guesses)
    if len(guesses) == 0:
        guesses.append(letter)
        return False
    #else:
    for idx in range(len(guesses)):
        if letter == guesses[idx]:
            return True
    guesses.append(letter)
    return False
#
def make_hidden_secret(secret_word, guesses):
    work_string = ""
    for idx in range(len(secret_word)):
        hit = 'n'
        for idn in range(len(guesses)):
            if secret_word[idx] == guesses[idn]:
                work_string = work_string + guesses[idn] + ' '
                hit = 'y'
        if hit == 'n':
            work_string = work_string + '_ '
#
    work_string = work_string.rstrip()
    return work_string
#
def won(guessed):
    for idx in range(len(guessed)):
        if guessed[idx] == '_':
            return False
    return True
#
def play_graphics(secret_word):
#
    width_px = 700
    height_px = 700
    win = GraphWin("Hangman", width_px, height_px)
    in_msg = Text(Point(250, 675), "Enter Letter")
    in_msg.draw(win)
    guess_box = Entry(Point(310, 625), 10)
    guess_box.setFill('white')
    guess_box.setText('- - - - - -')
    guess_box.draw(win)
    entry_box = Entry(Point(295, 675), 1)
    entry_box.setFill('white')
    entry_box.setText("")
    entry_box.draw(win)
    bot_line = Line(Point(200, 600), Point(500, 600))
    bot_line.draw(win)
    main_line = Line(Point(400, 100), Point(400, 600))
    main_line.draw(win)
    top_line = Line(Point(275, 100), Point(400, 100))
    top_line.draw(win)
    cen_line = Line(Point(275, 100), Point(275, 175))
    cen_line.draw(win)
    a_box = Entry(Point(600, 40), 1)
    a_box.setText('a')
    a_box.setFill('white')
    a_box.draw(win)
    b_box = Entry(Point(645, 40), 1)
    b_box.setText('b')
    b_box.setFill('white')
    b_box.draw(win)
    c_box = Entry(Point(600, 70), 1)
    c_box.setText('c')
    c_box.setFill('white')
    c_box.draw(win)
    d_box = Entry(Point(645, 70), 1)
    d_box.setText('d')
    d_box.setFill('white')
    d_box.draw(win)
    e_box = Entry(Point(600, 100), 1)
    e_box.setText('e')
    e_box.setFill('white')
    e_box.draw(win)
    f_box = Entry(Point(645, 100), 1)
    f_box.setText('f')
    f_box.setFill('white')
    f_box.draw(win)
    g_box = Entry(Point(600, 130), 1)
    g_box.setText('g')
    g_box.setFill('white')
    g_box.draw(win)
    h_box = Entry(Point(645, 130), 1)
    h_box.setText('h')
    h_box.setFill('white')
    h_box.draw(win)
    i_box = Entry(Point(600, 160), 1)
    i_box.setText('i')
    i_box.setFill('white')
    i_box.draw(win)
    j_box = Entry(Point(645, 160), 1)
    j_box.setText('j')
    j_box.setFill('white')
    j_box.draw(win)
    k_box = Entry(Point(600, 190), 1)
    k_box.setText('k')
    k_box.setFill('white')
    k_box.draw(win)
    l_box = Entry(Point(645, 190), 1)
    l_box.setText('l')
    l_box.setFill('white')
    l_box.draw(win)
    m_box = Entry(Point(600, 220), 1)
    m_box.setText('m')
    m_box.setFill('white')
    m_box.draw(win)
    n_box = Entry(Point(645, 220), 1)
    n_box.setText('n')
    n_box.setFill('white')
    n_box.draw(win)
    o_box = Entry(Point(600, 250), 1)
    o_box.setText('o')
    o_box.setFill('white')
    o_box.draw(win)
    p_box = Entry(Point(645, 250), 1)
    p_box.setText('p')
    p_box.setFill('white')
    p_box.draw(win)
    q_box = Entry(Point(600, 280), 1)
    q_box.setText('q')
    q_box.setFill('white')
    q_box.draw(win)
    r_box = Entry(Point(645, 280), 1)
    r_box.setText('r')
    r_box.setFill('white')
    r_box.draw(win)
    s_box = Entry(Point(600, 310), 1)
    s_box.setText('s')
    s_box.setFill('white')
    s_box.draw(win)
    t_box = Entry(Point(645, 310), 1)
    t_box.setText('t')
    t_box.setFill('white')
    t_box.draw(win)
    u_box = Entry(Point(600, 340), 1)
    u_box.setText('u')
    u_box.setFill('white')
    u_box.draw(win)
    v_box = Entry(Point(645, 340), 1)
    v_box.setText('v')
    v_box.setFill('white')
    v_box.draw(win)
    w_box = Entry(Point(600, 370), 1)
    w_box.setText('w')
    w_box.setFill('white')
    w_box.draw(win)
    x_box = Entry(Point(645, 370), 1)
    x_box.setText('x')
    x_box.setFill('white')
    x_box.draw(win)
    y_box = Entry(Point(600, 400), 1)
    y_box.setText('y')
    y_box.setFill('white')
    y_box.draw(win)
    z_box = Entry(Point(645, 400), 1)
    z_box.setText('z')
    z_box.setFill('white')
    z_box.draw(win)
# now, input letters
    print('In play_graphic, secret word = ', secret_word)
    hidden_word = []
    for idx in range(len(secret_word)):
        hidden_word.append('-')
    guesses = []
    guesses_left = 6
    word_string = ""
#
    while guesses_left > 0:
        word_string = make_hidden_secret(secret_word, guesses)
        guess_box.setText(word_string)
        success = won(word_string)
        #if success == True:
        if success:
            winner = Text(Point(347,25),"Winner!")
            winner.draw(win)
            in_msg.undraw()
            entry_box.undraw()
            quit_msg = Text(Point(300, 675), "Click to Close ")
            quit_msg.draw(win)
            win.getMouse()
            return
#
        #print('Word String: ', word_string)
        ltr_in = entry_box.getText()
        win.getMouse()
        #print(ltr_in)
        if ltr_in == 'a':
            #setattr(win, a_box, 'pink')
            a_box.setFill('pink')
        elif ltr_in == 'b':
            b_box.setFill('pink')
        elif ltr_in == 'c':
            c_box.setFill('pink')
        elif ltr_in == 'd':
            d_box.setFill('pink')
        elif ltr_in == 'e':
            e_box.setFill('pink')
        elif ltr_in == 'f':
            f_box.setFill('pink')
        elif ltr_in == 'g':
            g_box.setFill('pink')
        elif ltr_in == 'h':
            h_box.setFill('pink')
        elif ltr_in == 'i':
            i_box.setFill('pink')
        elif ltr_in == 'j':
            j_box.setFill('pink')
        elif ltr_in == 'k':
            k_box.setFill('pink')
        elif ltr_in == 'l':
            l_box.setFill('pink')
        elif ltr_in == 'm':
            m_box.setFill('pink')
        elif ltr_in == 'n':
            n_box.setFill('pink')
        elif ltr_in == 'o':
            o_box.setFill('pink')
        elif ltr_in == 'p':
            p_box.setFill('pink')
        elif ltr_in == 'q':
            q_box.setFill('pink')
        elif ltr_in == 'r':
            r_box.setFill('pink')
        elif ltr_in == 's':
            s_box.setFill('pink')
        elif ltr_in == 't':
            t_box.setFill('pink')
        elif ltr_in == 'u':
            u_box.setFill('pink')
        elif ltr_in == 'v':
            v_box.setFill('pink')
        elif ltr_in == 'w':
            w_box.setFill('pink')
        elif ltr_in == 'x':
            x_box.setFill('pink')
        elif ltr_in == 'y':
            y_box.setFill('pink')
        elif ltr_in == 'z':
            z_box.setFill('pink')
#
        in_list = already_guessed(ltr_in, guesses)
        if not in_list:
            in_secret_word = letter_in_secret_word(ltr_in, secret_word)
            #if in_secret_word == True:
            if in_secret_word:
                for idx in range(len(secret_word)):
                    if secret_word[idx] == ltr_in:
                        hidden_word[idx] = ltr_in
            else:
                # draw carcus
                if guesses_left == 5:
                    cir_head = Circle(Point(275, 200), 25)
                    cir_head.draw(win)
                elif guesses_left == 4:
                    torso_line = Line(Point(275, 225), Point(275, 400))
                    torso_line.draw(win)
                elif guesses_left == 3:
                    left_arm = Line(Point(275, 250), Point(225, 300))
                    left_arm.draw(win)
                elif guesses_left == 2:
                    right_arm = Line(Point(275, 250), Point(325, 300))
                    right_arm.draw(win)
                elif guesses_left == 1:
                    left_leg = Line(Point(275, 400), Point(225, 500))
                    left_leg.draw(win)
                    win.getMouse()
                guesses_left = guesses_left - 1
#
    if guesses_left == 0:
        right_leg = Line(Point(275, 400), Point(325, 500))
        right_leg.draw(win)
        loser = Text(Point(347,25),"Sorry, you did not win.")
        loser.draw(win)
        answer_string = 'The word was ' + secret_word
        mistery = Text(Point(347, 37), answer_string)
        mistery.draw(win)
        in_msg.undraw()
        entry_box.undraw()
        quit_msg = Text(Point(300, 675), "Click to Close ")
        quit_msg.draw(win)
        win.getMouse()
#
    win.getMouse()
#
    win.close()
#
def print_and_prompt(guesses_left, guesses, hidden_word):
    print('already guessed: [', end="")
    if len(guesses) == 0:
        print(']')
    else:
        for idx in range(len(guesses)):
            if idx == 0:
                print(guesses[idx - 1], end = "")
            else:
                print(guesses[idx - 1], end="")
        print(']')
    print('guesses remaining:', guesses_left)
    for ltrs in range (len(hidden_word)):
        if ltrs < (len(hidden_word)):
            print(hidden_word[ltrs], end = "")
    print()
    ltr_in = input('guess a letter: ')
    return ltr_in
#
def play_command_line(secret_word):
    print('In command_line, secret word = ', secret_word)
    hidden_word = []
    for idx in range(len(secret_word)):
        hidden_word.append('-')
    guesses = []
    guesses_left = 6
    word_string = ""
#
    while guesses_left > 0:
        word_string = make_hidden_secret(secret_word, guesses)
        success = won(word_string)
        if success:
            print('winner!')
            print(word_string)
            break
#
        ltr_in = print_and_prompt(guesses_left, guesses, word_string)
        print(ltr_in)
        in_list = already_guessed(ltr_in, guesses)
        if in_list is True:
            continue
#
        in_secret_word = letter_in_secret_word(ltr_in, secret_word)
        if in_secret_word:
            for idx in range(len(secret_word)):
                if secret_word[idx] == ltr_in:
                    hidden_word[idx] = ltr_in
        else:
            # draw carcus
            guesses_left = guesses_left - 1
#
    if guesses_left == 0:
        print('sorry, you did not guess the word.')
#

if __name__ == '__main__':
    words = get_words("words.txt")
    secret_word = get_random_word(words)
#
    answer = input('Do you want to play command line(c) or graphic version(g)? '
                   '(anything else to quit): ')
    if answer[0] == 'c':
        play_command_line(secret_word)
    elif answer[0] == 'g':
        play_graphics(secret_word)
#
    print('Finis!')
#
