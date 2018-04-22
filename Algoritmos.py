import random 
import time
import timeit

opcion = 1

class Algoritmos:

    def ordenar(self, A, primero, ultimo):
        for i in range (primero, ultimo):
            indiceMenor = i
            for j in range (i+1, ultimo+1):
                if A[j] < A[indiceMenor]:
                    indiceMenor = j
            if indiceMenor != i:
                A[i], A[indiceMenor] = A[indiceMenor], A[i]

    def quick_sort2(self, A, menor, mayor):
        if menor < mayor:
            p = self.particion(A, menor, mayor)
            self.quick_sort2(A, menor, p - 1)
            self.quick_sort2(A, p + 1, mayor)

    def quick_sort(self, A):
	    self.quick_sort2(A, 0, len(A)-1)

    def pivot_medio(self, A, menor, mayor):
        medio = (mayor + menor) // 2
        pivot = medio
        return pivot

    def pivot_random(self, A, menor, mayor):
        pivot = pivot=random.randint(menor,mayor)
        return pivot
	
    def particion(self, A, menor, mayor):
        if opcion == 1:
	        indiceDelPivot = self.pivot_medio(A, menor, mayor)
        if opcion == 2:
            indiceDelPivot = self.pivot_random(A, menor, mayor)
        valorDelPivot = A[indiceDelPivot]
        A[indiceDelPivot], A[menor] = A[menor], A[indiceDelPivot]
        borde = menor

        for i in range(menor, mayor + 1):
            if A[i] < valorDelPivot:
                borde += 1
                A[i], A[borde] = A[borde], A[i]
        A[menor], A[borde] = A[borde], A[menor]

        return borde
			
    def sort5(self, A):
        A0, A1, A2, A3, A4 = A[0], A[1], A[2], A[3], A[4]
        if A0 > A1:
            A0, A1 = A1, A0
        if A2 > A3:
            A2, A3 = A3, A2
        
        if A1 > A3:
            A1, A3 = A3, A1
            A1, A2 = A2, A1
            if A1 < A0:
                A1, A0 = A0, A1
            if A1 > A2:
                A1, A2 = A2, A1
        elif A0 > A2:
            A1, A2, A0 = A0, A1, A2
        elif A1 > A2:
             A1, A2 = A2, A1
        
        if A4 > A3:   
            pass
        elif A4 > A2:
            A3, A4 = A4, A3
        elif A4 > A1:
            A2, A3, A4 = A4, A2, A3
        elif A4 > A0:
            A1, A2, A3, A4 = A4, A1, A2, A3
        else:
            A0, A1, A2, A3, A4 = A4, A0, A1, A2, A3

    def median_of_medians(self, A, k):

        sublists = [(A[j:j+5]) for j in range(0, len(A), 5)]
        
        for i in range(len(sublists)):
            if len(sublists[i]) != 5:
                sublists[i] = sorted(sublists[i])
            else:
                self.sort5(sublists[i])
        
        medians = [sublist[len(sublist) // 2] for sublist in sublists]
            
        if len(medians) != 5:
            medians = sorted(medians)
        else:
            self.sort5(medians)
    
        pivot = medians[len(medians) // 2]
    
        SL = [x for x in A if x < pivot]
        SR = [x for x in A if x > pivot]
    
        if len(SL) > k:
            return self.median_of_medians(SL, k)
        elif len(SL) < k:
            return self.median_of_medians(SR, k-len(SL)-1)
        return pivot