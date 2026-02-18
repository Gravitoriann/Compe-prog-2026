### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from TP.TP4 import solve


def test_from_problem_description():
    assert solve("The quick brown fox jumps over the lazy dog") == "ouoerteo"
    assert solve("Sphinx of black quartz, judge my vow") == "auo"
    assert solve("aaaaaabcdefghijklmonpqrstuvwxy") == ""

def test_supplementaire():
    assert solve("Portez ce vieux whisky au juge blond qui fume") == "eeiueouiue"
