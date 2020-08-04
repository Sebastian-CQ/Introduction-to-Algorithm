from timeit import Timer
import matplotlib.pyplot as plt
import random


########################################################################################################################
# X = list(range(20000))
#
# popzero = Timer('x.pop(0)', 'from __main__ import x')
# pop = Timer('x.pop()', 'from __main__ import x')
# p1, p2 = [], []
# for i in range(2000, 50000, 1000):
#     x = list(range(i))
#     p1.append(pop.timeit(number=1000))
#     p2.append(popzero.timeit(number=1000))
#
# plt.scatter([i for i in range(len(p1))], p1, c='r')
# plt.scatter([i for i in range(len(p1))], p2, c='b')
# plt.grid()
# plt.ylim(0, 0.02)
# plt.show()


########################################################################################################################

for i in range(1000, 20000, 1000):
    t1 = Timer('random.randrange(%d) in x' % i, 'from __main__ import random, x')
    x = list(range(i))
    list_time = t1.timeit(number=1000)
    x = {j:None for j in range(i)}
    dict_time = t1.timeit(number=1000)
    print('%d,  %f,  %f' % (i, list_time, dict_time))
