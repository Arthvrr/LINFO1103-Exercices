from liste import List

def cum_sum(l):
    """
    Fonction permettant de retourner une liste étant la somme cumulée de la liste l
    """

    def cum_sum_helper(l,somme=0,result=List()):
        
        if l.is_empty():
            return result
        
        head = l.head()
        tail = l.tail()

        somme += head
        return cum_sum_helper(tail,somme,result).concat(somme)
    
    if l.is_empty():
        return List()
    else:
        return cum_sum_helper(l)
        


# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
print(l6)
print(cum_sum(l6))
