from liste import List

def length(l):

    def length_helper(l,num=0):
        
        if l.is_empty():
            return num
        
        head = l.head()
        tail = l.tail()

        num += 1

        return length_helper(tail,num)
    
    if l.is_empty():
        return 0
    return length_helper(l)

# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(3)
l4 = l3.concat(2)
l5 = l4.concat(2)
l6 = l5.concat(1)
print(l6)
print(length(l6))