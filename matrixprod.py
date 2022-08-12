import numpy as np  
n=2 #orden
A = np.random.randint(10, size=(n,n))
B= np.random.randint(10, size=(n,n))
C=np.zeros((n,n))
# producto calculando C_ij https://en.wikipedia.org/wiki/Matrix_multiplication
for i in range(0,n):
  for j in range(0,n):
    for k in range(0,n):
      C[i][j]+=A[i][k]*B[k][j]

#imprimir resultado
print(A)
print(B)
print(C)
