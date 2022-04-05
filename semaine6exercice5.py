# Offrir à l'utilisateur d'entrer un nom de fichier et un nombre illimité de nombres positifs, tant et 
# aussi longtemps qu'il ne rentre pas un nombre négatif. Ajouter les nombres entrés par l'utilisateur 
# à une liste en excluant le nombre négatif. Ensuite, écrire les résultats suivants dans le fichier nommé 
# par l'utilisateur:

# La liste en ordre croissant
# La liste en ordre décroissant
# Le maximum
# Le minimum
# La moyenne de la liste
# La médiane (la valeur à la position centrale si la longueur de la liste est impaire et la moyenne des 
# deux valeurs centrales si paire)
# Ex: 1, 2, 3, 5, 4. Médiane = 3.
# Ex: 1, 2, 3, 4, 5, 6. Médiane = 3.5
# Le mode (l'occurrence la plus fréquente s'il y a lieu. Si chaque entrée est unique, inscrire que le mode = none)
# Ex: 1, 2, 2, 2, 3, 4, 3, 4. La mode = 3

# Vous ne pouvez pas utiliser de module, vous devez donc vous-même implémenter l'algorithme pour trier une liste 
# en ordre croissant, trier une liste en ordre décroissant, trouver le maximum, trouver le minimum, calculer la 
# moyenne, trouver la médiane, et trouver le mode(utilisez un dictionnaire pour chaque donnée en tant que clef, 
# affectez 0 comme valeur initiale et incrémentez de 1 à chaque répétition).


def liste_ordre_croissant(liste_entree_user):
    liste_ordre_croissant = []
    while liste_entree_user:
        nombre_min = minimum_liste(liste_entree_user)
        liste_entree_user.remove(nombre_min)
        liste_ordre_croissant.append(nombre_min)
    return liste_ordre_croissant
        

def liste_ordre_decroissant(liste_entree_user):
    liste_ordre_decroissant = []
    while liste_entree_user:
        nombre_max = maximum_liste(liste_entree_user)
        liste_entree_user.remove(nombre_max)
        liste_ordre_decroissant.append(nombre_max)
    return liste_ordre_decroissant


def minimum_liste(liste_entree_user):
    nombre_min = liste_entree_user[0]
    for i in liste_entree_user:
        if i < nombre_min:
            nombre_min = i
    return nombre_min


def maximum_liste(liste_entree_user):
    nombre_max = liste_entree_user[0]
    for i in liste_entree_user:
        if i > nombre_max:
            nombre_max = i
    return nombre_max


def moyenne_liste(liste_entree_user):
    somme = 0
    nb_valeur = 0
    for i in liste_entree_user:
        nb_valeur = nb_valeur + 1
        somme = somme + i
    return (somme/nb_valeur)


def mediane_liste(liste_entree_user):
    if len(liste_entree_user)%2 == 0:
        nb_med_1 = int((len(liste_entree_user))/2 - 1)
        nb_med_2 = int(nb_med_1 + 1)
        return (liste_entree_user[nb_med_1] + liste_entree_user[nb_med_2]) / 2   
    else:
        nb_med_1 = int((len(liste_entree_user) - 1)/2)
        return liste_entree_user[nb_med_1]


def mode_liste(liste_entree_user):
    
    ordre_croissant = liste_ordre_croissant(liste_entree_user)

    nb_pareil = 0
    fois_pareil = 0
    fois_pareil_max = 0
    for i in ordre_croissant:
        if i != nb_pareil:
            if fois_pareil > fois_pareil_max:
                fois_pareil_max = fois_pareil
                nb_pareil = i
                fois_pareil = 1
            else: 
                nb_pareil = i
                fois_pareil = 1
        elif i == nb_pareil :
            fois_pareil = fois_pareil + 1            
    if fois_pareil_max == 1:
        return "None"
    else:
        return fois_pareil_max
   
   
