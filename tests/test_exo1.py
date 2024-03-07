from calculus.exo1 import count_upper_lower_case


def test_count_upper_lower_case_with_all_uppercase(capsys):
    source = "CECI EST UN TEST DE LA CHAÎNE DE CARACTÈRES!"
    count_upper_lower_case(source)
    captured = capsys.readouterr()
    assert captured.out == "Il y a 38 majuscules, et 0 minuscules.\n"


def test_count_upper_lower_case_with_all_lowercase(capsys):
    source = "ceci est un test de la chaîne de caractères!"
    count_upper_lower_case(source)
    captured = capsys.readouterr()
    assert captured.out == "Il y a 0 majuscules, et 38 minuscules.\n"


def test_count_upper_lower_case_with_mixed_case(capsys):
    source = "Ceci est un Test de la Chaîne de Caractères!"
    count_upper_lower_case(source)
    captured = capsys.readouterr()
    assert captured.out == "Il y a 5 majuscules, et 33 minuscules.\n"


def test_count_upper_lower_case_with_empty_string(capsys):
    source = ""
    count_upper_lower_case(source)
    captured = capsys.readouterr()
    assert captured.out == "Il y a 0 majuscules, et 0 minuscules.\n"
