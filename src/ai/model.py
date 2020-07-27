import torch
import torch.nn as nn
import torch.nn.functional as F

# Initial input size: 6x7
# After conv1: 4x5
# After conv2: 2x3

class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        # kernel
        self.conv1 = nn.Conv2d(1, 6, 3, stride=1) # 6 kernels of size 3x3 having depth 1
        self.conv2 = nn.Conv2d(6, 16, 3, stride=1) # 16 kernels of size 3x3 having depth 6
        self.fc1 = nn.Linear(16*2*3, 128) # 16 kernels with a 2x3 dimension
        self.fc2 = nn.Linear(128, 64) # input 128 neuroins, output 128 neurons
        self.fc3 = nn.Linear(64, 7) # input 128 neurons, output 7 neurons (7 slots in of the game)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features




def main():
    print("Model main.")

if __name__ == '__main__':
    main()