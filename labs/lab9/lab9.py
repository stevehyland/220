"""
Name: <Steve Hyland>
<ProgramName>.py
"""
#
def build_board():
    tt_list = []
    for idx in range(9):
        tt_list.append(idx + 1)
    print(tt_list)
    return tt_list
#
def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)
#
def is_legal(board, position):
    temp_str = str(board[position - 1])
    if temp_str.isnumeric():
        return True
    return False
#
def fill_spot(board, position, character):
    character = character.strip()
    character = character.lower()
    board[position - 1] = character
#
def winning_game(board):
# determine if we have a winner
    if board[0] == board[1] and board[0] == board[2]:
        return True
    elif board[0] == board[4] and board[0] == board[8]:
        return True
    elif board[0] == board[3] and board[0] == board[6]:
        return True
    elif board[1] == board[4] and board[1] == board[7]:
        return True
    elif board[2] == board[5] and board[2] == board[8]:
        return True
    elif board[3] == board[4] and board[3] == board[5]:
        return True
    elif board[6] == board[4] and board[6] == board[2]:
        return True
    elif board[6] == board[7] and board[6] == board[8]:
        return True
    return False
#
def game_over(board):
    game_won = winning_game(board)
    if (board.count('x') + board.count('o') == 9):
        return True
    if not game_won:
        for idx in range(len(board)):
            chr_in = chr(board[idx - 1])
            if chr_in.isnumeric():
                return False
        return True
#
def get_winner(board):
    game_won = winning_game(board)
    numx = board.count('x')
    numo = board.count('o')
    print(numx + numo)
    if game_won:
        if numx + numo == 9:
            return
        elif numo >= numx:
            return 'o'
        return 'x'
#
def play(board):
    game_won = winning_game(board)

    while game_won is False:
        print_board((board))
        position = eval(input('x\'s, choose a position:'))
        space_ok = is_legal(board, position)
        while not space_ok:
            position = eval(input('position occupied, try again:'))
            space_ok = is_legal(board, position)
        fill_spot(board, position, 'x')
        print_board(board)
        game_over = winning_game(board)
        if (board.count('x') + board.count('o') == 9 ):
            game_over = True
#
        if game_over == False:
            position = eval(input('o\'s, choose a position:'))
            space_ok = is_legal(board, position)
            while not space_ok:
                position = eval(input('position occupied, try again:'))
                space_ok = is_legal(board, position)
            fill_spot(board, position, 'o')
            print_board(board)
        game_won = winning_game(board)
        if board.count('x') + board.count('o') == 9:
            game_won  = True

    victor = get_winner(board)
    if victor == 'x':
        print('x\'s win!')
    elif victor == 'o':
            print('o\'s win')
    else: print('it is a tie.')

#
def main():

    print('Welcome to Tic Tac Toe.  You will be prompted to enter a square to enter ', end="")
    print('your letter - either x or o.')
    print('When a game is won you will be give a chance to play another game - enter "Y" or "y"')
    print('X goes first')
    print('              E N J O Y     ')
    go_nogo = input('Do you want to play TIC-TAC-TOE? ')
#
    while go_nogo[0] == 'y' or go_nogo[0] == 'Y':
        tt_list = build_board()
        play(tt_list)
        go_nogo = input('Do you want to play TIC-TAC-TOE again? ')
    print('Goodbye!')


if __name__ == '__main__':
    main()
#
