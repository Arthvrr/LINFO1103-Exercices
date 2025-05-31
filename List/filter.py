from liste import List

def filter_pair(l):
    """
    Fonction permettant de filtrer la liste pour ne garder que les éléments pair de la liste l
    """

    def filter_pair_helper(l):
    
        if l.is_empty():
            return l
        
        head = l.head()
        tail = l.tail()

        if head % 2 == 0:
            return filter_pair_helper(tail).concat(head)
        else:
            return filter_pair_helper(tail)
        
    if l.is_empty():
        return None
    else:
        return filter_pair_helper(l)
    


# Zone de tests
l1 = List()
l2 = l1.concat(6)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(3)
print(l6)
print(filter_pair(l6))