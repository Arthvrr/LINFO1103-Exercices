class BinaryTree:
    def __init__(self, elem=None):
        """
        pre:  -
        post: initialize a new Binary Tree with "elem" stored at the root node,
              when "elem" is None, this is interpreted as an empty BinaryTree
        """
        self.root_elem = elem   # An element at the root
        if elem is not None:
            self.left_tree = BinaryTree()   # A reference to the left subtree
            self.right_tree = BinaryTree()  # A reference to the right subtree
        else:
            self.left_tree = None
            self.right_tree = None

    def __str__(self):
        """
        pre: -
        post: return the BinaryTree content as a string following a prefix order
        """
        if self.is_empty():
            return '[]'
        return '[' + str(self.elem()) + str(self.left()) + str(self.right()) + ']'

    def is_empty(self):
        """
        pre: -
        post: return a boolean True if the BinaryTree is empty, False otherwise
        """
        return self.root_elem is None

    def elem(self):
        """
        pre: current Tree is not empty
        post: return the element at the root of the current Tree
        """
        if self.is_empty():
            raise RuntimeError('Cannot get the root element from an empty tree')
        return self.root_elem

    def setelem(self, elem):
        """
        pre: elem is not None
        post: the root element of the current BinaryTree is set to elem
        """
        if elem is None:
            raise RuntimeError('setelem requires "elem" to be different from None')
        self.root_elem = elem

    def left(self):
        """
        pre: current Tree is not empty
        post: return the left subtree of the current BinaryTree
        """
        if self.is_empty():
            raise RuntimeError('Cannot get the left subtree of an empty tree')
        return self.left_tree

    def setleft(self, tree):
        """
        pre: -
        post: the left subtree of the current BinaryTree is set to "tree"
        """
        if not isinstance(tree, BinaryTree):
            raise RuntimeError('setleft requires "tree" to be a BinaryTree')
        self.left_tree = tree

    def right(self):
        """
        pre: current Tree is not empty
        post: return the right subtree of the current BinaryTree
        """
        if self.is_empty():
            raise RuntimeError('Cannot get the right subtree of an empty tree')
        return self.right_tree

    def setright(self, tree):
        """
        pre: -
        post: the right subtree of the current BinaryTree is set to "tree"
        """
        if not isinstance(tree, BinaryTree):
            raise RuntimeError('setright requires "tree" to be a BinaryTree')
        self.right_tree = tree

    #MÉTHODES IMPLÉMENTÉES
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