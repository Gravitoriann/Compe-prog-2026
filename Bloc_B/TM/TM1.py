## This is the template for TM1, full problem in the rulebook ##

def solve(network: list[str], destination: int):
    """
    Find the way the tramway should take

    Parameters:
        network list[str]: The network visualized
        destination int: The destination of the Tramway
        
    Returns:
        str: The instructions of the Tramway direction to take
    """
    instructions = []
    destination = str(destination)
    search = network[-1].index(destination)
    found = (len(network[-1]) / 2)
    center = (len(network[-1]) / 2)
    for line in network:
        for (index,item) in enumerate(line):
            if item =="/" and line[index+1] == "\\":
                if (center <= (len(network[-1]) / 2) and index <= (len(network[-1]) / 2)) or (center >= (len(network[-1]) / 2) and index >=(len(network[-1]) / 2)):
                    if index+1 >= center and search >= center:
                        found= index+1
                        if index< search:
                            instructions.append("R")
                        else: instructions.append("L")
                    elif index+1 <= center and search <= center:
                        found= index+1
                        if index> search:
                            instructions.append("L")
                        else: instructions.append("R")
        center = found






    


    return "".join(instructions)

