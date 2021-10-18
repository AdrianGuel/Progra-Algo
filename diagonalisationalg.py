
import numpy as np
import matplotlib.pyplot as plt
n=3
A=np.random.rand(n,n)
B=np.random.rand(n,n)

for p in range(n):
    for i in range(n):
        if i!=p:
            for j in range(n):
                A[i][j]=A[i][j]-(A[i][p]/A[p][p])*A[p][j]

print(A)
