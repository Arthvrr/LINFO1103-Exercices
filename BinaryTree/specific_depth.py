from binary_tree import BinaryTree

def specific_depth(tree,depth):
    """
    pre: 'tree' une instance de BinaryTree vérifiant l'invariant d'un ABR
         'depth' la profondeur de l'arbre à laquelle on regarde pour le nombre de noeuds étant à cette profondeur
    post: retourne le nombre de noeuds de l'arbre se situant à la profondeur 'depth'
    La profondeur de la racine est 0
    """

    if tree.is_empty():
        return 0
    
    elif depth == 0:
        return 1
    else:
        return specific_depth(tree.left(),depth-1) + specific_depth(tree.right(),depth-1)

arbre = BinaryTree()

arbre.insert(23)
arbre.insert(14)
arbre.insert(9)
arbre.insert(35)
arbre.insert(28)
arbre.insert(5)
arbre.insert(17)

print(specific_depth(arbre,1))