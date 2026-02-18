from enum import Enum
## This is the template for DS1, full problem in the rulebook ##

class Category(Enum):
    PUZZLE = 1
    FIGURINE = 2
    COLLECTIBLE = 3
    DOLL = 4
    CAR = 5
    BOARD_GAME = 6
    VIDEO_GAME = 7

class ToyInfo:
    def __init__(self, min_age: int, max_age: int, category: Category, price: int, id: int, name: str):
        self.min_age = min_age
        self.max_age = max_age
        self.category = category
        self.price = price
        self.id = id
        self.name = name

def solve(toys: list[ToyInfo], age: int, category: Category):
    """
    Pick the perfect Gift list

    Parameters:
        toys [ToyInfo]: The toys with all their characteristics
        age int: The age of the child
        category Category: The favorite category of toys of the child
        
    Returns:
        [str]: The IDs of all the toys that are valid from lowest to highest price
    """
    selected_toys = []
    ## YOUR CODE GOES HERE ##
    ## VOTRE CODE VA ICI ##



    return selected_toys
