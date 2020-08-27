import numpy as np
import math


def Hire_Assistant(n):
    num = 1
    best_value = np.random.rand()
    for i in range(n):
        value = np.random.rand()
        if value > best_value:
            best_value = value
            num += 1
    return num


print(Hire_Assistant(1000))
print(math.log(1000))