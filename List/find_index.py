from liste import List

def find_index(l,e):
    """
    Fonction permettant de retourner l'index de e dans la liste l, retourne -1 si pas présent
    """
    
    def find_index_helper(l,e,number=0):
        if l.is_empty():
            return -1
        
        head = l.head()
        tail = l.tail()

        if head == e:
            return number
        else:
            number += 1

        return find_index_helper(tail,e,number)
    
    if l.is_empty():
        return False
    return find_index_helper(l,e)




# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
print(l6)
print(find_index(l6,5))
print(find_index(l6,20))