def binary_search(A,key,low,high):

    if low > high:
        return -1
    
    mid = (low + high) // 2

    if A[mid] == key:
        return mid
    elif A[mid] < key: #Si clé est plus grande que mid, on cherche à droite
        return binary_search(A,key,mid+1,high)
    else: #Si clé est plus petite que mid, on cherche à gauche
        return binary_search(A,key,low,mid-1)


def binary_search_iter(A,key,low,high):
    
    while low <= high:
        
        mid = (low + high) // 2

        if A[mid] == key:
            return mid
        
        elif A[mid] > key:
            high = mid - 1
        
        else:
            low = mid + 1

    return -1



test = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(test,8,0,len(test)-1))
print(binary_search_iter(test,8,0,len(test)-1))