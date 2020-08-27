import numpy as np


def Randomized_Hire_Assistant(alist):
    # randomly permute the list of candidate
    length = len(alist)
    blist = Permute_by_Sorting(alist)

    best_num = 0
    per_best = blist[1]
    for i in range(length):
        if blist[i] > per_best:
            per_best = blist[i]
            best_num += 1
    return best_num


def Permute_by_Sorting(alist):
    length = len(alist)

    blist = np.random.randint(low=0, high=length^3, size=length)
    blist = [i for i, v in sorted(enumerate(blist), key=lambda x:x[1], reverse=False)]

    alist = alist[blist]
    return alist


print(Randomized_Hire_Assistant(np.random.random(100)))
print(np.log(100))


# 5.4
def Probability(n):
    pro = 1
    m = n
    while True:
        pro = pro * m/n
        m -= 1
        if pro <= 1/2:
            break
    return n-m


print(Probability(365))