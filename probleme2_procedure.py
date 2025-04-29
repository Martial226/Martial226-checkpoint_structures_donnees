# Définition de la procédure dot_product utilisant une variable de sortie
def dot_product(v1, v2, ps):
    ps[0] = 0
    for i in range(len(v1)):
        ps[0] += v1[i] * v2[i]

# Vérifie si les vecteurs sont orthogonaux
def verifier_orthogonalite(n, liste_vecteurs):
    for i in range(n):
        v1, v2 = liste_vecteurs[i]
        ps = [0]  # Liste utilisée pour simuler une variable de sortie
        dot_product(v1, v2, ps)
        if ps[0] == 0:
            print(f"Les vecteurs {v1} et {v2} sont orthogonaux.")
        else:
            print(f"Les vecteurs {v1} et {v2} ne sont pas orthogonaux.")

