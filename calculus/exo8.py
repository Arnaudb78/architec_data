import random


def deviner_nombre():
    nombre_mystere = random.randint(1, 100)
    nombre_tentatives = 5  # Nombre de tentatives autorisées

    print("Bienvenue dans le jeu de deviner le nombre !")
    print("Je pense à un nombre entre 1 et 100. A vous de deviner !")

    for tentative in range(1, nombre_tentatives + 1):
        tentative_utilisateur = int(
            input(f"Tentative {tentative}/{nombre_tentatives}. Entrez votre guess : "))

        if tentative_utilisateur < nombre_mystere:
            print("Le nombre mystère est plus grand !")
        elif tentative_utilisateur > nombre_mystere:
            print("Le nombre mystère est plus petit !")
        else:
            print(f"Félicitations ! Vous avez deviné le nombre mystère ({nombre_mystere}) en {tentative} tentatives !")
            return

    print(f"Désolé, vous avez utilisé toutes vos {nombre_tentatives} tentatives. Le nombre mystère était {nombre_mystere}.")


# Exemple d'utilisation
deviner_nombre()
