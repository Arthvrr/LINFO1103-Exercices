from binary_tree import BinaryTree

def delete(tree,value):
    
    if tree.is_empty(): #arbre est vide, rien à supprimer
        return tree

    #on va dans le sous-arbre de gauche si la valeur est plus petite que la racine
    if value < tree.elem():
        tree.setleft(delete(tree.left(), value))
    
    #on va dans le sous-arbre de droite si la valeur est plus grande que la raince
    elif value > tree.elem():
        tree.setright(delete(tree.right(), value))
    
    # si la valeur est égal à la racine (c'est l'élément à supprimer)
    else:
        #Cas 1 : le noeud est une feuille 
        if tree.left().is_empty() and tree.right().is_empty():
            return BinaryTree()  # Remplacer le nœud par un arbre vide
        
        #Cas 2 : le noeud a un seul sous-arbre (gauche ou droit)
        elif tree.left().is_empty():
            return tree.right()  # Remplacer le nœud par son sous-arbre droit
        elif tree.right().is_empty():
            return tree.left()   # Remplacer le nœud par son sous-arbre gauche

        #Cas 3 : le noeud a deux enfants
        else:
            #Trouver le successeur (le plus petit élément dans le sous-arbre droit)
            min_larger_node = find_min(tree.right())
            tree.setelem(min_larger_node.elem())  # Remplacer l'élément du nœud courant
            #Supprimer le successeur dans le sous-arbre droit
            tree.setright(delete(tree.right(), min_larger_node.elem()))
    
    return tree

def find_min(tree):
    """
    Fonction utilitaire pour trouver le nœud ayant la plus petite valeur dans un sous-arbre.
    """
    current = tree
    while not current.left().is_empty():
        current = current.left()
    return current

arbre = BinaryTree()

arbre.insert(10)
arbre.insert(5)
arbre.insert(15)
arbre.insert(3)
arbre.insert(7)
arbre.insert(12)
arbre.insert(17)
print(arbre)
delete(arbre,12)
print(arbre)
delete(arbre,7)
print(arbre)