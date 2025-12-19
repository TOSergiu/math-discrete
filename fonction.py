import numpy as np

def pageRankLinear(A: np.matrix, alpha: float, v: np.array):
    """
        – Input : Une matrice d’adjacence 1 A d’un graphe dirigé, 
        pondéré et régulier G, un vecteur de personnalisation v, 
        ainsi qu’un paramètre de téléportation α compris entre 0
        et 1 (0.9 par défaut et pour les résultats à présenter).
        Toutes ces valeurs sont non-négatives.

        – Output : Un vecteur x contenant les scores d’importance des noeuds ordonnés dans
        le même ordre que les lignes de la matrice d’adjacence (représentant les noeuds).
    """

    n = A.shape[0]  #nombre de noeuds matrice A

    #on construit la matrice de transition P
    P = np.zeros((n, n))

    for j in range(n):
        col_sum = np.sum(A[:, j])
        if col_sum != 0:
            P[:, j] = A[:, j] / col_sum
        else:
            #si un noeud n'a pas de sortie, on met une proba uniforme
            P[:, j] = 1.0 / n

    #construction du système linéaire
    I = np.eye(n) #créer matrice taille n sur n
    M = I - alpha * P #formule dans les slides
    b = (1 - alpha) * v #pareil formule slides

    #on résoud avec np
    x = np.linalg.solve(M, b)

    #normalisation finale c'est dans les consignes (somme = 1)
    x = x / np.sum(x)

    print("PageRank (méthode système linéaire) :")
    print(x)

    return x

def pageRankPower():
    return 0
def randowWalk():
    return 0