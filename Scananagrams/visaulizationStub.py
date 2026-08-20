import numpy as np

def visualizeBoard(boardCenters, avgTileLen):

    centersAdj = normalizeCenters(boardCenters, avgTileLen)
    board = np.zeros(getBoardDimensions(centersAdj))

    for x in centersAdj:
        x1 = int(x[0])
        y1 = int(x[1])
        board[y1,x1]=1

    for row in board:
        toPrint =''
        for col in row:
            toPrint+=str(int(col))
        print(toPrint)

def normalizeCenters(boardCenters, avgTileLen):
    centersAdj = boardCenters.copy()
    centersAdj = centersAdj//avgTileLen
    farLeft = centersAdj[np.argmin(centersAdj[:,0])][0]
    farTop = centersAdj[np.argmin(centersAdj[:,1])][1]
    centersAdj[:,0] -=farLeft
    centersAdj[:,1]-= farTop 
    return centersAdj

def getBoardDimensions(normalizedCenters):
    width = normalizedCenters[np.argmax(normalizeCenters[:,0])][0]
    height = normalizedCenters[np.argmax(normalizeCenters[:,1])][1]
    return (width,height)