def entree_user():
    liste_choix_user = []
    choix_user = 1

    nom_fichier_user = input("Entrer un nom de fichier : ")
    fichier_user = open(f"{nom_fichier_user}.txt", "w", encoding="utf8")
    fichier_user.writelines("Vos entrées sont : ")

    while choix_user != 0:
        try:
            choix_user = float(input("Entrer une liste de nombres positifs ou 0 lorsque vous avez terminé : "))
        except:
            print("Attention, vous devez entrer un nombre!")
        if choix_user > 0 :
            liste_choix_user.append(choix_user)
            fichier_user.writelines(f"{choix_user}, ")
        elif choix_user == 0 :
            break    
        else:
            print("Attention, votre nombre doit être positif")

    liste_choix_user_copy_1 = liste_choix_user.copy()
    liste_choix_user_copy_2 = liste_choix_user.copy()
    fichier_user.writelines("\n")
    fichier_user.writelines(f"\nVos entrées en ordre croissant sont : {liste_ordre_croissant(liste_choix_user_copy_1)} \n")
    fichier_user.writelines(f"Vos entrées en ordre décroissant sont : {liste_ordre_decroissant(liste_choix_user_copy_2)} \n")
    fichier_user.writelines(f"Votre entrée minimum est : {minimum_liste(liste_choix_user)} \n")
    fichier_user.writelines(f"Votre entrée maximum est : {maximum_liste(liste_choix_user)} \n")
    fichier_user.writelines(f"La moyenne de vos entrée est : {moyenne_liste(liste_choix_user)} \n")
    fichier_user.writelines(f"La médianne de vos entrée est : {mediane_liste(liste_choix_user)} \n")
    fichier_user.writelines(f"Le mode de vos entrée est : {mode_liste(liste_choix_user)} \n")
    fichier_user.close()


entree_user()



# "Entrer une liste de nombres positifs ou 0 lorsque vous avez terminé"
# 0 est un nombre positif
#
# "vos entrée" besoin d'un "s"
#
# Ça me dit que tous mes nombres sont des float, ça devrait être tous des int
#
# Si j'entre 1,2,1,2, ça me dit mode = 2, mais ça doit être mode = 1,2
# Le mode est le (ou les) nombres le(s) plus fréquent(s)
#
# À part, super clean.
#
# :)
# 
# BRAVO en 3D ->

"""
                                                                 ,---,    ,---,    ,---,    ,---,  
                                                    ,----..   ,`--.' | ,`--.' | ,`--.' | ,`--.' |  
    ,---,. ,-.----.      ,---,                     /   /   \  |   :  : |   :  : |   :  : |   :  :  
  ,'  .'  \\    /  \    '  .' \            ,---.  /   .     : '   '  ; '   '  ; '   '  ; '   '  ;  
,---.' .' |;   :    \  /  ;    '.         /__./| .   /   ;.  \|   |  | |   |  | |   |  | |   |  |  
|   |  |: ||   | .\ : :  :       \   ,---.;  ; |.   ;   /  ` ;'   :  ; '   :  ; '   :  ; '   :  ;  
:   :  :  /.   : |: | :  |   /\   \ /___/ \  | |;   |  ; \ ; ||   |  ' |   |  ' |   |  ' |   |  '  
:   |    ; |   |  \ : |  :  ' ;.   :\   ;  \ ' ||   :  | ; | ''   :  | '   :  | '   :  | '   :  |  
|   :     \|   : .  / |  |  ;/  \   \\   \  \: |.   |  ' ' ' :;   |  ; ;   |  ; ;   |  ; ;   |  ;  
|   |   . |;   | |  \ '  :  | \  \ ,' ;   \  ' .'   ;  \; /  |`---'. | `---'. | `---'. | `---'. |  
'   :  '; ||   | ;\  \|  |  '  '--'    \   \   ' \   \  ',  /  `--..`;  `--..`;  `--..`;  `--..`;  
|   |  | ; :   ' | \.'|  :  :           \   `  ;  ;   :    /  .--,_    .--,_    .--,_    .--,_     
|   :   /  :   : :-'  |  | ,'            :   \ |   \   \ .'   |    |`. |    |`. |    |`. |    |`.  
|   | ,'   |   |.'    `--''               '---"     `---`     `-- -`, ;`-- -`, ;`-- -`, ;`-- -`, ; 
`----'     `---'                                                '---`"   '---`"   '---`"   '---`"  
                                                                                                   
"""




