### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from DS.DS3 import solve


def test_from_problem_description():
    assert solve([(17, 2), (14, 3), (1, 1), (22, -1), (31, 5), (2, 4)], 0) == [
        17,
        1,
        14,
        22,
    ]
    assert solve([(5, -1), (2, 2), (58, 0), (61, 1), (77, -1)], 3) == [61, 2, 58, 5]
    assert solve([(49, 2), (90, 0), (1, -1), (44, 6), (26, 4)], 1) == [90, 49, 1]
