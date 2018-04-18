from median_of_median import median_of_medians
import random
import time

def fact_tail(m):
    def facting(n, f):
        print("n = {}  f = {}".format(n, f))
        if n == 0 : return f
        return facting(n - 1, n * f)
    return facting(m, 1)

A = [8, 33, 17, 51, 57, 49, 35, 11, 25, 37, 14, 3, 2, 13, 
     52, 12, 6, 29, 32, 54, 5, 16, 22, 23, 7]

B = []

sum = 0

for i in range(50):
    sum += fact_tail(i)
    time.sleep(1)
    B.append(i)
    print(sum)

print(median_of_medians(B, len(B) // 2))