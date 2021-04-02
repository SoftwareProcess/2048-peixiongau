
import hashlib;



DIRECTION = ('up', 'down', 'left', 'right')
VALID_NUMS = ('0', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024')
global grid_parsed


# Finish the shift operation
def _shift(userParms):
    result = {'shift': 'shift stub'}
    # Check if we got valid parameters
    result = _check_parms(userParms)
    if "status" in result:   
        return result
    
    # The validation passed
    grid = userParms["grid"]
    direction = userParms["direction"]
    score = userParms["score"]
    # Operate the data
    grid = _operate(grid, direction)
    # Generate one numbers after operation(and get the score)
    score = _gen_tiles(grid)
    
    result["grid"] = grid
    result["score"] = score
    result["integrity"] = _gen_integrity(grid, score)
    # Check if user has won or lost, and generate the status
    result["status"] = _gen_status(grid, score)
    
    
    return result

# parse parameters
def _check_parms(userParms):
    result = {}
    
    msg = _check_missing(userParms)
    if "passed" not in msg:
        result["status"] = msg
        return result
    grid = userParms["grid"]
    (msg, grid) = _check_grid(grid)
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
        return "error: missing direction";
    if "integrity" not in userParms:
        return "error: missing integrity";
    
    return "passed"
    
def _check_grid(grid):
    grid_parsed = [];
    accum = '';
    temp = ''
    count = 0
    for num in grid:
        temp = accum + num
        for x in VALID_NUMS:
            if accum == '0':
                break;
            
            
            if temp in x:
                accum = temp
                break
            
            if x == '1024':
                msg = "error: invalid grid", None
                return msg
        
        if accum in VALID_NUMS:
            grid_parsed.append(accum)
            count += 1
            accum = ''
            temp = ''
    
    if count != 16:
        return "error: invalid grid", None
    
    if '0' not in grid_parsed:
        return "error: no shift possible", None
    return "passed", grid_parsed


    
def _check_score(score: str):
    scr = int(score)
    if scr % 2 == 0:
        return "passed"
    return "error: invalid score"

def _check_integrity(parms):
    data = parms['grid'] + '.' + parms['score']
    
    hasher = hashlib.sha256()
    
    hasher.update(data.encode())

    expected = hasher.hexdigest().upper()
    
    if parms['integrity'] == expected:
        return "passed"
    return "error: bad integrity value"

def _check_direction(direction):
    if direction in DIRECTION:
        return 'passed'
    return 'error: invalid direction'
        
        
    
    
    

def _operate(direction):
    grid = _parse_grid(direction)
    
    results = []
    # Calculation
    for sequence in grid:
        num = 0
        result = []
        for x in sequence:
            if x == 0:
                continue
            
            if num == 0:
                num = x
                continue
            
            if num == x:
                result.append(num * 2)
                num = 0
        
        results.append(result)
    
    # Putting results back to grid
    if direction == 'right' or direction == 'down':
        for i in range(3):
            for j in range(2):
                if j > len(results[i]):
                    continue
                grid[i][3-j] = results[i][j]
    else:
        for i in range(3):
            for j in range(2):
                if j > len(results[i]):
                    continue
                grid[i][j] = results[i][j]
    
    _update_grid(grid, direction)
    return 0

def _parse_grid(direction):
    grid = [['0','0','0','0'],['0','0','0','0'],['0','0','0','0'],['0','0','0','0']]
    print(grid_parsed)
    if direction == 'up' or direction == 'down':
        # rows and columns
        i = 0
        j = 0
        for i in range(4):
            for j in range(4):
                grid[j][i] = int(grid_parsed[i + j * 4])
    else:
        for i in range(4):
            for j in range(4):
                grid[i][j] = int(grid_parsed[i * 4 + j])
    
    return grid

def _update_grid(grid, direction):
    if direction == 'up' or direction == 'down':
        # rows and columns
        i = 0
        j = 0
        for i in range(4):
            for j in range(4):
                grid_parsed[i + j * 4] = str(grid[j][i])
    else:
        for i in range(4):
            for j in range(4):
                grid_parsed[i * 4 + j] = str(grid[i][j])
    
    if '2048' in grid_parsed:
        print("you win!")       #modiify later
    return grid_parsed


def _gen_tiles(grid):
    return 0

def _gen_integrity(grid, score):
    return 0

def _gen_status(grid, score):
    return 0