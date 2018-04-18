def sort5(a):
    
    if len(a) < 2: return a
    pequeno = sort5([x for x in a[1:] if x <= a[0]]) 
    grande = sort5([x for x in a[1:] if x > a[0]]) 
    return sum([pequeno, [a[0]], grande], [])

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
