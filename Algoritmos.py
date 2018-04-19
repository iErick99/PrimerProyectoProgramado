class Algoritmos:

def quick_sort(A):
	quick_sort2(A, 0, len(A)-1)
	
def quick_sort2(A, menor, mayor):
    if (mayor-menor < maximo) and (menor < mayor): 
        ordenar(A, menor, mayor)
    elif menor < mayor:
        p = particion(A, menor, mayor)
        quick_sort2(A, menor, p - 1)
        quick_sort2(A, p + 1, mayor)

def pivot_medio(A, menor, mayor):
	medio = (mayor + menor) // 2
	pivot = medio
	return pivot
	
def particion(A, menor, mayor):
	indiceDelPivot = pivot_medio(A, menor, mayor)
	valorDelPivot = A[indiceDelPivot]
	A[indiceDelPivot], A[menor] = A[menor], A[indiceDelPivot]
	borde = menor

	for i in range(menor, mayor+1):
		if A[i] < valorDelPivot:
			borde += 1
			A[i], A[borde] = A[borde], A[i]
	A[menor], A[borde] = A[borde], A[menor]

	return (borde)
	
def ordenar(A, primero, ultimo):
    for i in range (primero, ultimo):
        indiceMenor = i
        for j in range (i+1, ultimo+1):
             if A[j] < A[indiceMenor]:
                indiceMenor = j
        if indiceMenor != i:
            A[i], A[indiceMenor] = A[indiceMenor], A[i]
			
def sort5(A):
    
    if len(A) < 2: return A
    pequeno = sort5([x for x in A[1:] if x <= A[0]]) 
    grande = sort5([x for x in A[1:] if x > A[0]]) 
    return sum([pequeno, [A[0]], grande], [])

def median_of_medians(A, k):
    
    sublists = [sort5(A[j:j+5]) for j in range(0, len(A), 5)]
    medians = [sublist[len(sublist) // 2] for sublist in sublists]
    medians = sort5(medians)
    
    pivot = medians[len(medians) // 2]
    
    SL = [x for x in A if x < pivot]
    SR = [x for x in A if x > pivot]
    
    if len(SL) > k:
        return median_of_medians(SL, k)
    elif len(SL) < k:
        return median_of_medians(SR, k-len(SL)-1)
    return pivot

