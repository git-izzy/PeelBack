from .TileInfo import TileInfo, Point
from .TileNeighbors import TileNeighbors
from .. import helper
from sklearn.neighbors import NearestNeighbors
import numpy as np

def setAllneighbors(tiles:list[TileInfo], avgTileLen, returnCenterTile = False)-> list[TileInfo] | tuple[list[TileInfo], TileInfo]:
    centers = np.asarray([ [tile.center.x,tile.center.y] for tile in tiles])
    npTiles = np.asarray(tiles)

    neigh = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(centers)
    indices = neigh.kneighbors(centers, return_distance=False)
    nearestNeighbors =  npTiles[indices]

    for neighbors in nearestNeighbors:
        neighbors = findNeighbor(neighbors[0],avgTileLen,neighbors)

    if returnCenterTile:
        #change to median?
        approxCenter = np.average(centers,axis=0)
        centNeigh = neigh.kneighbors([approxCenter], n_neighbors=1, return_distance=False)
        centerTile = tiles[centNeigh[0][0]]
        return tiles, centerTile
    else:
        return tiles



#NearestNeighbors argument should be passed a list of 5 nearest neighbors NOT entire list of centers
from Scananagrams.src.tiles.TileNeighbors import TileNeighbors

def findNeighbor(tile: TileInfo, avgTileLen: int | float, nearestNeighbors) -> TileNeighbors: 
    moePercent = .3
    neighbors = tile.tileDict
    tileX = tile.center.x
    tileY = tile.center.y

    for adjTile in nearestNeighbors:

        otherX = adjTile.center.x
        otherY = adjTile.center.y

        minX, maxX = helper.addCI(otherX, avgTileLen, moePercent) 
        minY, maxY = helper.addCI(otherY, avgTileLen, moePercent)

        staticXCheck = (minX < tileX < maxX)
        staticYCheck = (minY < tileY <maxY)

        if(neighbors['up'] is None and staticXCheck and (minY + avgTileLen < tileY < maxY+avgTileLen)):
            neighbors['up'] = adjTile
            # adjtile.tileDict['down'] = tile
        
        if( neighbors['down'] is None and staticXCheck and (minY - avgTileLen < tileY < maxY - avgTileLen) ):
            neighbors['down'] = adjTile
            # adjtile.tileDict['up'] = tile

        if(neighbors['left'] is None and staticYCheck and (minX + avgTileLen < tileX < maxX + avgTileLen)):
            neighbors['left'] = adjTile
            # adjtile.tileDict['right'] = tile

        if(neighbors['right'] is None and staticYCheck and (minX - avgTileLen < tileX < maxX - avgTileLen)):
            neighbors['right'] = adjTile
            # adjtile.tileDict['left']=tile

    return neighbors