import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np

import torchvision
import torchvision.transforms as transforms

import matplotlib.pyplot as plt

train_set = torchvision.datasets.FashionMNIST(
    root='./data'
    ,train=True
    ,download=True
    ,transform=transforms.Compose([
        transforms.ToTensor()
    ])
)

display_loader = torch.utils.data.DataLoader(train_set, batch_size=16)
batch = next(iter(display_loader))
images, labels = batch

grid = torchvision.utils.make_grid(images, nrow=10)
plt.figure(figsize=(15, 15))
plt.imshow(np.transpose(grid, (1, 2, 0)))
plt.show()

for I in range(16):
    plt.subplot(4, 4, I+1)
    plt.imshow(images[I].squeeze())
plt.show()
