from Scananagrams.src.TileNeighbors import TileNeighbors

class Center():
    def __init__(self,x,y):
        self.x=x
        self.y = y

class TileInfo():
    def __init__(self, center:Center, letter:str):
        self.center = center
        self.letter=letter
        self.tileDict = TileNeighbors()

    def setNeighbors(self, tileDict:TileNeighbors):
        self.tileDict=tileDict