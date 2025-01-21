from binary_tree import BinaryTree

def preorder(tree): #RGD
    if tree.is_empty():
        return []
    return [tree.elem()] + preorder(tree.left()) + preorder(tree.right())

def inorder(tree): #GRD
    if tree.is_empty():
        return []
    return inorder(tree.left()) + [tree.elem()] + inorder(tree.right())

def postorder(tree): #GDR
    if tree.is_empty():
        return []
    return postorder(tree.left()) + postorder(tree.right()) + [tree.elem()]


arbre = BinaryTree()

arbre.insert(10)
arbre.insert(5)
arbre.insert(15)
arbre.insert(3)
arbre.insert(7)
arbre.insert(12)
arbre.insert(17)

# print(preorder(arbre)) #10 5 3 7 15 12 17
# print(inorder(arbre)) #3 5 7 10 12 15 17
# print(postorder(arbre)) #3 7 5 12 17 15 10


arbre2 = BinaryTree()
arbre2.insert(0)
arbre2.insert(-3)
arbre2.insert(6)
arbre2.insert(-7)
arbre2.insert(-1)
arbre2.insert(4)
arbre2.insert(9)

print(preorder(arbre2)) #0 -3 -7 -1 6 4 9
print(inorder(arbre2)) #-7 -3 -1 0 4 6 9
print(postorder(arbre2)) #-7 -1 -3 4 9 6 0