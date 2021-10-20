import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('noisysignalfile.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x, y, color='g', label="noisy data")

plt.xticks(rotation=25)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.title('Noisy Signal', fontsize=20)
plt.grid()
plt.legend()
plt.show()
