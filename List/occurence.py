from liste import List

def find_occurence(l,e):
    """
    Fonction permettant de retourner le nombre d'occurences de e dans la liste l, retourne 0 si pas présent
    """

    def find_occurence_helper(l,e,count=0):

        if l.is_empty():
            return count
        
        head = l.head()
        tail = l.tail()

        if head == e:
            count+=1
        return find_occurence_helper(tail,e,count)
    
    if l.is_empty():
        return 0
    return find_occurence_helper(l,e)

# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(5)
l6 = l5.concat(1)
print(l6)
print(find_occurence(l6,5))
print(find_occurence(l6,20))