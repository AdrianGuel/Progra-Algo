import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pend(y, t, b, c):
    return np.array([y[1], -b*y[1] - c*np.sin(y[0])])

b = 0.25
c = 5.0
y0 = np.array([np.pi - 0.1, 0.0])
t = np.linspace(0, 10, 101)

sol = odeint(pend, y0, t, args=(b, c))
plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')
plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

