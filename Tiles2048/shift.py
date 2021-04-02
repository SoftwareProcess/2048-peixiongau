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
    result = {"status": "stub"}
    return result

def _operate(grid, direction):
    return 0

def _gen_tiles(grid):
    return 0

def _gen_integrity(grid, score):
    return 0

def _gen_status(grid, score):
    return 0