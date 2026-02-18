### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from TP.TP2 import solve


def test_from_problem_description():
    assert solve("At the CRC we never give up and lose the game!") == "Impossible"
    assert solve("Un bon robot ne gagne que facilement!") == "Un bon robot\nne gagne\nque facilement!"
    assert solve("It is hard to write on limited length.") == "It is hard to\nwrite on\nlimited length."

def test_supplementaire():
    assert solve("Un arc-en-ciel est magnifique et impressionnant") == "Impossible"
    