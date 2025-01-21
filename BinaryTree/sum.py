from binary_tree import BinaryTree

def somme(tree):
    if tree.is_empty():
        return 0
    
    return tree.elem() + somme(tree.left()) + somme(tree.right())


arbre = BinaryTree()

arbre.insert(23)
arbre.insert(14)
arbre.insert(9)
arbre.insert(35)
arbre.insert(28)
arbre.insert(5)
arbre.insert(17)

print(somme(arbre))

arbre2 = BinaryTree()
arbre2.insert(4)
arbre2.insert(6)
arbre2.insert(2)

print(somme(arbre2))