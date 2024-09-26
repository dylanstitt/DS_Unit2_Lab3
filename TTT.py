from random import choice

class TicTacToe:
    """TicTacToe Class"""

    def __init__(self):
        """Initialize the board, current token, and the A-C -> 0-2 translations"""
        self.__board = [['@ ' for i in range(3)] for i in range(3)]
        self.__turn = choice(['X', 'O'])
        self.__translations = {'a': 0, 'b': 1, 'c': 2}


    def __str__(self):
        """Displays the board nicely"""
        str = '  A B C\n'
        for i in range(3):
            str += f'{i+1} '
            for j in range(3):
                str += self.__board[i][j]
            str += '\n'
        return str


    def __checkWin(self, token):
        """Checks the horizontal, vertical, and diagonal spaces for the same token 3 in a row and return the token that wins, 'Draw' if it is a tie, and False if neither"""
        horizontal = [[self.__board[i][j] for j in range(3)] for i in range(3)]
        vertical = [[self.__board[j][i] for j in range(3)] for i in range(3)]

        hCounts = [horizontal[i].count(token + ' ') for i in range(3)]
        vCounts = [vertical[i].count(token+' ') for i in range(3)]

        if sum([self.__board[i].count('@ ') for i in range(3)]) == 0:
            return 'Draw'
        elif (self.__board[0][0] == self.__board[1][1] == self.__board[2][2]) or self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
            return token
        elif 3 in hCounts or 3 in vCounts:
            return token
        return False


    def placeToken(self, x, y):
        """Checks the make sure that the current space is empty, places the player token if it is, and then checks for a winner, returns it, and changes the token"""
        if self.__board[y][self.__translations[x]] == '@ ':
            self.__board[y][self.__translations[x]] = self.__turn+' '
        else:
            return False

        winner = self.isWinner(self.__turn)
        self.__turn = 'X' if self.__turn == 'O' else 'O'
        return winner


    def isWinner(self, token):
        """Calls the self.__checkWin() function to determine if the token is winner and returns it for the self.placeToken() to use"""
        return self.__checkWin(token)
