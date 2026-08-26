
#Centers argument should be passed a list of 4 nearest neighbors NOT entire list of centers
def findNeighbor(tile, avgTileLen, centers):
    # exampleImg = image.copy()
    moe = avgTileLen * .3
    neighbors = {'up':None,'down':None,'left':None,'right':None}
    tileX = tile[0]
    tileY = tile[1]
    for point in centers:
        otherX = point[0]
        otherY = point[1]
        staticXCheck = (otherX-moe < tileX < otherX+moe)
        staticYCheck = (otherY-moe <tileY<otherY+moe)
        #Check for up neighbor
        if( neighbors['up'] is None and staticXCheck and (otherY - avgTileLen - moe < tileY < otherY - avgTileLen + moe) ):
            neighbors['up'] = point
            # cv2.circle(exampleImg, (otherX,otherY), 20, (0,0,0), 25)

        #Check for down neighbor
        if(neighbors['down'] is None and staticXCheck and (otherY+avgTileLen-moe < tileY < otherY+avgTileLen+moe)):
            neighbors['down'] = point
            # cv2.circle(exampleImg, (otherX,otherY), 20, (0,0,0), 25)

        if(neighbors['left'] is None and staticYCheck and (otherX-avgTileLen-moe < tileX < otherX-avgTileLen+moe)):
            neighbors['left'] = point
            # cv2.circle(exampleImg, (otherX,otherY), 20, (0,0,0), 25)

        if(neighbors['right'] is None and staticYCheck and (otherX+avgTileLen-moe < tileX < otherX+avgTileLen+moe)):
            neighbors['right'] = point
            # cv2.circle(exampleImg, (otherX,otherY), 20, (0,0,0), 25)

    # cv2.circle(exampleImg,(tileX,tileY), 25, (250, 40,40),25)
    # plt.imshow(exampleImg)
    # plt.show()
    return neighbors