import numpy as np

from connectFour.connectFour import ConnectFour
from connectFour.player import Player


def main():
    try:
        player2 = Player(2)
        player1 = Player(1)
        env = ConnectFour()
        env.printBoard()
        env.makeMove(3, player1)
        env.printBoard()
        env.makeMove(2, player1)
        env.printBoard()
        env.makeMove(1, player1)
        env.printBoard()
        env.makeMove(0, player1)
        env.printBoard()

    except ValueError as error:
        print('Caught this error: ' + repr(error))
        raise


if __name__ == '__main__':
    main()