# Écrire un programme demandant à l'utilisateur de rentrer un nombre entre\
# 1 et 20, vérifier si ce dernier est bel et bien entre 1 et 20 et\
# indiquez-lui si son nombre est un nombre premier (ayant aucun autre\
# facteur entier que 1 et lui-même)

def nombre_premier():
    nb_user = int(input("Entrer un chiffre entre 1 et 20 pour savoir si\
 c'est un nombre premier : "))
    if not(1 <= nb_user <= 20):
        print("Attention, vous devez entrer chiffre entre 1 et 20!")
    elif nb_user == 2 or nb_user == 3 or nb_user == 5 or nb_user == 7\
    or nb_user == 11 or nb_user == 13 or nb_user == 13 or nb_user == 19 :
        print(f"{nb_user} est un nombre premier")
    else :
        print(f"{nb_user} n'est pas un nombre premier")

nombre_premier()


# OH yea je viens d'apprendre le \ pour continuer sur une autre ligne !