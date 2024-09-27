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
                number = int(input('Only enter numbers 1-3. Enter your number again: '))

        except ValueError:
            validateInput(inp, mode)

        return letter, number-1

    # This is used to validate the user picking their token
    else:
        while inp not in ['x', 'o']:
            inp = input('Only enter X or O. Enter your input: ').lower()
        return inp.upper()


def displayWinner(winner, board):
    """Calls the art from the art.py file to print the correct win message and the final board"""
    os.system('cls')
    if winner.upper() == 'X':
        print(art.x)
    elif winner.upper() == 'O':
        print(art.o)
    else:
        print(art.tie)
    print(f'\n{board}')


def playAgain(inp):
    """Validating and asking the player if they would like to play again"""
    while inp not in ['y', 'n']:
        inp = input('Do you want to play again? (y/n): ').lower()

    if inp == 'y':
        return True
    else:
        os.system('cls')
        print('Thanks for playing!')
        return False


def main():
    """Calls all other function and holds the main game loop"""
    os.system('cls')
    player = validateInput(input('Enter X or O: ').lower(), 'token')
    playing = True
    usedSpaces = []

    game = TicTacToe()
    while playing:
        os.system('cls')
        print(game)

        currentPlayer = game.getCurrentPlayer()
        if currentPlayer == player:
            x, y = validateInput(input('Enter the space you would like to place your token at: '), 'coord')
            while (x, y) in usedSpaces:
                x, y = validateInput(input('Enter an empty space. Try again: '), 'coord')

        else:
            x, y, = random.choice(['a', 'b', 'c']), random.randint(0, 2)
            while (x, y) in usedSpaces:
                x, y, = random.choice(['a', 'b', 'c']), random.randint(0, 2)

        usedSpaces.append((x, y))
        winner = game.placeToken(x, y)

        if winner != False:
            displayWinner(winner, game)
            again = input('\n\nDo you want to play again? (y/n): ').lower()

            if playAgain(again):
                os.system('cls')
                player = validateInput(input('Enter X or O: ').lower(), 'token')
                playing = True
                usedSpaces = []

                game = TicTacToe()
            else:
                exit()

if __name__ == '__main__':
    main()
