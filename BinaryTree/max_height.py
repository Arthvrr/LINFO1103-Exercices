from binary_tree import BinaryTree

def max_height(tree):
    
    if tree.is_empty():
        return 0
    
    left_height = max_height(tree.left())
    right_height = max_height(tree.right())

    return 1 + max(left_height,right_height)


a1 = BinaryTree()

a1.insert(10)
a1.insert(20)
a1.insert(30)
a1.insert(40)
a1.insert(50)
a1.insert(60)
a1.insert(-10)
a1.insert(-20)
a1.insert(-30)

print(max_height(a1))