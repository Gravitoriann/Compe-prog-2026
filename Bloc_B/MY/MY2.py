## This is the template for MY2, full problem in the rulebook ##


def solve(thunder_1: tuple[float, float], thunder_2: tuple[float, float]) -> float:
    """
    Find the closest possible distance between the 2 observers regarding the time they hear both thunders.

    Parameters:
        thunder_1 tuple[float, float]: The number of seconds for each observer to hear the thunder at position (0, 0)
        thunder_2 tuple[float, float]: The number of seconds for each observer to hear the thunder at position (4, 0)
        
    Returns:
        float: The minimal distance between the observers with a precision of 2 decimal places
    """
    SPEED_OF_SOUND = 340  # m/s
    LIGHTNING_DISTANCE = 4000  # 4 km in meters
    distance = 0

    p1 = (((((thunder_1[0]*SPEED_OF_SOUND)**2)-((thunder_2[0]*SPEED_OF_SOUND)**2)+16000000)/(8000)), ((((thunder_1[0]*SPEED_OF_SOUND)**2)-((((thunder_1[0]*SPEED_OF_SOUND)**2)-((thunder_2[0]*SPEED_OF_SOUND)**2)+16000000)/(8000))**2)**0.5))
    p2 = (((((thunder_1[1]*SPEED_OF_SOUND)**2)-((thunder_2[1]*SPEED_OF_SOUND)**2)+16000000)/(8000)), ((((thunder_1[1]*SPEED_OF_SOUND)**2)-((((thunder_1[1]*SPEED_OF_SOUND)**2)-((thunder_2[1]*SPEED_OF_SOUND)**2)+16000000)/(8000))**2)**0.5))
    distance = round((((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5),2)


    return distance
