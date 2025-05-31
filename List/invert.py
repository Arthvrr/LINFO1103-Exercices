from liste import List

def inverse(l):
    """
    Fonction permettant d'inverser les éléments d'une liste l
    """

    def inverse_helper(l,result=List()):

        if l.is_empty():
            return result
        
        head = l.head()
        tail = l.tail()

        result = result.concat(head)

        return inverse_helper(tail,result)
    
    if l.is_empty():
        return None
    return inverse_helper(l)
    

# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
print(l6)
print(inverse(l6))