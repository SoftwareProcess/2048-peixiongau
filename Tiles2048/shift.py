from random import random
import hashlib;
from pickle import NONE




DIRECTION = ('up', 'down', 'left', 'right')
VALID_NUMS = ('0', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024')
global grid_parsed


# Finish the shift operation
def _shift(userParms):
    
    if 'direction' not in userParms:
        userParms['direction'] = 'down'
    if userParms['direction'] == '':
        userParms['direction'] = 'down'
    
    # Check if we got valid parameters
    result = _check_parms(userParms)
    if "status" in result:   
        return result
    
    # The validation passed
    grid = userParms["grid"]
    direction = userParms["direction"]
    old_score = userParms["score"]
    
    grid_parsed = _check_grid(grid)[1]
    # Operate the data
    (grid, score, status) = _operate(grid_parsed, direction)
    # Generate one numbers after operation(and get the score)
    score += int(old_score)
    
    result["grid"] = grid
    result["score"] = str(score)
    result["integrity"] = _gen_integrity(grid, score)
    # Check if user has won or lost, and generate the status
    result["status"] = status
    
    
    return result

# parse parameters
def _check_parms(userParms):
    result = {}
    
    msg = _check_missing(userParms)
    if "passed" not in msg:
        result["status"] = msg
        return result
    grid = userParms["grid"]
    msg = _check_grid(grid)[0]
    if "passed" not in msg:
        result["status"] = msg
        return result
    
    score = userParms["score"]
    msg = _check_score(score)
    if "passed" not in msg:
        result["status"] = msg
        return result
    
    
    direction = userParms["direction"]
    msg = _check_direction(direction)
    if "passed" not in msg:
        result["status"] = msg
        return result
    
    #integrity = userParms["integrity"]
    msg = _check_integrity(userParms)
    if "passed" not in msg:
        result["status"] = msg
        return result
    
    return result

# Check if there are any missing parameters
def _check_missing(userParms):
    if "grid" not in userParms:
        return "error: missing grid"
    if "score" not in userParms:
        return "error: missing score";
    if "direction" not in userParms:
        userParms['direction'] = 'down'
        #return "error: missing direction";
    if "integrity" not in userParms:
        return "error: missing integrity";
    
    return "passed"
    
def _check_grid(grid):
    grid_parsed = [];
    #pos = 0
    #accum = '';
    temp = ''
    #buffer:str  '''A buffer for part of a number to parse'''
    count = 0
    for i in range(len(grid)):
        temp += grid[i]
        
        for x in VALID_NUMS:
            if x.startswith(temp):
                #pos = i
                break
            # Not possible to be in valids with one more char
            if x == '1024':
                temp = temp[:-1];
                if temp == '':
                    return "error: invalid grid" + temp + grid[i], None
                else:
                    grid_parsed.append(temp)
                    count += 1
                    temp = grid[i]
            
        
    
    if count != 16:
        return "error: invalid grid" + count, None
    
    ''' Modification needed '''
    if '0' not in grid_parsed:
        if _check_lose(grid_parsed) == 'lose': 
            return "error: no shift possible", None
    return "passed", grid_parsed


    
def _check_score(score: str):
    try:
        scr = int(score)
    except:
        return 'error: invalid score'
    if scr < 0:
        return 'error: invalid score'
    if scr % 2 == 0:
        return "passed"
    return "error: invalid score"

def _check_integrity(parms):
    data = parms['grid'] + '.' + parms['score']
    
    hasher = hashlib.sha256()
    
    hasher.update(data.encode())

    expected = hasher.hexdigest().upper()
    #print(expected)
    if parms['integrity'] == expected:
        return "passed"
    return "error: bad integrity value"

def _check_direction(direction):
    if direction.lower() in DIRECTION:
        return 'passed'
    return 'error: invalid direction'
        
        
    
    
    
# make the operation and return the new grid
def _operate(gridIn, direction):
    grid = _parse_grid(gridIn, direction)
    score = 0
    # Calculation
    for i in range(4):
        prev = 0
        for j in range(4):
            if grid[i][j] == 0:
                continue
            
            if prev == 0:
                prev = grid[i][j]
                continue
            
            if prev == grid[i][j]:
                grid[i][j] *= 2

                x = j-1
                while grid[i][x] != prev:
                    x -= 1
                grid[i][x] = 0
                
                score += prev * 2
                prev = 0
                
                continue
            
            
            prev = grid[i][j]
            
        
    print(grid, 'in operate')
    if direction == 'right' or direction == 'down':
        for i in range(4):
            for j in range(4):
                if j == 0:
                    continue
                if grid[i][j-1] == 0:
                    continue
                if grid[i][j] == 0:
                    grid = _change_pos(grid, i, j, direction)
    else:
        for i in range(4):
            for j in range(3, -1, -1):
                if j == 3:
                    continue
                if grid[i][j+1] == 0:
                    continue
                if grid[i][j] == 0:
                    grid = _change_pos(grid, i, j, direction)

    grid = _update_grid(grid, direction)
    (grid, status) = _gen_tiles(grid)
    result = ''
    for num in grid:
        result += str(num)
    return result, score, status

def _change_pos(grid, i, j, dirc):
    if dirc == 'right' or dirc == 'down':
        if j == 0 or grid[i][j-1] == 0:
            return grid
        if grid[i][j] == 0:
            grid[i][j] = grid[i][j-1]
            grid[i][j-1] = 0
            grid = _change_pos(grid, i, j-1, dirc)
            
    else:
        if j == 3 or grid[i][j+1] == 0:
            return grid
        if grid[i][j] == 0:
            grid[i][j] = grid[i][j+1]
            grid[i][j+1] = 0
            grid = _change_pos(grid, i, j+1, dirc)
    
    return grid
        
def _parse_grid(gridIn, direction):
    grid = [['0','0','0','0'],['0','0','0','0'],['0','0','0','0'],['0','0','0','0']]
    #print(gridIn, ' in parse_grid()')
    if direction == 'up' or direction == 'down':
        # rows and columns
        i = 0
        j = 0
        for i in range(4):
            for j in range(4):
                grid[i][j] = int(gridIn[i + j * 4])
    else:
        for i in range(4):
            for j in range(4):
                grid[i][j] = int(gridIn[i * 4 + j])
    
    return grid

def _update_grid(grid_calced, direction):
    grid_original= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(grid_calced, ' in update_grid()')
    if direction == 'up' or direction == 'down':
        # rows and columns
        i = 0
        j = 0
        for i in range(4):
            for j in range(4):
                grid_original[i + j * 4] = str(grid_calced[i][j])
    else:
        for i in range(4):
            for j in range(4):
                print("i", i, "j", j)
                grid_original[i * 4 + j] = str(grid_calced[i][j])
    
    
                
    if '2048' in grid_original:
        print("you win!")       
    return grid_original

# Calculate score and Generate tiles
def _gen_tiles(grid):
    
    #score = 0
    left = 1
    odds = 0.2
    #for num in grid:
    #    score += int(num)
    
    if '2048' in grid:
        return grid, 'win'
    
    while left > 0:
        if grid.count('0') == 0:
            ''' Modification may be needed'''
            return grid,'lose'
        for i in range(16):
            if left == 0:
                break
            if grid[i] == '0':
                if random() < odds:
                    if random() < 0.1:
                        grid[i] = '2'
                    else:
                        grid[i] = '4'
                    left -= 1
    ''' modification may be needed '''
    if grid.count('0') == 0:
        return grid, _check_lose(grid)
    return grid,'ok'

def _gen_integrity(grid, score):
    data = grid + '.' + str(score)
    
    hasher = hashlib.sha256()
    
    hasher.update(data.encode())

    return hasher.hexdigest().upper()

# @param gridIn a full grid
def _check_lose(gridIn:list) -> str:
    num : str
    #dis : int
    for i in range(16):
        num = gridIn[i]
        #if num == '0':
        #    continue
        print(_get_adj(i))
        for x in _get_adj(i):
            print("x is: ",x)
            #if gridIn[x] == '0':
            #    dis = i - x
            #    x = x - dis
            if gridIn[x] == num:
                return 'ok';
            ''''''
        ''''''
    ''' No solution found'''
    return 'lose'
''' get adjacent coordinates'''
def _get_adj(pos)-> tuple:
    adjs = []
    #check if it's at the upper bound
    if pos > 3:
        adjs.append(pos - 4)
    if pos < 12:
        adjs.append(pos + 4)
    if pos % 4 != 0:
        adjs.append(pos - 1)
    if pos % 4 != 3:
        adjs.append(pos + 1)
        
    
    return tuple(adjs)