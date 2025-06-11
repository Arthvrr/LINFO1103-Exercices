from binary_tree import BinaryTree

def node_depth(tree,node):
    """
    pre: 'tree' une instance de BinaryTree vérifiant l'invariant d'un ABR
         'node' la valeur du noeud dont on souhaite connaître la profondeur
    post: retourne la profondeur du noeud 'node' dans l'arbre 'tree'
    La profondeur de la racine est 0
    """

    if tree.is_empty(): #Noeud pas dans l'arbre
        return -1
    
    elif tree.elem() == node:
        return 0
    else:
        left = node_depth(tree.left(), node)
        right = node_depth(tree.right(), node)
        if right == left:
            return -1
        else:
            return 1 + max(right, left)



arbre = BinaryTree()
arbre.insert(15)
# Niveau 1
arbre.insert(10)
arbre.insert(20)

# Niveau 2
arbre.insert(5)
arbre.insert(12)
arbre.insert(17)
arbre.insert(25)

# Niveau 3
arbre.insert(3)
arbre.insert(7)
arbre.insert(11)
arbre.insert(13)
arbre.insert(16)
arbre.insert(18)
arbre.insert(22)
arbre.insert(27)

print(node_depth(arbre,15))
print(node_depth(arbre,10))
print(node_depth(arbre,12))
print(node_depth(arbre,7))