from binary_tree import BinaryTree

def count_leaves(tree):
    """
    pre: 'tree' une instance de BinaryTree vérifiant l'invariant d'un ABR
    post: return the number of leaf nodes in the binary tree
    """
    if tree.is_empty():
        return 0
    if tree.left().is_empty() and tree.right().is_empty():
        return 1
    return count_leaves(tree.left()) + count_leaves(tree.right())


arbre = BinaryTree()

arbre.insert(10)
arbre.insert(5)
arbre.insert(15)
arbre.insert(3)
arbre.insert(7)
arbre.insert(12)
arbre.insert(17)

print (count_leaves(arbre))