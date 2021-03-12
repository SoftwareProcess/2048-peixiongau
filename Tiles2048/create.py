from matplotlib.pyplot import grid
#from Tools.scripts.patchcheck import status
from random import random
def _create(userParms):
    #result = {'create': 'create stub'}
    result = {}
    result["grid"] = 0
    result["score"] = 0
    result["integrity"] = 0
    result["status"] = 0
    
    
    return result


def _generateGrid():
    left = 2
    result = ''
    for i in range(16):
        if left == 0:
            result += '0'
            continue
        if random() < 0.3:
            result += '2'
            left -= 1
        else:
            result += '0'
    return result
            