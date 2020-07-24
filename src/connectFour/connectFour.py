import numpy as np
import random

class ConnectFour():
    def __init__(self):
        self.row = 6
        self.col = 7
        self.board = np.zeros((self.row, self.col))


    def printBoard(self):
        print(self.board)

    def reset(self):
        self.board = np.zeros((self.row, self.col))

    def isWin(self, player):
        # Check horizontal locations for win
        for c in range(self.col-3):
            for r in range(self.row):
                if self.board[r][c] == player.getNumber() and self.board[r][c+1] == player.getNumber() and self.board[r][c+2] == player.getNumber() and self.board[r][c+3] == player.getNumber():
                    return True

        # Check vertical locations for win
        for c in range(self.col):
            for r in range(self.row-3):
                if self.board[r][c] == player.getNumber() and self.board[r+1][c] == player.getNumber() and self.board[r+2][c] == player.getNumber() and self.board[r+3][c] == player.getNumber():
                    return True

        # Check positively sloped diaganols for win
        for c in range(self.col-3):
            for r in range(self.row-3):
                if self.board[r][c] == player.getNumber() and self.board[r+1][c+1] == player.getNumber() and self.board[r+2][c+2] == player.getNumber() and self.board[r+3][c+3] == player.getNumber():
                    return True

        # Check negatively sloped diaganols for win
        for c in range(self.col-3):
            for r in range(3, self.row):
                if self.board[r][c] == player.getNumber() and self.board[r-1][c+1] == player.getNumber() and self.board[r-2][c+2] == player.getNumber() and self.board[r-3][c+3] == player.getNumber():
                    return True


    def move(self, column, player):
        player.makeMove(column)

        if column < 0 or column >= self.col:
            raise ValueError('Invalid move was played')

        else:
            for i in range(0, self.row):
                for j in range(0, self.col):
                    if j == column:
                        # Top row
                        if i == 0:
                            # Column is already full
                            if self.board[i][j] != 0:
                                print("Invalid")
                                raise ValueError('Invalid move was played')
                        else:
                            # Bottom row
                            if i == self.row - 1:
                                if self.board[i][j] != 0:
                                    self.board[i-1][j] = player.getNumber()
                                    return True
                                else:
                                    self.board[i][j] = player.getNumber()
                                    return True
                            # Middle rows
                            elif self.board[i][j] != 0:
                                self.board[i-1][j] = player.getNumber()
                                return True

    def leftMost_algo(self, player):
        move = 0
        return self.move(move, player)

    def random_algo(self, player):
        move = random.randrange(0, self.col, 1)
        return self.move(move, player)

def main():
    print("ConnectFour main.")

if __name__ == '__main__':
    main()