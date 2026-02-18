### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from VG.VG2 import solve


def test_from_problem_description():
    sphere = (4, 5, 6, 2)
    cube = (6, 6, 6, 2)
    assert solve(sphere, cube) == True

    sphere = (11, 14, 3, 3)
    cube = (9, 12, 11, 6)
    assert solve(sphere, cube) == False

    sphere = (0, 0, 0, 10)
    cube = (0, 9, 14, 10)
    assert solve(sphere, cube) == True

def test_supplementaire():
    sphere = (2, 2, 2, 2)
    cube = (2, 2, 4, 1)
    assert solve(sphere, cube) == True

    sphere = (12, 2, 2, 4)
    cube = (2, 3, 4, 4)
    assert solve(sphere, cube) == False



