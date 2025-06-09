from binary_tree import BinaryTree

def path_to_node(tree, value):
    """
    pre: -
    post: return a list of elements representing the path to the node with the given value
          or None if the value is not in the tree
    """
    if tree.is_empty():
        return None

    if tree.elem() == value:
        return [tree.elem()]

    left_path = path_to_node(tree.left(), value)
    if left_path: #Si left_path est différent de none, la valeur a été trouvée dans le sous-arbre de gauche
        return [tree.elem()] + left_path #On ajoute la racine actuelle à la liste

    right_path = path_to_node(tree.right(), value)
    if right_path: #Si left_path est différent de none, la valeur a été trouvée dans le sous-arbre de droite
        return [tree.elem()] + right_path #On ajoute la racine actuelle à la liste

    return None

arbre = BinaryTree()

arbre.insert(10)
arbre.insert(5)
arbre.insert(15)
arbre.insert(3)
arbre.insert(7)
arbre.insert(12)
arbre.insert(17)

print(path_to_node(arbre,3))

arbre2 = BinaryTree().insert(5).insert(3).insert(8).insert(2).insert(4)

print(path_to_node(arbre2,4))