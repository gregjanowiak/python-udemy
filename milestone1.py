from os import system
import random

def play():
    while True:
        #reset board
        master_board = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' goes first!')

        start_game = input("Are you ready to play? (Yes/No) ")

        if start_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                #player 1's turn
                print_board(master_board)
                position = player_choice(master_board)
                place_marker(master_board, player1_marker, position)

                if win_checker(master_board,player1_marker):
                    print_board(master_board)
                    print("Congrats, you won the game!")
                    game_on = False

                else:
                    if full_board_check(master_board):
                        print_board(master_board)
                        print("The game is a tie.")
                        break
                    else:
                        turn = 'Player 2'
            else:
                #player 2's turn
                print_board(master_board)
                position = player_choice(master_board)
                place_marker(master_board, player2_marker, position)

                if win_checker(master_board,player2_marker):
                    print_board(master_board)
                    print("Congrats, you won the game!")
                    game_on = False

                else:
                    if full_board_check(master_board):
                        print_board(master_board)
                        print("The game is a tie.")
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break
    print("Thanks for playing!")

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
    return board[position] == ' '

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

def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

play()
