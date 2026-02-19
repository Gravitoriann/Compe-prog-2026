## This is the template for WO5, full problem in the rulebook ##

import math

def solve(left_wing: list[tuple[int, int, int]], center: list[tuple[int, int, int]], right_wing: list[tuple[int, int, int]]):
    """
    Find the best attacking lineup for a hockey team

    Parameters:
        left_wing list[tuple[int, int, int]]: The 4 left wing players with their number, natural talent and endurance
        center list[tuple[int, int, int]]: The 4 center players with their number, natural talent and endurance
        right_wing list[tuple[int, int, int]]: The 4 right wing players with their number, natural talent and endurance
        
    Returns:
        list[list[int]]: The numbers of the players on the 4 lines
    """
    lines = []

    left_first_scores = 0
    for i,t in enumerate(left_wing):
        score = t[1]*1.2+t[2]*1.2
        if score > left_first_scores:
            left_first_scores = score
            left = t[0]
            lefti = i
    left_first_scores = 0
    for i,t in enumerate(center):
        score = t[1]*1.2+t[2]*1.2
        if score > left_first_scores:
            left_first_scores = score
            centre = t[0]
            centrei = i
    left_first_scores = 0
    for i,t in enumerate(right_wing):
        score = t[1] * 1.2 + t[2] * 1.2
        if score > left_first_scores:
            left_first_scores = score
            right = t[0]
            righti = i
    lines.append([left, centre, right])
    left_wing.pop(lefti)
    center.pop(centrei)
    right_wing.pop(righti)

    left_first_scores = 0
    for i,t in enumerate(left_wing):
        score = t[1]*1.2+t[2]
        if score > left_first_scores:
            left_first_scores = score
            left = t[0]
            lefti = i
    left_first_scores = 0
    for i,t in enumerate(center):
        score = t[1]*1.2+t[2]
        if score > left_first_scores:
            left_first_scores = score
            centre = t[0]
            centrei = i
    left_first_scores = 0
    for i,t in enumerate(right_wing):
        score = t[1] * 1.2 + t[2]
        if score > left_first_scores:
            left_first_scores = score
            right = t[0]
            righti = i
    lines.append([left, centre, right])
    left_wing.pop(lefti)
    center.pop(centrei)
    right_wing.pop(righti)

    endurance_talent = -math.inf
    for i,t in enumerate(left_wing):
        score = t[2]-t[1]
        if score > endurance_talent:
            endurance_talent = score
            left = t[0]
            lefti = i
    endurance_talent = -math.inf
    for i,t in enumerate(center):
        score = t[2] - t[1]
        if score > endurance_talent:
            endurance_talent = score
            centre = t[0]
            centrei = i
    endurance_talent = -math.inf
    for i,t in enumerate(right_wing):
        score = t[2] - t[1]
        if score > endurance_talent:
            endurance_talent = score
            right = t[0]
            righti = i
    print(left_wing)
    fourth = [left, centre, right]
    left_wing.pop(lefti)
    center.pop(centrei)
    right_wing.pop(righti)
    lines.append([left_wing[0][0], center[0][0], right_wing[0][0]])
    lines.append(fourth)
    return lines
