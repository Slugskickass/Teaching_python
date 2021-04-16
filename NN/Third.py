import torch

t = torch.tensor([
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]
], dtype=torch.float32)

print(t)

print(t.reshape([1, 12]))

print(t.reshape([2, 6]))

print(t.reshape([3, 4]))

#print(t.reshape([12, 1]))


print(t.reshape([1, 12]).squeeze().shape)

print(t.reshape([1, 12]).unsqueeze(dim=0).unsqueeze(dim=0).shape)