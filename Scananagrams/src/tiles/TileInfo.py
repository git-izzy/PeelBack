from .TileNeighbors import TileNeighbors
from ..helper import Point

class TileInfo():
    def __init__(self, id:int, center:Point, letter:str):
        self.id=id
        self.center = center
        self.letter=letter
        self.tileDict = TileNeighbors()

    def setNeighbors(self, tileDict:TileNeighbors):
        self.tileDict=tileDict

    def __str__(self):
        stringRep = f'Tile: {self.letter} Position: {self.center}'
        return stringRep

    