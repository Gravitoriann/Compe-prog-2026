## This is the template for TP4, full problem in the rulebook ##

def solve(pangram: str):
    """
    Find the letters that are used more than once in the pangram

    Parameters:
        pangram str: The sentence that may be a pangram
        
    Returns:
        str: An empty string if not a pangram, otherwise the duplicated letters in order of appearance
    """
    duplicates = ""
    ## YOUR CODE GOES HERE ##
    ## VOTRE CODE VA ICI ##
    pangram = pangram.lower()
    caracts = set(pangram)
    if " " in caracts:
        caracts.remove(" ")
    if "," in caracts:
        caracts.remove(",")
    used = set()
    repetes = []
    if len(caracts) >= 26:
        for lettre in pangram:
            if lettre == " " or lettre == ",":
                continue
            if lettre not in used:
                used.add(lettre)
            else:
                repetes.append(lettre)
        duplicates = "".join(repetes)

    return duplicates
