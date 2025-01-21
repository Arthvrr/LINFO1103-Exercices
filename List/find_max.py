from liste import List

def find_max(l):
    
    def find_max_helper(l,maxi=float('-inf')):
        
        if l.is_empty():
            return maxi
        
        head = l.head()
        tail = l.tail()

        if head > maxi:
            maxi = head

        return find_max_helper(tail,maxi)
    
    if l.is_empty():
        return None
    return find_max_helper(l)








# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
print(l6)
print(find_max(l6))

l = List()
l = l.concat(10)
print(find_max(l))