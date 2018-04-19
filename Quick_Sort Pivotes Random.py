import random
import time

def particion(A, menor, mayor):
    pivot = A[menor]
    i = menor - 1
    j = mayor + 1
 
    while True :
        while True:
            i += 1
            if A[i] < pivot:
                break
        while True:
            j -= 1
            if A[j] > pivot :
                break

        if i >= j : return j

        A[i], A[j] = A[j], A[i]
    
def particion_random(A, menor, mayor):
    random1 = menor + random.seed(time.time()) % (mayor - menor)
    A[random1], A[menor] = A[menor], A[random1]
    return particion(A, menor, mayor)

 
def quickSort(A, menor,mayor):
    if menor < mayor :
        pi = particion_random(A, menor, mayor)
        quickSort(A, menor, pi)
        quickSort(A, pi + 1, mayor)


 
def printArray(A):
    print(A)


A = [ 10, 7, 8, 9, 1, 5 ]


quickSort(A, 0, len(A) - 1)
#print(printArray(A))
