## This is the template for TP3, full problem in the rulebook ##

def solve(palindrome: str):
    """
    Find the amount of changes to make it a palindrome

    Parameters:
        palindrome str: The string to try to make into a palindrome
        
    Returns:
        int: The amount of changes needed to make it a palindrome
    """
    changes = 0
    ## YOUR CODE GOES HERE ##
    ## VOTRE CODE VA ICI ##
    def is_palindrome(p):
        i_start = 0
        i_end = len(p) - 1
        while i_start < i_end:
            if p[i_start] != p[i_end]:
                return False
            i_start += 1
            i_end -= 1
        return True

    if is_palindrome(palindrome):
        return changes

    lettre_instances = {}
    indices_lettres = {}
    for i, lettre in enumerate(palindrome):
        if lettre not in lettre_instances:
            lettre_instances[lettre] = 1
        else:
            lettre_instances[lettre] += 1
        indices_lettres[i] = lettre

    lettres_instances_impaires = []
    lettres_impaires_indices = {}

    for l, nb in lettre_instances.items():
        if nb%2:
            lettres_instances_impaires.append(l)

    for i, l in indices_lettres:
        if l not in lettres_instances_impaires:
            continue
        if l not in lettres_impaires_indices:
            lettres_impaires_indices[l] = [i]
        else:
            lettres_impaires_indices[l].append(i)

    return changes
