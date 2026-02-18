### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from DS.DS2 import solve


def test_from_problem_description():
    n = 4
    a = [2, 4, 1, 3]
    v = [20, 60, 40, 80]
    assert solve(n, a , v) == 180

    n = 2
    a = [2, 1]
    v = [100, 50]
    assert solve(n, a, v) == 100

    n = 5
    a = [2, 1, 4, 5, 3]
    v = [10, 30, 20, 40, 15]
    assert solve(n, a, v) == 90

    