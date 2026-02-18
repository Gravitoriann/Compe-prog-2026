## This is the template for TP2, full problem in the rulebook ##

def solve(haiku: str):
    """
    Separate into Haiku

    Parameters:
        haiku str: The string to separate in haiku
        
    Returns:
        [str]: The string of the Haiku separate in different rows
    """
    final_haiku = []
    ## YOUR CODE GOES HERE ##
    ## VOTRE CODE VA ICI ##
    for i in ["'", "-", ".", ",", "!", "?"]:
        haiku = haiku.replace(i, " ")
    haiku = haiku.split(" ")
    line1 = []
    line2 = []
    line3 = []
    for section in haiku:
        if len("".join(line1)) != 10:
            if len("".join(line1)) + len(section) <= 10:
                line1.append(section)
            else: return "Impossible"
        elif len("".join(line2)) != 7:
            if len("".join(line2)) + len(section) <= 7:
                line2.append(section)
            else: return "Impossible"
        elif len("".join(line3)) != 13:
            if len("".join(line3)) + len(section) <= 13:
                line3.append(section)
            else: return "Impossible"

    final_haiku = str(" ".join(line1) + "\n" + " ".join(line2) + "\n" + " ".join(line3))





    return final_haiku
