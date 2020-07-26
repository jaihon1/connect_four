import numpy as np

from connectFour.connectFour import ConnectFour
from connectFour.player import Player


def main():
    try:
        player2 = Player(2)
        player1 = Player(1)
        env = ConnectFour()
        env.run(player1, player2)


    except ValueError as error:
        print('Caught this error: ' + repr(error))
        raise


if __name__ == '__main__':
    main()