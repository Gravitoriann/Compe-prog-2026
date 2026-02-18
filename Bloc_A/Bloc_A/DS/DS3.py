## This is the template for DS3, full problem in the rulebook ##


def solve(memory: list[str], start: int):
    """
    Compute the wall surface without the window

    Parameters:
        wall [str]: The wall drawn with the window

    Returns:
        int: The area of the wall (no window) in square foot
    """
    resultat = []
    ### YOUR CODE GOES HERE ###
    current = start
    while current != -1:
        t = memory[current]
        resultat.append(t[0])
        current = t[1]

    return resultat
