## This is the template for TM2, full problem in the rulebook ##

import math

def solve(stations: list[int]):
    """
    Find the time it takes to get to the competition

    Parameters:
        stations list[int]: The amount of stations to travel per line to take
        
    Returns:
        float: The time to get to the competition (using 1 decimal precision)
    """
    total_time = 0.0
    modifiable = stations.copy()

    for i, nb in enumerate(stations):
        total_time += 2.5*(nb-1)
        if len(modifiable) != 1:
            total_time = math.ceil(total_time)
            while True:
                if total_time%5:
                    total_time+=1
                else:
                    print("fin transfert")
                    print(total_time)
                    modifiable.pop(0)
                    break
    
    return total_time
