### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from twoD.twoD2 import solve


def test_from_problem_description():
    books = ["Hobbit", "Disney", "Inferno", "Narnia", "Wicked", "Harry Potter"]
    assert solve(books) == [
    "┌───┐                         ",
    "│ H │                         ",
    "│ a │                         ",
    "│ r │                         ",
    "│ r │                         ",
    "│ y │┌───┐                    ",
    "│   ││ I │┌───┐┌───┐┌───┐┌───┐",
    "│ P ││ n ││ D ││ H ││ N ││ W │",
    "│ o ││ f ││ i ││ o ││ a ││ i │",
    "│ t ││ e ││ s ││ b ││ r ││ c │",
    "│ t ││ r ││ n ││ b ││ n ││ k │",
    "│ e ││ n ││ e ││ i ││ i ││ e │",
    "│ r ││ o ││ y ││ t ││ a ││ d │",
    "└───┘└───┘└───┘└───┘└───┘└───┘"
    ]

    books = ["The Hunger Games", "The Great Gatsby", "The book thief", "The Outsiders", "The little Prince", "Pride and Prejudice"]
    assert solve(books) == [
    "┌───┐                         ",
    "│ P │                         ",
    "│ r │┌───┐                    ",
    "│ i ││ T │┌───┐┌───┐          ",
    "│ d ││ h ││ T ││ T │          ",
    "│ e ││ e ││ h ││ h │┌───┐     ",
    "│   ││   ││ e ││ e ││ T │┌───┐",
    "│ a ││ l ││   ││   ││ h ││ T │",
    "│ n ││ i ││ G ││ H ││ e ││ h │",
    "│ d ││ t ││ r ││ u ││   ││ e │",
    "│   ││ t ││ e ││ n ││ b ││   │",
    "│ P ││ l ││ a ││ g ││ o ││ O │",
    "│ r ││ e ││ t ││ e ││ o ││ u │",
    "│ e ││   ││   ││ r ││ k ││ t │",
    "│ j ││ P ││ G ││   ││   ││ s │",
    "│ u ││ r ││ a ││ G ││ t ││ i │",
    "│ d ││ i ││ t ││ a ││ h ││ d │",
    "│ i ││ n ││ s ││ m ││ i ││ e │",
    "│ c ││ c ││ b ││ e ││ e ││ r │",
    "│ e ││ e ││ y ││ s ││ f ││ s │",
    "└───┘└───┘└───┘└───┘└───┘└───┘"
    ]

    books = ["1984", "Twilight", "The Giver", "Divergent", "Holes", "The Host", "Eragon"]
    assert solve(books) == [
    "┌───┐┌───┐                         ",
    "│ D ││ T │┌───┐┌───┐               ",
    "│ i ││ h ││ T ││ T │               ",
    "│ v ││ e ││ h ││ w │┌───┐          ",
    "│ e ││   ││ e ││ i ││ E │┌───┐     ",
    "│ r ││ G ││   ││ l ││ r ││ H │┌───┐",
    "│ g ││ i ││ H ││ i ││ a ││ o ││ 1 │",
    "│ e ││ v ││ o ││ g ││ g ││ l ││ 9 │",
    "│ n ││ e ││ s ││ h ││ o ││ e ││ 8 │",
    "│ t ││ r ││ t ││ t ││ n ││ s ││ 4 │",
    "└───┘└───┘└───┘└───┘└───┘└───┘└───┘"
    ]
    