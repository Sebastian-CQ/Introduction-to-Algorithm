import numpy as np
import time


def Bucket_Sort(alist):
    n = len(alist)
    blist = []
    for i in range(n):
        blist.append([])

    for j in range(n):
        blist[int(alist[j])].append(alist[j])

    for k in range(n):
        blist[k].sort()

    return np.concatenate(blist)


A = np.random.random(10000)
start = time.time()
Bucket_Sort(A)
end = time.time()
print(end - start)
