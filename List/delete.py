from liste import List

def delete(l,e):

    if l.is_empty():
        return l
    
    head = l.head()
    tail = l.tail()

    if head == e:
        return delete(tail,e)
    else:
        return delete(tail,e).concat(head)
    



l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
print(l6)
l7 = (delete(l6,5))
print(l7)
l8 = (delete(l7,8))
print(l8)