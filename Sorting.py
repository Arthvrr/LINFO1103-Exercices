def bubble_sort(A):
    """
    Complexité temporelle : θ(n^2)
    O(n^2) comparaisons et swap

    Stable, en place
    """
    for i in range(len(A)-1,-1,-1):
        for j in range(1,i+1):
            if A[j-1] > A[j]:
                A[j], A[j-1] = A[j-1], A[j]

    return A


test = [1,9,3,2,8,5,4,7,6]
print(bubble_sort(test))

def bubble_sort_2(A):
    """
    Idem que bubblesort, sauf que s'il n'y a plus besoin de swap, on break
    
    Complexité temporelle: O(n^2)
    O(n^2) comparaisons et swap

    Stable, en place et adaptatif
    """
    for i in range(len(A)-1,-1,-1):
        swapped = False
        for j in range(1,i+1):
            if A[j-1] > A[j]:
                A[j], A[j-1] = A[j-1], A[j]
                swapped = True
        
        if not swapped:
            break
    return A



def selection_sort(A):
    """
    Le minimum du sous-tableau liste[i:] se met en position liste[i]
    
    Complexité temporelle: θ(n^2)    
    θ(n^2) comparaisons et O(n) swap

    En place
    """
    for i in range(0,len(A)):
        mini = i
        for j in range(i+1,len(A)):
            if A[i] < A[mini]:
                mini = j
        if mini != i:
            A[i],A[mini] = A[mini], A[i]
    return A



def insertion_sort(A):
    """
    Insère liste[i] à sa place pour chaque i, déplace les éléments plus grands de 1
    
    Complexité temporelle: O(n^2)
    O(n^2) comparaisons et swaps

    Stable, en place et adaptatif
    """
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        
        A[j+1] = key
    
    return A

"""
Stable : ne réordonnes pas les clés égales
En place : change liste donnée en input
Adaptatif : algo va plus vite pour listes quasi triées (--> O(n))


BubbleSort : theta(n^2) : O(n^2) comparaisons et swaps, stable et en place
BubbleSort2 : O(n^2) : O(n^2) comparaisons et swaps, stable, en place et adaptatif
SelectionSort : theta(n^2) : theta(n^2) comparaisons et O(n) swaps, en place
InsertionSort : O(n^2) : O(n) comparaisons et swaps, stable, en place et adaptatif


BubbleSort est pas efficace, SelectionSort est pareil mais il est mieux si on veut minimiser le nombre de swaps.
InsertionSort est toujours quadratique mais son caractère adaptatif est un plus.
"""

def linear_sort(liste):
    """
    Créé un dictionnaire pour compter le nombre d'occurences entre mini et maxi, puis recréé une nouvelle liste avec le dico
    Autrement dit, c'est un histogramme de valeurs!
    
    Complexité temporelle: θ(n+maxi-mini)
    Complexité spatiale: θ(maxi-mini)
    Note: on peut changer ça en θ(nombre de valeurs différentes) mais c'est en dehors de la matière de ce cours
    """
    maxi = max(liste)
    mini = min(liste)
    dico = {}
    for i in range(mini,maxi+1):
        dico[i] = 0
    for item in liste:
        dico[item] += 1
    result = []
    for i in range(mini,maxi+1):
        result += [i] * dico[i]
    return result


