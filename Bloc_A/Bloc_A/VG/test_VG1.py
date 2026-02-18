### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from VG.VG1 import solve


def test_from_problem_description():
    assert solve(240, ["bread", "cut lettuce", "cut tomato", "cooked beef"]) == 624

    assert solve(300, ["cut carrot", "cut cabbage"]) == 216

    assert solve(265, ["pepper", "cut cheese", "cut tomato", "boiled pasta", "boiled sauce", "cooked beef"]) == 1610



def test_supplementaire():
    assert solve(150, ["cooked sausage", "cooked bread"]) == 140

    assert solve(407, ["boiled rice", "boiled carrot", "cooked beef", "cooked onion"]) == 1547



