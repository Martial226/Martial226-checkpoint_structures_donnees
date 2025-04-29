# Problème 1 : Somme des éléments distincts de deux ensembles
def somme_elements_distincts(ensemble1, ensemble2):
    somme = 0
    # Étape 1 : ajouter les éléments de ensemble1 qui ne sont pas dans ensemble2
    for elem1 in ensemble1:
        if elem1 not in ensemble2:
            somme += elem1
    
    # Étape 2 : ajouter les éléments de ensemble2 qui ne sont pas dans ensemble1
    for elem2 in ensemble2:
        if elem2 not in ensemble1:
            somme += elem2
            
    return somme

