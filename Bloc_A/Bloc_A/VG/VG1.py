## This is the template for VG1, full problem in the rulebook ##


def solve(timer: int, recipe: list[str]):
    """
    How much profit can you make in Overcooked

    Parameters:
        timer int: The number of seconds for the level
        recipe list[str]: The ingredients and cooking manipulations for each step of the recipe

    Returns:
        int: The maximum amount of profit that can be made
    """
    profit = 0
    ### YOUR CODE GOES HERE ###
    import math
    time_for_one_recipe = 1
    non_prepares = []
    cut = []
    boiled = []
    cooked = []
    for ingredient in recipe:
        L = ingredient.split()
        if len(L) == 1:
            time_for_one_recipe += 1
            non_prepares.append(ingredient)
        else:
            if L[0] == "boiled":
                boiled.append(ingredient)
                time_for_one_recipe += 1
            elif L[0] == "cooked":
                cooked.append(ingredient)
                time_for_one_recipe += 1
            else:
                time_for_one_recipe += 5
                cut.append(ingredient)

    nb_max_recettes = math.floor(timer*2/time_for_one_recipe)
    nb_max_boiled_unique = math.inf
    nb_max_cooked_unique = math.inf

    if boiled:
        nb_max_boiled_unique = ((timer/10)/len(boiled))*4
    if cooked:
        nb_max_cooked_unique = ((timer/7)/len(cooked))*2

    nb_recettes = math.floor(min([nb_max_recettes, nb_max_boiled_unique, nb_max_cooked_unique]))
    profit = round(((len(recipe)+len(non_prepares)+2*len(cut)+4*(len(cooked)+len(boiled)))*(len(recipe)/3))*nb_recettes)

    return profit
