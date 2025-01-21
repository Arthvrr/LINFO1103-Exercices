def merge_sort(liste):
    def merge(partie1,partie2):
        result = []
        i = 0 ; j = 0

        while i < len(partie1) and j < len(partie2):

            if partie1[i] < partie2[j]:
                result.append(partie1[i])
                i += 1

            else:
                result.append(partie2[j])
                j += 1

        while i < len(partie1):
            result.append(partie1[i])
            i += 1
        
        while j < len(partie2):
            result.append(partie2[j])
            j += 1

        return result
    
    n = len(liste)

    if n == 1:
        return liste
    return merge(merge_sort(liste[:n//2]),merge_sort(liste[n//2:]))

test = [40,30,80,10,70,50,90,20,60]
print(merge_sort(test))