### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from WO.WO5 import solve


def test_from_problem_description():
    # Exemple 1 - original
    l_w = [(26, 8, 8), (98, 10, 9), (56, 7, 6), (44, 6, 7)]
    c = [(23, 7, 7), (66, 6, 7), (8, 9, 10), (12, 8, 8)]
    r_w = [(41, 4, 8), (74, 9, 9), (33, 6, 6), (55, 9, 10)]
    assert solve(l_w, c, r_w) == [[98, 8, 55], [26, 12, 74], [56, 23, 33], [44, 66, 41]]

    l_w_2 = [(11, 10, 5), (22, 5, 10), (33, 8, 8), (44, 3, 3)]
    c_2 = [(55, 9, 6), (66, 6, 9), (77, 7, 7), (88, 4, 4)]
    r_w_2 = [(91, 10, 10), (92, 2, 8), (93, 8, 2), (94, 5, 5)]
    assert solve(l_w_2, c_2, r_w_2) == [[33, 66, 91], [11, 55, 93], [44, 77, 94], [22, 88, 92]]

    l_w_3 = [(1, 7, 8), (2, 8, 7), (3, 6, 6), (4, 5, 5)]
    c_3 = [(5, 9, 8), (6, 8, 9), (7, 7, 7), (8, 6, 6)]
    r_w_3 = [(9, 10, 7), (10, 7, 10), (11, 8, 8), (12, 5, 6)]
    assert solve(l_w_3, c_3, r_w_3) == [[1, 6, 10], [2, 5, 9], [3, 7, 11], [4, 8, 12]]


def test_supplementaire():
    l_w_4 = [(10, 10, 1), (20, 1, 10), (30, 5, 5), (40, 8, 3)]
    c_4 = [(50, 10, 2), (60, 2, 10), (70, 6, 6), (80, 7, 4)]
    r_w_4 = [(90, 9, 3), (100, 3, 9), (110, 6, 5), (120, 5, 7)]
    assert solve(l_w_4, c_4, r_w_4) == [[40, 70, 120], [10, 50, 90], [30, 80, 110], [20, 60, 100]]
