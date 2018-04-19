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
        if (mayor - menor < mayor) and (menor < mayor): 
            self.ordenar(A, menor, mayor)
        if (mayor-menor < mayor) and (menor < mayor): 
            self.ordenar(A, menor, mayor)
        elif menor < mayor:
            p = self.particion(A, menor, mayor)
            self.quick_sort2(A, menor, p - 1)
            self.quick_sort2(A, p + 1, mayor)

    def quick_sort(self, A):
	    self.quick_sort2(A, 0, len(A)-1)

    def pivot_medio(self, A, menor, mayor):
	    medio = (mayor + menor) // 2
	    pivot = medio
	    return pivot
	
    def particion(self, A, menor, mayor):
	    indiceDelPivot = self.pivot_medio(A, menor, mayor)
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
    
        if len(A) < 2: return A
        pequeno = self.sort5([x for x in A[1:] if x <= A[0]]) 
        grande = self.sort5([x for x in A[1:] if x > A[0]]) 
        return sum([pequeno, [A[0]], grande], [])

    def median_of_medians(self, A, k):
    
        sublists = [self.sort5(A[j:j+5]) for j in range(0, len(A), 5)]
        medians = [sublist[len(sublist) // 2] for sublist in sublists]
        medians = self.sort5(medians)
    
        pivot = medians[len(medians) // 2]
    
        SL = [x for x in A if x < pivot]
        SR = [x for x in A if x > pivot]
    
        if len(SL) > k:
            return self.median_of_medians(SL, k)
        elif len(SL) < k:
            return self.median_of_medians(SR, k-len(SL)-1)
        return pivot


A = [2,4,5,1,2]

A2 = Algoritmos()

A2.quick_sort(A)

print(A)