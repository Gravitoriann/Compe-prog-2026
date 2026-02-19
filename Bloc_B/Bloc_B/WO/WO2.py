## This is the template for WO2, full problem in the rulebook ##

def solve(track: list[str]):
    """
    Find the directions to steer the bobsleigh

    Parameters:
        track [str]: The bobsleigh track layout
        
    Returns:
        [str]: The directions to steer the bobsleigh
    """
    directions = ""
    anciens_voisins = []
    voisins = [(-1, 0),(1,0),(0,-1),(0,1)]
    visited = set()

    for i, element in enumerate(track[-1]):
        if element == "D":
            coords = (len(track)-1, i)
            visited.add(coords)
    anciens_voisins.append((-1,0))
    while True:
        if track[coords[0]][coords[1]] == "F":
            return directions[1:]
        for voisin in voisins:
            if track[coords[0]+voisin[0]][coords[1]+voisin[1]] != " ":
                if (coords[0]+voisin[0], coords[1]+voisin[1]) not in visited:
                    anciens_voisins.append(voisin)
                    coords = (coords[0]+voisin[0], coords[1]+voisin[1])
                    visited.add(coords)
                    if voisin != anciens_voisins[-2]:
                        av = anciens_voisins[-2]
                        v = voisin
                        if av == (-1,0)and v==(0,1)or av==(0,-1)and v==(-1,0)or av==(0,1)and v==(1,0)or av==(1,0)and v==(0,-1):
                            directions += "D"
                        elif av == (-1,0)and v==(0,-1)or av==(0,-1)and v==(1,0)or av==(0,1)and v==(-1,0)or av==(1,0)and v==(0,1):
                            directions += "G"
                    else:
                        directions += "R"
    
    return directions
