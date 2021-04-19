import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset, random_split
from torch.utils.tensorboard import SummaryWriter
import time
from collections import OrderedDict
from collections import namedtuple
from itertools import product
import torchvision
import torchvision.transforms as transforms

train_set = torchvision.datasets.FashionMNIST(root='./data', train=True,
                                              download=True, transform=transforms.Compose([transforms.ToTensor()]))

class Network(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=12, kernel_size=5)

        self.fc1 = nn.Linear(in_features=12 * 4 * 4, out_features=120)
        self.fc2 = nn.Linear(in_features=120, out_features=60)
        self.out = nn.Linear(in_features=60, out_features=10)

    def forward(self, t):
        t = t

        # (2) hidden conv layer
        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)

        # (3) hidden conv layer
        t = self.conv2(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)

        # (4) hidden linear layer
        t = t.reshape(-1, 12 * 4 * 4)
        t = self.fc1(t)
        t = F.relu(t)

        # (5) hidden linear layer
        t = self.fc2(t)
        t = F.relu(t)

        # (6) output layer
        t = self.out(t)
        # t = F.softmax(t, dim=1)

        return t

    def __repr__(self):
        return "Bunny Kitten"

def calculate_correct(out, labels):
    return torch.eq(out.argmax(dim=1), labels).sum().numpy()

class RunBuilder():
    @staticmethod
    def get_runs(params):

        Run = namedtuple('Run', params.keys())

        runs = []
        for v in product(*params.values()):
            runs.append(Run(*v))
        return runs

class RunManager():
    def __init__(self):

        self.epoch_count = 0
        self.epoch_loss = 0
        self.epoch_num_correct = 0
        self.epoch_start_time = None

        self.run_params = None
        self.run_count = 0
        self.run_data = []
        self.run_start_time = None

        self.network = None
        self.loader = None
        self.tb = None

    def begin_run(self, run, network, loader):
        self.run_start_time = time.time()
        self.run_params = run
        self.run_count += 1
        self.network = network
        self.loader = loader
        self.tb = SummaryWriter(comment=f'-{run}')
        characteristics, labels = next(iter(self.loader))

    def end_run(self):
        self.tb.close()
        self.epoch_count = 0

    def begin_epoch(self):
        self.epoch_start_time = time.time()
        self.epoch_count += 1
        self.epoch_loss = 0
        self.epoch_num_correct = 0

    def end_epoch(self):
        epoch_duration = time.time() - self.epoch_start_time
        run_duration = time.time() - self.run_start_time

        loss = self.epoch_loss / len(self.loader.dataset)
        accuracy = self.epoch_num_correct / len(self.loader.dataset)

        self.tb.add_scalar('Loss', loss, self.epoch_count)
        self.tb.add_scalar('Accuracy', accuracy, self.epoch_count)

    def _get_num_correct(self, preds, labels):
        return preds.argmax(dim=1).eq(labels).sum().item()

    def track_loss(self, loss, batch):
        self.epoch_loss += loss.item() * batch[0].shape[0]

    def track_num_correct(self, preds, labels):
        self.epoch_num_correct += self._get_num_correct(preds, labels)

    def inform(self, discrete_n):
        if self.epoch_count % discrete_n == 0:
            print(self.epoch_count, ' ', self.run_count)

params = OrderedDict(lr=[.01], batch_size=[10], number_epocs=[100])
m = RunManager()

for run in RunBuilder.get_runs(params):

    network = Network()
    loader = DataLoader(train_set, batch_size=run.batch_size, shuffle=True)
    optimizer = torch.optim.Adam(network.parameters(), lr=run.lr)
    m.begin_run(run, network, loader)

    for epoch in range(run.number_epocs):
        m.begin_epoch()
        for batch in loader:
            characteristics, labels = batch
            preds = network(characteristics)  # Pass Batch
            loss = F.cross_entropy(preds, labels)  # Calculate Loss
            optimizer.zero_grad()  # Zero Gradients
            loss.backward()  # Calculate Gradients
            optimizer.step()  # Update Weights
            m.track_loss(loss, batch)
            m.track_num_correct(preds, labels)
        m.inform(25)
        m.end_epoch()
    m.end_run()