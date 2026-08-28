from TileInfo import TileInfo
from TileNeighbors import TileNeighbors
import helper
from sklearn.neighbors import NearestNeighbors

def setAllneighbors(tiles:list[TileInfo], returnCenterTile = False)-> list[TileInfo] | tuple[list[TileInfo], TileInfo]:
    neigh = NearestNeighbors(n_neighbors=6, algorithm='ball_tree').fit(centers)
    indices = neigh.kneighbors(centers, return_distance=False)

#Centers argument should be passed a list of 4 nearest neighbors NOT entire list of centers
def findNeighbor(tile: TileInfo, avgTileLen: int | float, nearestNeighbors : list[TileInfo]) -> TileNeighbors: 
    # exampleImg = image.copy()
    moePercent = .3
    neighbors = TileNeighbors()
    tileX = tile.center.x
    tileY = tile.center.y
    for adjtile in nearestNeighbors:
        otherX = adjtile.center.x
        otherY = adjtile.center.y
        minX, maxX = helper.addCI(otherX,avgTileLen, moePercent=moePercent) 
        minY, maxY = helper.addCI(otherY,avgTileLen,moePercent)
        staticXCheck = (minX < tileX < maxX)
        staticYCheck = (minY <tileY <maxY)
        #Check for up neighbor
        if( neighbors['up'] is None and staticXCheck and (minY - avgTileLen < tileY < maxY + avgTileLen) ):
            neighbors['up'] = adjtile
            # cv2.circle(exampleImg, (otherX,otherY), 20, (0,0,0), 25)

        #Check for down neighbor
        if(neighbors['down'] is None and staticXCheck and (minY + avgTileLen < tileY < maxY+avgTileLen)):
            neighbors['down'] = adjtile
            # cv2.circle(exampleImg, (otherX,otherY), 20, (0,0,0), 25)

        if(neighbors['left'] is None and staticYCheck and (minX - avgTileLen < tileX < maxX - avgTileLen)):
            neighbors['left'] = adjtile
            # cv2.circle(exampleImg, (otherX,otherY), 20, (0,0,0), 25)

        if(neighbors['right'] is None and staticYCheck and (minX + avgTileLen < tileX < maxX + avgTileLen)):
            neighbors['right'] = adjtile
            # cv2.circle(exampleImg, (otherX,otherY), 20, (0,0,0), 25)

    # cv2.circle(exampleImg,(tileX,tileY), 25, (250, 40,40),25)
    # plt.imshow(exampleImg)
    # plt.show()
    return neighbors