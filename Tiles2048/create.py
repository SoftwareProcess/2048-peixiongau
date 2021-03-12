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

def _generateIntegrity(grid, score):
    hasher = hashlib.sha256(bytes(grid, 'utf-8'))
    hasher.update(b'.')
    hasher.update(int2byte(score))
    return hasher.hexdigest()
            
