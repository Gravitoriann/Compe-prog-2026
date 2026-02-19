### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from MY.MY4 import solve


def test_from_problem_description():
    assert solve(25, [[16,"E",5],[17,"NE",3],[11,"NO", 3],[29,"E",2],[42,"N",5],[12,"SO",7]]) == 15.05
    assert solve(47, [[12,"NE",3],[7,"E",5],[18,"N",9]]) == 10.68
    assert solve(5, [[55,"NE",7],[31,"SE",5],[60,"S",3],[19,"N",4],[37,"S",7]]) == 19.13

def test_supplementaire():
    assert solve(29,[[37,"E",1],[15,"NO",6],[15,"NE",2],[23,"O",2],[36,"E",1],[31,"N",1],[46,"E",17]]) == 14.95

    