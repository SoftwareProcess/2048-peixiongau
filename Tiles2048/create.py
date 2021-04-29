#from Tools.scripts.patchcheck import status
from random import random
import hashlib
from pip._vendor.six import int2byte


def _create(userParms):
    #result = {'create': 'create stub'}
    result = {}
    result["grid"] = _generateGrid()
    result["score"] = 0
    result['integrity'] = _generateIntegrity(result['grid'], 0)
    result['status'] = 'ok'
    
    
    return result


def _generateGrid():
    odds = 0.15
    left = 2
    result = ''
    for i in range(16):
        if left == 0:
            result += '0'
            continue
        if random() < odds: # + i * odds:
            result += '2'
            left -= 1
        else:
            if i >= 13:
                odds = 2
            result += '0'
    return result

def _generateIntegrity(grid, score):
    data = grid + '.' + str(score)
    
    hasher = hashlib.sha256()
    
    hasher.update(data.encode())

    return hasher.hexdigest().upper()
            
