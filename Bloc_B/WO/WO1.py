## This is the template for WO1, full problem in the rulebook ##
def time(distance, initial_speed, stamina, second_speed):
    time1 = 0
    if stamina > distance:
        time1 = distance/(initial_speed/3.6)
    else:
        time1 += stamina/(initial_speed/3.6)
        time1 += (distance-stamina)/(second_speed/3.6)
    return time1

def solve(distance: int, skaters: list[str], initial_speed: list[float], stamina: list[int], second_speed: list[float]):
    """
    Find the fastest skater and their winning time!

    Parameters:
        distance int: The distance of the race in meters
        skaters list[str]: The name of the skaters
        initial_speed list[float]: The speed of the athlete at the start of the race
        stamina list[int]: The amount of meters before dropping to second_speed
        second_speed list[float]: The speed of the athlete after the stamina drop
        
    Returns:
        str: The name of the athlete followed by their time in seconds with 2 decimals
    """
    winner = ""
    best_time = 9999
    for (index,skater) in enumerate(skaters):
        if time(distance, initial_speed[index], stamina[index], second_speed[index]) < best_time:
            best_time = time(distance, initial_speed[index], stamina[index], second_speed[index])
            winner = f"{skater}, {round(best_time, 2)}s"


    

    
    return winner

