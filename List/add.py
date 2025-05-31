from liste import List

def add(l,e,idx):
    """
    Fonction permettant d'ajouter l'élément e à l'index idx de la liste l
    """

    def add_helper(l,e,idx,counter=0):

        if l.is_empty():
            raise IndexError("erreur !")
        
        head = l.head()
        tail = l.tail()

        if counter == idx:
            return l.concat(e)
        
        return (add_helper(tail, e, idx, counter + 1)).concat(head)
    
    if l.is_empty():
        return [e]
    return add_helper(l,e,idx)

    
# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
print(l6)
print(add(l6,4,4))

#liste vide
l12 = List()
print(add(l12,12,20))
        
        