import numpy as np
import itertools

n = 2000

A1 = np.linspace(0,1,n)
A2 = np.linspace(0,1,n)
A3 = np.linspace(0,1,n)
A4 = np.linspace(0,1,n)
A5 = np.linspace(0,1,n)
A6 = np.linspace(0,1,n)

comb = list(itertools.product(A1,A2))

print('done')
print(len(comb))