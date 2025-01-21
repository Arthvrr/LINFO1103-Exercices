from liste import List

def flatten(l):

    def flatten_helper(l,res=[]):

        if l.is_empty():
            return res
        
        head = l.head()
        tail = l.tail()

        res.append(head)

        return flatten_helper(tail,res)
    
    if l.is_empty():
        return []
    return flatten_helper(l)


def unflatten(liste):

    max = len(liste)-1
    result = List()

    while 0 <= max:

        result = result.concat(liste[max])
        max -= 1

    return result

def unflatten_invert(liste):
    idx = 0
    max = len(liste)
    result = List()

    while idx < max:
        result = result.concat(liste[idx])
        idx += 1
    
    return result


# Zone de tests
l1 = List()
l2 = l1.concat(3)
l3 = l2.concat(5)
l4 = l3.concat(2)
l5 = l4.concat(8)
l6 = l5.concat(1)
print(l6)
print(flatten(l6))


liste1 = [1, 8, 2, 5, 3]
print(unflatten(liste1))
print(unflatten_invert(liste1))