from liste import List

def unique(l):
    """
    Fonction permettant de retourner la liste l composée d'éléments uniques (pas de doublons)
    """

    def unique_helper(l,seen=set(),result=List()):

        if l.is_empty():
            return result
        
        head = l.head()
        tail = l.tail()

        if head in seen:
            return unique_helper(tail,seen,result)
        else :
            seen.add(head)
            return unique_helper(tail,seen,result).concat(head)
        

    if l.is_empty():
        return None
    
    return unique_helper(l)


# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(3)
l5 = l4.concat(3)
l6 = l5.concat(3)
print(l6)
print(unique(l6))