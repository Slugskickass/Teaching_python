import torch
import torch.nn as nn
import torch.nn.functional as F

class Network(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=12, kernel_size=5)

        self.fc1 = nn.Linear(in_features=12*4*4, out_features=120)
        self.fc2 = nn.Linear(in_features=120, out_features=60)
        self.out = nn.Linear(in_features=60, out_features=10)

    def forward(self, t):
        # implement the forward pass
        t = t

        # (2) hidden conv layer
        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)

        return t

network = Network()
print(network)
my_data = [[1, 2, 3, 1, 2, 3],
            [4, 5, 6, 4, 5, 6],
            [7, 8, 9, 7, 8, 9],
           [1, 2, 3, 1, 2, 3],
           [4, 5, 6, 4, 5, 6],
           [7, 8, 9, 7, 8, 9]]

images = torch.tensor(my_data, dtype=torch.float32).unsqueeze(dim=0).unsqueeze(dim=0)
print(images.shape)
preds = network(images)
print(preds.shape)