import numpy as np

from connectFour.connectFour import ConnectFour
from connectFour.player import Player


def main():
    try:
        player2 = Player('Obi-Wan')
        player1 = Player('Anakin')
        env = ConnectFour(player1, player2)
        env.printBoard()
        env.makeMove(3)
        env.printBoard()

    except ValueError as error:
        print('Caught this error: ' + repr(error))
        raise


if __name__ == '__main__':
    main()