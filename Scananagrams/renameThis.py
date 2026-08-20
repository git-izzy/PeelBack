#Contains starting 

from ultralytics import RTDETR
import numpy as np
import cv2
import matplotlib.pyplot as plt

"""Actual training of model"""
# model = RTDETR("rtdetr-l.pt")
# model.info()
# results = model.train(data='./Scananagrams.yolov8', epochs = 50, imgsz=640)

"""Make everything a class? Maybe a static class"""
#Using trained parameters in best.pt

class CHANGE_CLASSNAME():

    myModel = RTDETR('./best.pt')
            
    #Change this functions name - or wrap it into __init__
    @staticmethod
    def getResult( imagePath):
        result = myModel.predict(imagePath)
        boxes = result[0].boxes.xyxy.cpu().numpy()


    def getCenters(self, boxes):

        self.centers = []
        self.avgTileLen = 0
        for box in boxes:
            x1,y1,x2,y2 = map(int,box)
            xAvg = (x1+x2)//2
            yAvg = (y1+y2)//2
            self.centers.append([xAvg,yAvg])
            self.avgTileLen += x2-x1
            self.avgTileLen += y2-y1
        avgTileLen/= len(self.boxes)*2