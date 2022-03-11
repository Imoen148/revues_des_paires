# Créer une calculatrice d'IMC demandant à l'utilisateur sa grandeur(en mètres), 
# son poids(en kg). Retournez ensuite la catégorie dans laquelle se trouve la 
# personne.

""" 
Poids en kg / Taille en mètre au 2 = IMC

IMC 0 à 16.49: Maigreur extrême
IMC 16.5 à 18.49: Maigreur
IMC 18.5 à 24.99: Poids santé
IMC 25 à 29.99: Surpoids
IMC 30 à 34.99: Obèse classe 1
IMC 35 à 39: Obèse classe 2
IMC 40 et +: Obésité morbide

"""

def imc ():
    taille = int(input("Entrer votre taille en cm : "))
    poids = int(input("Entrer votre poids en livres : "))
    taille = taille/100
    poids = poids/2.2046
    return poids/taille**2

def category (imc_user):
    if imc_user >= 40:
        print("Catégorie : Obésité morbide")
    elif imc_user >= 35:
        print("Catégorie : Obèse classe 2")
    elif imc_user >= 30:
        print("Catégorie : Obèse classe 1")
    elif imc_user >= 25:
        print("Catégorie : Surpoids")
    elif imc_user >= 18.5:
        print("Catégorie : Poids santé")
    elif imc_user >= 16.5:
        print("Catégorie : Maigreur")
    else:
        print("Catégorie : Maigreur extrême")

imc_user = imc ()
category(imc_user)