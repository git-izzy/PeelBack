import numpy as np
import cv2
from cv2.typing import MatLike

class Contour():
    def __init__(self, contour : MatLike):
        self.contour = contour
        x,y,w,h = cv2.boundingRect(contour)
        self.boundingRect = {"x":x, "y":y, "w":w, "h":h}

    def getContour(self):
        """Gives the core contour object - **use only when necessary**"""
        return self.contour

    def getCroppedContourFromImage(self, image : MatLike, padding=0)->MatLike:
        x,y = self.getBoundingCorner()
        h= self.getHeight()
        w = self.getWidth()
        croppedImage = image[y-padding:y+h+padding, x-padding:x+w+padding]
        return croppedImage

    def getHeight(self)->int:
        """
        Returns height of contour's bounding rect
        """
        return self.boundingRect['h']
    
    def getWidth(self)->int:
        """
        Returns width of contour's bounding rect
        """
        return self.boundingRect['w']

    def getBoundingCorner(self, cornerCode= 'TL') -> tuple[int,int]:
        """
        Returns a corner of the bounding box. \n
        cornerCode parameter accepts values of TL, TR, BL, BR\n
        T | B - Top or Bottom\n
        R | L - Left Or Right\n
        Default response is to give top left corner

        :return: x coordinate, y coordinate
        """
        x,y = self.boundingRect['x'], self.boundingRect['y']

        if cornerCode[0]=='B':
            y+= self.boundingRect['h']
        if cornerCode[1]=='R':
            x+= self.boundingRect['w']
    
        return x,y

    def getSolidity(self)->float:
        hull = cv2.convexHull(self.contour)
        hull_area = cv2.contourArea(hull)
        if hull_area > 0: # Avoid division by zero
            solidity = self.getContourArea() / hull_area
        else:
            solidity = 0
        return solidity

    def getContourArea(self)->float:
        "Return the area of the contour - calls `cv2.contourArea`"
        return cv2.contourArea(self.contour)

    def getBoundingArea(self)->int:
        """
        Returns the area of the contours bounding box
        """
        height = self.getHeight()
        width = self.getWidth()
        return (width *height)

    def getAspectRatio(self)->float:
        """
        :return: bounding rect width divided bounding rect height
        """
        height = self.getHeight()
        width = self.getWidth()
        return width/height 

    def getTopLeftCorner(self)->tuple[int,int]:
        """
        Return the top left corrdinate for the bounding box of the contour
        """
        return self.getBoundingCorner('TL')

    def getTopRightCorner(self)->tuple[int,int]:
        """
        Return the top right corrdinate for the bounding box of the contour
        """
        return self.getBoundingCorner('TR')

    def getBottomRightCorner(self)->tuple[int,int]:
        """
        Return the bottom right corrdinate for the bounding box of the contour
        """
        return self.getBoundingCorner('BR')

    def getBottomLeftCorner(self)->tuple[int,int]:
        """
        Return the bottom left corrdinate for the bounding box of the contour
        """
        return self.getBoundingCorner('BL')