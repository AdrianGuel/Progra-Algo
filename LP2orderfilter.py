import serial
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  # Tiempo real

plt.style.use('fivethirtyeight')  # Estilo
# Comunicación Serial
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=2);
time.sleep = 1;
t = 0;  # Señal Ruidosa
d_señal = [];
dp_señal = [];  # Graficar
d_filtro = [];
d_filtro2 = [];
tiempo = [];

while (t <= 0.5):
    señal = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 50 * t);  # Señal de Prueba
    t = t + 0.001;  # Muestras - 1000
    d_señal.append(str(señal));
    dp_señal.append(señal);
    tiempo.append(t);

# Graficacion en tiempo real
fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-2.5, 2.5))
line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)

def animate(l):
    line.set_data(tiempo[:l], d_filtro2[:l])
    line2.set_data(tiempo[:l], dp_señal[:l])
    return line, line2,

cuenta = 0;

for i in d_señal:
    arduino.write((i + '\n').encode());
    salida = arduino.readline().decode('ascii');
    d_filtro.append(salida);
    d_filtro[0] = "0.00\r\n";  # Valor que no cambia. sin0 = 0
    strorg = d_filtro[cuenta];
    strnew = strorg.replace('\r\n', '');
    d_filtro2.append(float(strnew));
    cuenta = cuenta + 1;

arduino.close();

anim = FuncAnimation(fig, animate, interval=1)
plt.show()
