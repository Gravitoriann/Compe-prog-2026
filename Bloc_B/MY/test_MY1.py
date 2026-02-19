### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from MY.MY1 import solve


def test_from_problem_description():
    whirlpool = 0.45
    positions = [(-0.3, 0.5), (0.25, -0.4), (1, -0.75)]
    assert solve(whirlpool, positions) == 1

    whirlpool = 0.24
    positions = [(-0.1, -0.05), (0.3, -0.2), (0.0, 0.39), (0.1, -0.23)]
    assert solve(whirlpool, positions) == 0

    whirlpool = 0.84
    positions = [(-0.45, 0.45), (0.31, -0.15), (0.5, -0.5), (-0.71, -0.7), (75.5, 3.45), (0.99, 0.01)]
    assert solve(whirlpool, positions) == 3



    