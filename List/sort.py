from liste import List

def sort(l):
    """
    Fonction permettant de trier une liste l
    """

    if l.is_empty():
        return l

    elements = []
    current = l
    while not current.is_empty():
        elements.append(current.head())
        current = current.tail()

    elements.sort()

    sorted_list = List()
    for elem in reversed(elements):
        sorted_list = sorted_list.concat(elem)

    return sorted_list

# Tests
l1 = List()
l1 = l1.concat(4).concat(7).concat(9).concat(2).concat(5)
print("Avant tri :", l1)
sorted_l = sort(l1)
print("Après tri :", sorted_l)