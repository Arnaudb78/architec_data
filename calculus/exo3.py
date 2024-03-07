def calculate_sum():
    nombre1_str = input("Entrez le premier nombre : ")
    nombre2_str = input("Entrez le deuxième nombre : ")

    try:
        nombre1 = int(nombre1_str)
        nombre2 = int(nombre2_str)
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
        return

    somme = nombre1 + nombre2

    print(f"La somme de {nombre1} et {nombre2} est égale à :")
    print(f"- En tant qu'entier : {somme}")
    print(f"- En tant que chaîne de caractères : {str(somme)}")
    print(f"- En tant que flottant : {float(somme)}")


calculate_sum()
