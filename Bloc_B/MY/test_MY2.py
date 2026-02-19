### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from MY.MY2 import solve


def test_from_problem_description():
    assert solve((5.88, 8.82), (8.82, 4.41)) == 1549.45

    t1_obs1 = 2000 / 340
    t1_obs2 = 2100 / 340
    t2_obs1 = 2500 / 340
    t2_obs2 = 2400 / 340
    assert solve((t1_obs1, t1_obs2), (t2_obs1, t2_obs2)) == 112.62


    t1_obs1 = 1000 / 340
    t1_obs2 = 2000 / 340
    t2_obs1 = 3000 / 340
    t2_obs2 = 2000 / 340
    assert solve((t1_obs1, t1_obs2), (t2_obs1, t2_obs2)) == 1000.0


def test_supplementaire():
    t1_obs1 = 5000 / 340
    t1_obs2 = 4000 / 340
    t2_obs1 = 3000 / 340
    t2_obs2 = 2500 / 340
    assert solve((t1_obs1, t1_obs2), (t2_obs1, t2_obs2)) == 1000.62
