import numpy as np


def percentCI(center:int | float, moePercent: float):
    """
    Returns min, max of a confidence interval of the format (center*(1-moePercent), center*(1+morePercent)) 
    
    :param int | float center: The center of the confidence interval
    :param float moePercent: The margin of error, defined as a percent increase of the center
    :return min,max: minimum and maximum of confidence interval 
    """
    low = center * (1-moePercent)
    high = center * (1+moePercent)
    return low,high

def addCI(center: int | float, moe: int | float, percent: float = 1.0):
    """
    Returns min,max of confidence interval of the format (center - moe, center + moe)
        If percent is given then the confidence interval takes the form (center - (moe * percent), center + (moe * percent))

    
    """
    low = center - ( moe* percent)
    high = center + (moe*percent)
    return low,high


def findNewAvgTileLen(boxes:np.ndarray):
    z = np.average(boxes[:,2]-boxes[:,0])
    y = np.average(boxes[:,3]-boxes[:,1])
    newAvg = (y+z)/2
    return newAvg