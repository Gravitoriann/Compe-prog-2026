### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from TM.TM4 import solve


def test_from_problem_description():
    instructions = [
        "Vendôme = Orange",
        "Licorne = Soirée illimité",
        "Snowdon = Sac à dos",
        "Vert -> Rose",
        "Vert = Coffee",
        "Sac à main = Mensuel",
        "Jaune = Bandoulière",
        "Station2 = Lait",
        "Station0 = Berri-UQAM",
        "Weekend-illimité -> Sac à dos",
        "Bandoulière -> 1 passage",
        "Sac plastique = Jus",
        "Atwater = Tote bag",
        "Berri-UQAM -> Bleu",
        "Eau -> Sac à dos"]
    assert solve(instructions) == [["Go ask Frank...."]]


    