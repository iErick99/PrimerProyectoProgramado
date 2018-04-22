import random 
import time
import timeit

opcion = 1

class Algoritmos:

    def __init__(self, listaA ):
        self.A = listaA
    
    def printA(self):
        if self.A != None:
            print(self.A)

    def quick_sort2(self, menor, mayor):
        if menor < mayor:
            p = self.particion(menor, mayor)
            self.quick_sort2(menor, p - 1)
            self.quick_sort2(p + 1, mayor)

    def quick_sort(self):
	    self.quick_sort2(0, len(self.A)-1)

    def pivot_medio(self, menor, mayor):
        medio = (mayor + menor) // 2
        pivot = medio
        return pivot

    def pivot_random(self, menor, mayor):
        pivot = pivot=random.randint(menor,mayor)
        return pivot
	
    def particion(self, menor, mayor):
        if opcion == 1:
	        indiceDelPivot = self.pivot_medio(menor, mayor)
        if opcion == 2:
            indiceDelPivot = self.pivot_random(menor, mayor)
        valorDelPivot = self.A[indiceDelPivot]
        self.A[indiceDelPivot], self.A[menor] = self.A[menor], self.A[indiceDelPivot]
        borde = menor

        for i in range(menor, mayor + 1):
            if self.A[i] < valorDelPivot:
                borde += 1
                self.A[i], self.A[borde] = self.A[borde], self.A[i]
        self.A[menor], self.A[borde] = self.A[borde], self.A[menor]

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
        A[0], A[1], A[2], A[3], A[4] = A0, A1, A2, A3, A4

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

#Algoritmos para probar el tiempo del quick_sort

import csv

a = None

def timing_algoritmos(start, stop, step):
    global a
    results = []
    population = list(range(0, stop))
    for n in range(start, stop, step):
        size = start + n
        a = random.sample(population, size)
        print("Size={}".format(size))
        tn = timeit.timeit("Algoritmos(a).quick_sort()", number=10, globals=globals())
        results.append((size, tn))
    return results

def algoritmos_time_save(filename="data/QuickSort3.csv", start=10, stop=1000, step=100):
    results = timing_algoritmos(start, stop, step)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['i', 'n', 'time(n)'])
        for i, (n, tn) in enumerate(results):
            writer.writerow([i, n, tn])
            

algoritmos_time_save()

