import numpy as np

def normalize_vector(u):
    s = np.sum(u)
    if s <= 0:
        raise ValueError("Impossible.")
    return u / s

def build_P(A):
    """
    Crée la matrice de transition P, dont chaque colonne est stochastique.
    P[i,j] est la probabilité d'aller d'un noeud j à un noeud i 
    Les colonnes correspondant à des noeuds sans liens sortants sont mises à zéro.
    Retourne P 
    """
    A = np.array(A, dtype=float)
    n = A.shape[0]
    col_sums = np.sum(A, axis=0)
    P = np.zeros_like(A)
    for j in range(n):
        if col_sums[j] > 0:
            P[:, j] = A[:, j] / col_sums[j]
        else:
            P[:, j] = 0.0
    return P

def build_G(P, alpha, v):
    """
    Crée la matrice Google: G = alpha * P + (1 - alpha) * v * 1^T
    P est une matrice colonne-stochastique (chaque colonne somme à 1 ou 0).
    v est un vecteur de personnalisation (somme à 1 après normalisation).
    Retourne G
    """
    v = normalize_vector(np.array(v, dtype=float))
    n = P.shape[0]
    outer = np.outer(v, np.ones(n))   
    G = alpha * P + (1.0 - alpha) * outer
    return G

def pageRankPower(A, alpha, v, eps = 1e-12):
    """
    - Initialise x avec le vecteur des degrés entrants (indegree).
    - Applique l’itération : x_{k+1} = G @ x_k, avec normalisation après chaque étape.
    Affiche A, P, G, les 3 premières itérations, et le vecteur final.
    Retroune le vecteur final x. 
    """
    A = np.array(A, dtype=float)
    n = A.shape[0]
    v = normalize_vector(np.array(v, dtype=float))
    P = build_P(A)
    G = build_G(P, alpha, v)

    indegree = np.sum(A, axis=0)

    if np.sum(indegree) == 0:
        x = np.ones(n) / float(n)
    else:
        x = np.array(indegree, dtype=float)
        x = normalize_vector(x)

    print(A)
    print(P)
    print(G)
    print(x)

    count = 0
    x2 = x.copy()
    first_three = []
    for i in range(1000):
        count += 1
        x = G.dot(x2)   
        x = np.maximum(x, 0.0)
        x = normalize_vector(x)

        if count <= 3:
            first_three.append(x.copy())
        r = np.linalg.norm(x - x2, 1)
        x2 = x.copy()
        if r < eps:
            break