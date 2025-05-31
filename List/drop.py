from liste import List

def drop(l,n):
    """
    Fonction permettant de supprimer les n premiers éléments de la liste l
    """
    
    def drop_helper(l,counter=0):

        if l.is_empty():
            return l
        
        head = l.head()
        tail = l.tail()
        
        if n == counter:
            return l
        
        counter+= 1

        return drop_helper(tail,counter)
        
    
    if l.is_empty():
        return None
    
    return drop_helper(l)

# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
print(l6)
print(drop(l6,2))