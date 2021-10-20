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

T=0.000001
RC=1/(2*3.141516*1000)

vo=[]
vo.append(0)
print(vo)
for k in range(len(x)-1):
    vo.append((T/RC)*y[k]+(1-T/RC)*vo[k])

plt.plot(x,vo, color='g', label="noisy data")

plt.xticks(rotation=25)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.title('Filtered Signal', fontsize=20)
plt.grid()
plt.legend()
plt.show()
