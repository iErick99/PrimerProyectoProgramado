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
