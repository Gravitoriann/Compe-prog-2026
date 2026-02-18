## This is the template for 2D1, full problem in the rulebook ##

def solve(wall: list[str]):
    """
    Compute the wall surface without the window

    Parameters:
        wall [str]: The wall drawn with the window

    Returns:
        int: The area of the wall (no window) in square foot
    """
    area = 10
    ## YOUR CODE GOES HERE ##
    ## VOTRE CODE VA ICI ##
    largeur_totale = len(wall[0])
    hauteur_totale = 2*len(wall)
    coords_non_nulles = []

    for ichaine, chaine in enumerate(wall):
        for icaract, caract in enumerate(chaine):
            if caract =="┌" or caract=="┘":
                coords_non_nulles.append((ichaine, icaract))

    largeur_fenetre = coords_non_nulles[-2][1] - coords_non_nulles[1][1] +1
    hauteur_fenetre = 2*(coords_non_nulles[-2][0] - coords_non_nulles[1][0]+1)

    aire_tot = largeur_totale*hauteur_totale
    aire_fen = largeur_fenetre*hauteur_fenetre

    area = aire_tot - aire_fen

    return area