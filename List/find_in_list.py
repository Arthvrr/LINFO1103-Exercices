from liste import List

def find_in_list(l,e,k):
    """
    Fonction permettant de retourner la sous-liste telle que la k-ième occurence de e est la head de la liste 
    """

    if l.is_empty():
        return None
    
    if l.head() == e:

        if k == 1:
            return l
        
        else:
            k -= 1

    return find_in_list(l.tail(),e,k)
        


# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
l7 = l6.concat(3)
print(l7)
print(find_in_list(l7,3,2)) #doit retourner [3[]]
print(find_in_list(l7,2,1)) #doit retourner [2[5[3[]]]]
print(find_in_list(l7,2,2)) #doit retourner None
