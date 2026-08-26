import torch
from torch import optim, nn
from torch.utils.data import DataLoader


from OCRModel import SingleCharOCR


class CNNTrainer():
    def __init__(self, net: SingleCharOCR, lossFunc, optimizer:optim):
        self.net = net
        self.lossFunc = lossFunc
        self.optim = optimizer

    def runEpoch(self, dataloader:DataLoader, reportInterval = 50):
        totalLoss = 0.0
        for i, data in enumerate(dataloader,0):
            inputs, labels = data
            self.optim.zero_grad()

            outputs = self.net(inputs)
            loss = self.lossFunc(outputs,labels)
            loss.backward()
            self.optim.step()
            totalLoss += loss.item()

            if i % reportInterval == reportInterval-1: 
                print(f'    {i+1} samples - Avg loss: {totalLoss/i} ')

        return totalLoss

    def train(self, epochs:int, dataLoader:DataLoader):
        for epoch in range(epochs):
            print(f'Epoch {epoch+1}:')
            self.runEpoch(dataLoader)

    def test(self, testLoader:DataLoader):
        correct = 0
        total = 0
        with torch.no_grad():
            for data in testLoader:
                images, labels = data
                outputs = self.net(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        print(f'Total: {total}\nCorrect: {correct}\nAccuracy: {round(100*(correct/total),2)}')


