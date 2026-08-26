from torch import optim, nn

import torch.nn.functional as F
from torchvision.datasets import VisionDataset
import cv2
from PIL import Image
import numpy as np

class SingleCharOCR(nn.Module):
    def __init__(self):
        super(SingleCharOCR,self).__init__()

        kernelOneSize =3
        kernelTwoSize = 3

        out1 =6
        out2 = 16

        self.conv1 = nn.Conv2d(in_channels=3, out_channels= out1, kernel_size= kernelOneSize)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(in_channels= out1, out_channels= out2, kernel_size= kernelTwoSize)
        self.dense1 = nn.Linear(in_features= out2*kernelTwoSize*kernelTwoSize, out_features=120)
        self.dense2 = nn.Linear(in_features=120,out_features=84)
        self.dense3 = nn.Linear(in_features=84, out_features=26)
        

    def forward(self,imgs):
        conv1Out = self.conv1(imgs)
        conv2In = self.pool( F.relu(conv1Out) )
        conv2Out = self.conv2(conv2In)
        dense1In = self.pool( F.relu(conv2Out) )
        dense1In = dense1In.view(-1, 16*3*3) #Currently hardcoded
        dense1Out = F.relu( self.dense1(dense1In) )
        dense2Out = F.relu( self.dense2(dense1Out) )
        dense3Out = self.dense3(dense2Out)
        return dense3Out

class ImageDataset(VisionDataset):

    def __init__(self, imgs, transform = None):
        """
        imgs accepts a list of slices from a cv2 MatLike 
        """
        super().__init__(root=None, transform=transform)
        self.transform = transform
        self.imgs = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in imgs]

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, index):
        img = Image.fromarray(self.imgs[index].astype('uint8'))
        if self.transform:
            img = self.transform(img)
        return img

