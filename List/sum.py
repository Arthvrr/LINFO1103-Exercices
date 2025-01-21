from liste import List

def somme(l):

    def somme_helper(l,total=0):
        
        if l.is_empty():
            return total
        
        head = l.head()
        tail = l.tail()

        total += head

        return somme_helper(tail,total)
    
    if l.is_empty():
        return 0
    
    return somme_helper(l)


# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
print(l6)
print(somme(l6))