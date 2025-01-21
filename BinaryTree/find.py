from binary_tree import BinaryTree

def find(tree,value):
    
    if tree.is_empty():
        return False
    
    if tree.elem() == value:
        return True
    
    elif tree.elem() < value: #si valeur est plus grande que racine on check à droite
        return find(tree.right(),value)
    
    else: #si valeur est plus petite que racine on check à gauche
        return find(tree.left(),value)
    

arbre = BinaryTree()

arbre.insert(10)
arbre.insert(5)
arbre.insert(15)
arbre.insert(3)
arbre.insert(7)
arbre.insert(12)
arbre.insert(17)

print(find(arbre,15)) #TRUE
print(find(arbre,20)) #FALSE
print(find(arbre,12)) #TRUE
print(find(arbre,-5)) #FALSE