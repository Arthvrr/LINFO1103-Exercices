from binary_tree import BinaryTree

def search_parent(tree,key,res=None):
    """
    pre: 'tree' une instance de BinaryTree vérifiant l'invariant d'un ABR
        'key' une clé présente ou pas dans l'ABR
        'res' mémoire un résultat temporaire, initialisé à None par défaut
    post: renvoie le (sous-)arbre enraciné au nœud parent de la première occurrence de 'key' dans 'tree',
        renvoie un arbre vide si 'key' n'appartient pas à 'tree'.
        renvoie None si la première occurrence de "key" est à la racine et n'a donc pas de parent.
        La complexité temporelle de cette méthode doit être en O(h) où h est la hauteur de l'ABR.
        L'arbre 'tree', passé en argument, ne peut *pas* être modifié.
    """
    
    if tree.is_empty():
        return BinaryTree()
    
    if tree.elem() < key: #si clé est plus grande que racine on va check à droite

        if tree.right().is_empty():
            return BinaryTree()
        
        if tree.right().elem() == key:
            return tree.right()
        return search_parent(tree.right(),key,tree)
    
    elif tree.elem() > key: #si clé est plus petite que racine on va check à gauche
        
        if tree.left().is_empty():
            return BinaryTree()
        
        if tree.left().elem() == key:
            return tree.left()
        return search_parent(tree.left(),key,tree)

    else:
        return None
    

arbre = BinaryTree()

arbre.insert(10)
arbre.insert(5)
arbre.insert(15)
arbre.insert(3)
arbre.insert(7)
arbre.insert(12)
arbre.insert(17)

print(arbre)
subtree_5 = search_parent(arbre,5)
print(subtree_5)
subtree_15 = search_parent(arbre,15)
print(subtree_15)
subtree_error = search_parent(arbre,25)
print(subtree_error)