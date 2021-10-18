import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
N=100
n=4
t=np.linspace(0,10,N,endpoint=True)
y=np.power(t,4)
Phi=np.vander(t,n)
x=np.matmul(np.matmul(inv(np.matmul(np.transpose(Phi),Phi)),np.transpose(Phi)),np.transpose(y))

f=x[0]*np.power(t,n-1)
for i in range(1,n):
    f+=x[i]*np.power(t,n-(i+1))
    
plt.plot(t,f,'k')
plt.plot(t,y,'b')
plt.show()
