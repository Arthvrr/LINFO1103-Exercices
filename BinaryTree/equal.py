from binary_tree import BinaryTree

def __eq__(tree,other):
    
    if not isinstance(tree,BinaryTree()): #si other n'est pas de type BinaryTree, False
        return False
    
    if tree.is_empty() and other.is_empty():
        return True
    
    if tree.is_empty() or other.is_empty():
        return False
    
    return (
        tree.elem() == other.elem() and
        tree.left() == other.left() and
        tree.right() == other.right()
    )

b1 = BinaryTree()
b1.insert(12)
b1.insert(4)
b1.insert(20)
b1.insert(8)
b1.insert(16)

b2 = BinaryTree()
b2.insert(12)
b2.insert(4)
b2.insert(20)
b2.insert(8)
b2.insert(16)

print(b1 == b2)

b3 = BinaryTree()
b3.insert(15)
b3.insert(5)
b3.insert(25)

print(b1 == b3)