import numpy as np
import torch

from connectFour.connectFour import ConnectFour
from connectFour.player import Player

from ai.model import NeuralNet


def main():
    try:
        player2 = Player(2)
        player1 = Player(1)
        env = ConnectFour()
        # env.run(player1, player2)

        model = NeuralNet()
        params = list(model.parameters())
        print(model)

        x = torch.randn(1, 1, 6, 7)
        out = model(x)
        print(out)


    except ValueError as error:
        print('Caught this error: ' + repr(error))
        raise


if __name__ == '__main__':
    main()