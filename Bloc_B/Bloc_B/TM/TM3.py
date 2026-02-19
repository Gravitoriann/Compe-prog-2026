## This is the template for TM3, full problem in the rulebook ##

def solve(directions: str):
    """
    Find the direction of the loop line

    Parameters:
        directions list[str]: Sequence of directions (N,E,S,W) that form the loop line
        
    Returns:
        str: Either "CW" if the line is going clockwise, "CCW" if it is going counterclockwise
    """
    output = ""
    anti = "WSENW"
    horaire = "ESWNE"
    anti_count = 0
    horaire_count = 0
    for i,letter in enumerate(directions[:-1]):
        letters = letter + directions[i+1]
        if letters in anti:
            anti_count += 1
        if letters in horaire:
            horaire_count += 1
    if anti_count > horaire_count:
        output = "CCW"
    else:
        output = "CW"
    
    return output
