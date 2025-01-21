from binary_tree import BinaryTree

def size(tree):
    if tree.is_empty():
        return 0
    
    return 1 + size(tree.left()) + size(tree.right())


arbre = BinaryTree()

arbre.insert(23)
arbre.insert(14)
arbre.insert(9)
arbre.insert(35)
arbre.insert(28)
arbre.insert(5)
arbre.insert(17)

print(size(arbre))

arbre2 = BinaryTree()
arbre2.insert(4)
arbre2.insert(6)
arbre2.insert(2)

print(size(arbre2))