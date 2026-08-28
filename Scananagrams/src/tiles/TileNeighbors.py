from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .TileInfo import TileInfo

class TileNeighbors():

    def __init__(self,tileDict : dict = None, up=None, right=None, down=None, left=None):
        if (tileDict is None):
            self.neighbors = {"up":up, "right":right, "down":down, "left":left}
        else:
            self.neighbors = tileDict

    def findTargetKey(self,key):
        if (key == "up" or key == "u" or key == "U" or key == "UP" or key == 0):
            return "up"
                
        if (key =="right" or key =="r" or key =="R" or key == "RIGHT" or key ==1):
            return "right"

        if (key =="down" or key =="d" or key == "DOWN" or key == "D" or key == 2):
            return "down"

        if (key == "left" or key =="l" or key == "L" or key == "LEFT" or key ==3):
            return "left"

        raise KeyError()

    def removeNeighbor(self,key):
        self[key] = None    

    def __getitem__(self, key) ->'TileInfo':
        target = self.neighbors[ self.findTargetKey(key) ]
        return target

    def __setitem__(self, key, value):
        targetKey = self.findTargetKey(key)
        self.neighbors[targetKey] = value

    def __str__(self):
        return f"Neighbors: 'up': {self.neighbors['up']}, \'down\': {self.neighbors['down']} \'left\': {self.neighbors['left']}, \'right\': {self.neighbors['right']}"

    

    

    
    

    
