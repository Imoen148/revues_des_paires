# Créer un dictionnaire possédant les cours que vous suivez cette session et leur enseignant
# respectif. Par exemple:

# Keven Presseau-St-Laurent - Concepts de programmation 1

# Ensuite, afficher un menu à la console présentant les 5 cours et offrant à l'utilisateur
# d'en sélectionner 1. Lorsque l'utilisateur à fait sa sélection, afficher le nom de
# l'enseignant et le nom du cours à l'écran.

cours_prof = {"Keven Presseau-St-Laurent" : "Concepts de programmation 1",\
"Emma Senez-Parent" : "Logique Mathématique pour les professionnels de \
l'informatique", "Jean-Pierre Fiset" : "Système d'exploitation"}

fichier_cours_prof = open("bdd.txt", "w", encoding='utf8')
fichier_cours_prof.write("Concepts de programmation 1 \n")
fichier_cours_prof.write("Keven Presseau-St-Laurent \n")
fichier_cours_prof.write("\n")
fichier_cours_prof.write("Logique Mathématique pour les professionnels de l'informatique \n")
fichier_cours_prof.write("Emma Senez-Parent \n")
fichier_cours_prof.write("\n")
fichier_cours_prof.write("Système d'exploitation \n")
fichier_cours_prof.write("Jean-Pierre Fiset \n")
fichier_cours_prof.write("\n")
fichier_cours_prof.close()
fichier_cours_prof = open("bdd.txt", "r", encoding='utf8')

cours = list(cours_prof.values())
liste_cours_prof = list(cours_prof.items())

print("Sélectionner un cours pour connaitre le nom du professeur, faites \
une recherche par enseignant \nou ajouter un professeur et son cours \
associés.")
print("\t 1-", cours[0])
print("\t 2-", cours[1])
print("\t 3-", cours[2])
print("\t 4- Recherche par enseignant")
print("\t 5- Ajout enseignant/cours")
choix_user = int(input("Entrer 1, 2, 3, 4 ou 5 : "))
if choix_user == 1 or choix_user == 2 or choix_user == 3 or choix_user == 4\
or choix_user == 5:
    if choix_user == 1:
        print(liste_cours_prof[0])
    elif choix_user == 2:
        print(liste_cours_prof[1])
    elif choix_user == 3:
        print(liste_cours_prof[2])
    elif choix_user == 4:
        recherche_enseignant = input("Entrer le nom de l'enseignant rechercher : ")
        print(cours_prof.get(recherche_enseignant, "Ce professeur n'existe pas!"))
    else:
        prof_user = input("Entrer le nom du nouveau pofesseur : ")
        cours_user = input("Entrer le nom du nouveau cours associé : ")
        cours_prof[prof_user] = cours_user

        fichier_cours_prof = open("bdd.txt", "a", encoding='utf8')
        fichier_cours_prof.write(cours_user)
        fichier_cours_prof.write("\n")
        fichier_cours_prof.write(prof_user)
        fichier_cours_prof.write("\n")
        fichier_cours_prof.close()
else:
    (print("Attention, vous devez entre 1, 2 ou 3!"))

# Exercice 4 : 
#En se basant sur l'exercice 3, créer un fichier bdd.txt fonctionnant comme une base de 
# données et remplir le dictionnaire à partir de ce fichier. Pour vous faciliter la 
# tâche, vous pouvez écrire les informations de la manière suivante:

# Nom de cours 1
# Nom de prof 1

#Nom de cours 2
#...

# Exercice 5 :
# En se basant sur l'exercice 4, modifier le menu utilisateur en y ajoutant une
# option lui permettant de faire une recherche d'enseignant. Vérifier si 
# l'enseignant entré par l'utilisateur est présent dans votre liste de cours et 
# indiquer le résultat à la console.


# Exercice 6 :
# Offrir à l'utilisateur une nouvelle option au menu lui permettant d'ajouter un 
# cours et un nom d'enseignant à la base de données de l'exercice 4. Une fois 
# les données utilisateurs entrées, ajouter les informations à la fin du 
# document bdd.txt

# Revue de paires:
# Utilisez l'exercice 3-6 pour faire la revue des paires. Publiez vos exercices 
# dans le «repo» revue_des_paires de la semaine précédente pour effectuer la remise.