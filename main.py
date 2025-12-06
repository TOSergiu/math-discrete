import numpy as np
from fonction1 import pageRankLinear #j'importe ma fonction pageRankLinear vous devrez faire la même

def load_adjacency_matrice(filename):
    return np.genfromtxt(filename, delimiter=",") #no.genfromtxt permet de mettre en tableau la matrice
    #dans le fichier matrice.csv et le delimiter montre que les valeurs de la matrice sont séparées
    #par des virgules

def load_personalisation_vecteur(filename):
    return np.genfromtxt(filename, delimiter=",", skip_header=1)#c'est la même chose ici sauf qu'on
    #prend pas la première ligne du fichier avec les lettres

def main():
    alpha = 0.9 #valeur par défaut de alpha (téléportation)

    A = load_adjacency_matrice("matrice.csv") #on charge la matrice A
    v = load_personalisation_vecteur("VecteurPersonnalisation_Groupe45.csv") #on charge le vecteur

    print("Matrice d'adjacence A :")
    print(A) #pour imprimer la matrice donnée comme demandé dans les consignes

    print("Vecteur de personnalisation v :")
    print(v) #pour imprimer le vecteur de personnalisation comme demandé dans les consignes
    print("Somme de v :", np.sum(v))

    x = pageRankLinear(A, alpha, v) #x = vecteur pagerank quand il est calculé

    print("Somme de x :", np.sum(x)) #somme des valeurs calculée (1)

if __name__ == "__main__":
    main()