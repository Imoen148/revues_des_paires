# Écrire un programme avec une fonction prenant 2 floats et retournant leur addition\
# soustraction et division. Les résultats des additions doivent avoir au plus 1\
# chiffre après la virgule, la soustraction 2 chiffres après la virgule et la division\
# 3 chiffres après la virgule.

def calculatrice_float():
    print('''Entrer deux nombre décimaux en utilisant le "." (Ex : 25.36)''')
    nb_1 = float(input("Entrer votre premier nombre décimal : "))
    nb_2 = float(input("Entrer votre deuxième nombre décimal : "))

    print(f"Le résultat de l'addition de vos nombres est {(nb_1 + nb_2):.1f}")
    print(f"Le résultat de la soustraction de vos nombre est {(nb_1 - nb_2):.2f}")
    print(f"Le résultat de la division de vos nombres est {(nb_1 / nb_2):.3f}")
    
calculatrice_float()