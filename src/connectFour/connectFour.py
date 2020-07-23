import numpy as np

class ConnectFour():
    def __init__(self, player1, player2):
        self.row = 6
        self.col = 7
        self.player1 = player1
        self.player2 = player2

        self.board = np.zeros((self.row, self.col))


    def printBoard(self):
        print(self.board)


    def makeMove(self, column):
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
                                    self.board[i-1][j] = 1
                                    return True
                                else:
                                    self.board[i][j] = 1
                                    return True
                            # Middle rows
                            elif self.board[i][j] != 0:
                                self.board[i-1][j] = 1
                                return True


def main():
    print("ConnectFour main.")

if __name__ == '__main__':
    main()