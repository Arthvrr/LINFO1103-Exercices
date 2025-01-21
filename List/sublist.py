from liste import List

def sublist_first (self, elem):

    if self.is_empty():
        return List()
    
    if elem == self.head():
        return self
    
    return self.tail().sublist_first(elem)
