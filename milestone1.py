from os import system
import random

def play():
    while True:
        #reset board
        board = [' '] * 10
        

def replay():
    return input('Do you want to play again? (Yes/No): ').lower().startswith('y')

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9): '))

    return position

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def space_check(board,position):
    return board[position] == ''

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def win_checker(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or#top
    (board[4] == board[5] == board[6] == marker) or#across middle
    (board[7] == board[8] == board[9] == marker) or#bottom
    (board[1] == board[5] == board[9] == marker) or#diagonal from top left
    (board[3] == board[5] == board[7] == marker) or#diagonal from top right
    (board[1] == board[4] == board[7] == marker) or#left side
    (board[2] == board[5] == board[8] == marker) or#middle down
    (board[3] == board[6] == board[9] == marker))#right side

def place_marker(board,marker,space):
    board[space] = marker

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Enter your marker (X or O): ").upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def print_board():

    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

play()
