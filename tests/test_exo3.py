# from unittest.mock import patch
# from calculus.exo3 import calculate_sum
# from ..trouduc import caca

# def test_calculate_sum_entiers(capsys):
#     with patch('builtins.input', side_effect=['10', '20']):
#         calculate_sum()
#         captured = capsys.readouterr()
#         assert captured.out == "La somme de 10 et 20 est égale à : En tant qu'entier : 30 En tant que chaîne de caractères : 30- En tant que flottant : 30.0"


# def test_calculate_sum_chaines(capsys):
#     with patch('builtins.input', side_effect=['abc', 'def']):
#         calculate_sum()
#         captured = capsys.readouterr()
#         assert captured.out == "Erreur : Veuillez entrer des nombres valides."


# def test_calculate_sum_float(capsys):
#     with patch('builtins.input', side_effect=['10.5', '20.7']):
#         calculate_sum()
#         captured = capsys.readouterr()
#         assert captured.out == "La somme de 10 et 20 est égale à :- En tant qucentier : 30- En tant que chaîne de caractères : 30- En tant que flottant : 30.0"
