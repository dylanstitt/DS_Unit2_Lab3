# Dylan Stitt
# Unit 2 Lab 3
# Tic Tac Toe

from TTT import *
import art, os, random

def validateInput(inp, mode):
    """Takes in user input and a 'mode' to validate the correct input"""

    # This validates the user input for selecting a space to put their token
    if mode == 'coord':
        letter, number = inp[0], inp[1]
        while letter not in ['a', 'b', 'c']:
            letter = input('Only enter letters A-C. Enter your letter again: ').lower()

        try:
            number = int(number)
            while number < 1 or number > 3:
                number = int(input('Only enter numbers 1-3. Enter your number again: ').lower())

        except ValueError:
            validateInput(inp, mode)

        return letter, number

    # This is use to validate the user picking their token
    else:
        while inp not in ['x', 'o']:
            inp = input('Only enter X or O. Enter your input: ').lower()
        return inp


def displayWinner(winner, board):
    """Calls the art from the art.py file to print the correct win message and the final board"""
    os.system('cls')
    if winner == 'X':
        print(art.x)
    if winner == 'O':
        print(art.o)
    else:
        print(art.tie)
    print(f'\n{board}')


def main():
    """Calls all other function and holds the main game loop"""
    game = TicTacToe()
    # Finish game loop and displaying the winner


if __name__ == '__main__':
    main()
