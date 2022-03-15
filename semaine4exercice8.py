# Écrire une fonction prenant deux nombres et vérifiant si le premier nombre\
# est plus petit que le deuxième, si ce n'est pas le cas, les retourner dans\
# l'ordre inverse. Ex.: fonction(4, 3) retournerait 3 et, ensuite, 4.

def ordre_nb():
    nb_user_1 = int(input("Entrer un nombre : "))
    nb_user_2 = int(input("Entrer un deuxième nombre : "))
    if nb_user_1 > nb_user_2:
        nb_user_1, nb_user_2 = nb_user_2, nb_user_1
    return nb_user_1, nb_user_2

print(ordre_nb())
