nombre1_str = input("Entrez le premier nombre : ")
nombre2_str = input("Entrez le deuxième nombre : ")


class calculate_to_string:
    def __init__(self, nombre1_str, nombre2_str):
        self.nombre1_str = nombre1_str
        self.nombre2_str = nombre2_str

    def calculate_sum(self):
        try:
            nombre1 = int(self.nombre1_str)
            nombre2 = int(self.nombre2_str)
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
            return

        somme = nombre1 + nombre2

        print(f"La somme de {nombre1} et {nombre2} est égale à :")
        print(f"- En tant qu'entier : {somme}")
        print(f"- En tant que chaîne de caractères : {str(somme)}")
        print(f"- En tant que flottant : {float(somme)}")
