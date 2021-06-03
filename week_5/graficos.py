import matplotlib.pyplot as plt

x1 = [2,5,7,15]
y1 = [11,22,33,44]
x2 = [5,10,5,8]
y2 = [11,22,33,44]

plt.plot(x1, y1, color='green', linewidth=3, label='linea1')
plt.plot(x2, y2, color='yellow', linewidth=5, label='linea1')
plt.title('Gráfica plt')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid()
plt.legend()

plt.show()
