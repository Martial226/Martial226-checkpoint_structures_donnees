# Version avec une fonction dot_product
def dot_product(v1, v2):
    produit = 0
    for i in range(len(v1)):
        produit += v1[i] * v2[i]
    return produit

def verifier_orthogonalite_fonction(n, liste_vecteurs):
    for i in range(n):
        v1, v2 = liste_vecteurs[i]
        ps = dot_product(v1, v2)
        if ps == 0:
            print(f"Les vecteurs {v1} et {v2} sont orthogonaux.")
        else:
            print(f"Les vecteurs {v1} et {v2} ne sont pas orthogonaux.")


