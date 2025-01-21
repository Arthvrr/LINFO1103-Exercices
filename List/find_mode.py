from liste import List

def find_mode(l):

    def find_mode_helper(l,dico={},mode=0,maxi=0):

        if l.is_empty():
            return mode
        
        head = l.head()
        tail = l.tail()

        if head not in dico:
            dico[head] = 1
        
        else:
            dico[head] += 1

        if dico[head] > maxi:
            mode = head
            maxi = dico[head]
        
        return find_mode_helper(tail,dico,mode,maxi)
    
    if l.is_empty():
        return None
    return find_mode_helper(l)
    

# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(3)
l4 = l3.concat(2)
l5 = l4.concat(2)
l6 = l5.concat(1)
print(l6)
print(find_mode(l6))
        