
# avoir un texte défini 
# donner à l'utilisateur la possibilité de saisir le texte à partir de l'interface
# lors de le saisie de texte l'utilisateur ne doit pas regarder son clavier
# à fin de la saisie comparer les caractères saisie avec le texte donné au départ et calculer le nbre d'erreur de saisie



# -*-coding:Utf-8 -*

import os

texte_donné = []
texte_saisi = []

# avoir un texte défini 
texte_donné = "Bonjour, je te mets au défi de saisir ce texte en faisant le moins d'erreurs possible sans regarder ton clavier"
print(texte_donné)


# donner à l'utilisateur la possibilité de saisir le texte à partir de l'interface
texte_saisi = input("Saisir le texte : ")
print("le texte_saisi est :  "+texte_saisi+" ")


#comparer les 2 textes 
if  texte_donné == texte_saisi :
    print("Les deux textes sont identiques")
else :
    print("Les deux textes ne sont pas identiques")
    

#comparer caractère par caracteres


#compter le nbre de caractères faux


#compter le nbre de caractères 
def compte_mots(texte_saisi):
    return len(texte_saisi.split())
#---appel de la fonction compte_mots
compte_mots(texte_saisi)



 # compter les différences qu’il y a entre deux chaînes de caractères
def hamming_distance(string1, string2): 
    if (len(string1) != len (string2)):
        return -1
    print("test")
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
            print("meme nbre de lettres")
    # Return the final count of differences
    return distance
    print("test3")
    print ("le nbre de lettre differents est : ", distance)

hamming_distance("Bonjour", "Bonsoir")



# Preparation de l’arret
os.system("pause")








