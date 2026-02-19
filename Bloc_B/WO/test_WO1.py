### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from WO.WO1 import solve


def test_from_problem_description():
    distance = 500
    skaters = ["Serina", "Beatrice", "Jutta"]
    initial_speed = [48.26, 53.35, 48.45]
    stamina = [750, 400, 600]
    second_speed = [47.23, 34.16, 38.45]
    assert solve(distance, skaters, initial_speed, stamina, second_speed) == "Jutta, 37.15s"

    distance = 1000
    skaters = ["Courtney", "Li", "Gilli", "Arianna"]
    initial_speed = [44.10, 43.90, 43.36, 43.70]
    stamina = [750, 750, 625, 625]
    second_speed = [19.79, 19.36, 27.10, 26.86]
    assert solve(distance, skaters, initial_speed, stamina, second_speed) == "Gilli, 101.71s"

    distance = 2400
    skaters = ["United States", "Japan", "Canada", "Pays-Bas"]
    initial_speed = [48.19, 48.41, 54.61, 49.03]
    stamina = [1600, 1200, 2000, 1800]
    second_speed = [46.10, 48.40, 48.93, 29.32]
    assert solve(distance, skaters, initial_speed, stamina, second_speed) == "Canada, 161.27s"

    