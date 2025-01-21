from binary_tree import BinaryTree

def insert(tree,value):
    
    if tree.is_empty():
        tree.setelem(value)
        tree.setleft(BinaryTree())
        tree.setright(BinaryTree())

        #return tree #JE LE METTAIS LA

    #si l'arbre n'est pas vide et a au moins une racine
    else:
        if tree.elem() < value: #si valeur est plus grande que racine, on check à droite
            tree.right().insert(value)

        else: #si valeur est plus petite que racine, on check à gauche
            tree.left().insert(value)
    
    return tree


arbre = BinaryTree()

arbre.insert(10)
arbre.insert(5)
arbre.insert(15)
arbre.insert(3)
arbre.insert(7)
arbre.insert(12)
arbre.insert(17)
print(arbre)