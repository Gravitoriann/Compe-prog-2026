### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from WO.WO3 import solve


def test_from_problem_description():
    distance = 120
    scores = [18, 19, 17, 20, 16]
    assert solve(distance, scores) == 294

    distance = 95
    scores = [15, 15, 16, 14, 15]
    assert solve(distance, scores) == 235

    distance = 130
    scores = [20, 20, 19, 18, 17]
    assert solve(distance, scores) == 317

    
def test_supplementaire():
    distance = 80
    scores = [10, 12, 11, 9, 13]
    assert solve(distance, scores) == 193
    