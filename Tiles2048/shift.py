



valid_nums = ('0', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024')



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

def _check_parms(userParms):
    result = {}
    
    msg = _check_missing(userParms)
    if "passed" not in msg:
        result["status"] = msg
        return result
    grid = userParms["grid"]
    msg = _check_grid(grid)
    if "passed" not in msg:
        result["status"] = msg
        return result
    
    score = userParms["score"]
    msg = _check_score(score)
    if "passed" not in msg:
        result["status"] = msg
        return result
    
    integrity = userParms["integrity"]
    msg = _check_integrity(integrity)
    if "passed" not in msg:
        result["status"] = msg
        return result
    
    direction = userParms["direction"]
    msg = _check_direction(direction)
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
    if "integrity" not in userParms:
        return "error: missing integrity";
    if "direction" not in userParms:
        return "error: missing direction";
    return "passed"
    
def _check_grid(grid):
    accum = '';
    temp = ''
    count = 0
    for num in grid:
        for x in grid:
            if accum == '0':
                break;
            
            temp = accum + num
            if temp in x:
                accum = temp
                continue
            
            if x == '1024':
                msg = "error: invalid grid"
                return msg
        
        if accum in valid_nums:
            count += 1
            accum = ''
            temp = ''
    
    if count != 16:
        return "error: invalid grid"
    
    return "passed"


    
def _check_score(score):
    return '0'

def _check_integrity(integrity):
    return '0'

def _check_direction(direction):
    return '0'
        
        
    
    
    

def _operate(grid, direction):
    return 0

def _gen_tiles(grid):
    return 0

def _gen_integrity(grid, score):
    return 0

def _gen_status(grid, score):
    return 0