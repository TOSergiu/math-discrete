import numpy as np
import matplotlib.pyplot as plt

def pageRankLinear(a: np.matrix, alpha: float, v: np.array):
    """
        – Input : Une matrice d’adjacence 1 A d’un graphe dirigé, 
        pondéré et régulier G, un vecteur de personnalisation v, 
        ainsi qu’un paramètre de téléportation α compris entre 0
        et 1 (0.9 par défaut et pour les résultats à présenter).
        Toutes ces valeurs sont non-négatives.

        – Output : Un vecteur x contenant les scores d’importance des noeuds ordonnés dans
        le même ordre que les lignes de la matrice d’adjacence (représentant les noeuds).
    """

def pageRankPower():

def randomWalk(A: np . matrix , alpha : float , v : np . array ):
    """
    – Input : Une matrice d’adjacence A d’un graphe dirigé, pondéré et régulier G, un vecteur de personnalisation v, ainsi qu’un paramètre de téléportation α compris entre 0
    et 1 (0.9 par défaut et pour les résultats à présenter).
    – Output : Un vecteur x contenant les scores d’importance des noeuds ordonnés dans
    le même ordre que les lignes de la matrice d’adjacence (représentant les noeuds).
    """
    n = A.shape[0]

    # Normaliser la matrice d'adjacence
    D_inv = np.diag(1 / np.sum(A, axis=1).A1)
    P = np.zeros((n, n))

    # Initialiser le vecteur de scores
    x = np.ones(n) / n

    # Itérer jusqu'à convergence
    for k in range(100):
        P[current] += 1

        if np.random.rand() < alpha and A[current].sum() > 0:
            # suivre un lien
            outgoing = np.where(A[current] > 0)[1]
            current = np.random.choice(outgoing)
        else:
            # téléportation
            current = np.random.randint(0, n)

    # normalisation : estimation de PageRank
    x = P / P.sum()  


    print(x)
    return x
