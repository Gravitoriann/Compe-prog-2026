### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from DS.DS1 import solve
from DS.DS1 import ToyInfo
from DS.DS1 import Category


def test_from_problem_description():
    toys = [
        ToyInfo(3, 6, Category.PUZZLE, 15, 101, "Animal Puzzle"),
        ToyInfo(5, 9, Category.FIGURINE, 20, 102, "Knight Figure"),
        ToyInfo(6, 12, Category.PUZZLE, 10, 103, "World Map Puzzle"),
        ToyInfo(4, 7, Category.CAR, 18, 104, "Race Car"),
    ]
    age = 6
    category = Category.PUZZLE
    assert solve(toys, age, category) == [103, 101]

    toys = [
        ToyInfo(7, 12, Category.BOARD_GAME, 35, 201, "Treasure Island"),
        ToyInfo(6, 10, Category.BOARD_GAME, 25, 202, "Math Challenge"),
        ToyInfo(8, 14, Category.COLLECTIBLE, 40, 203, "Rare Cards"),
        ToyInfo(3, 7, Category.BOARD_GAME, 30, 204, "Family Fun"),
    ]
    age = 8
    category = Category.BOARD_GAME
    assert solve(toys, age, category) == [202, 201]


def test_supplementaire():
    toys = [
        ToyInfo(10, 16, Category.VIDEO_GAME, 60, 301, "Space Adventure"),
        ToyInfo(8, 12, Category.VIDEO_GAME, 45, 302, "Puzzle Quest"),
        ToyInfo(12, 18, Category.VIDEO_GAME, 70, 303, "Battle Arena"),
        ToyInfo(9, 14, Category.CAR, 40, 304, "Remote Racer"),
    ]
    age = 11
    category = Category.VIDEO_GAME
    assert solve(toys, age, category) == [302, 301]
    