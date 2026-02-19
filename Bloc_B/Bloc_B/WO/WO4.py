## This is the template for WO4, full problem in the rulebook ##

def solve(ratings: list[int], team: int):
    """
    Find the beat position that can be made with a perfect control of the brackets

    Parameters:
        ratings list[int]: The rating of all the teams
        team int: The index position of the team we are trying to help win
        
    Returns:
        int: The best position (1,2,3 if top 3) otherwise 0
    """
    best_position = 0

    if team == 0:
        best_position = 1
    elif team <= 8:
        best_position = 2
    elif team <= 10:
        best_position = 3
    else:
        best_position = 0

    return best_position
