## This is the template for MY1, full problem in the rulebook ##

def solve(whirlpoool: float, positions: list[tuple[float, float]]):
    """
    Find how many of the positions are safe for the ships

    Parameters:
        whirlpool float: The radius of the whirlpool
        positions list[tuple[float, float]]: position of the ships
        
    Returns:
        int: The number of ships that are safe
    """
    nbr_safe = 0
    for pos in positions:
        if (pos[0]**2 + pos[1]**2)**0.5 > whirlpoool +0.15:
            nbr_safe +=1


    

    
    return nbr_safe