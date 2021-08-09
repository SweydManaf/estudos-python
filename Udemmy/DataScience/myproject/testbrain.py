import matplotlib.pyplot as plt

x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4]

plt.plot(x, y)
plt.scatter(x, y)
plt.axhline(0, color='red')
plt.axvline(0, color='red')

plt.grid()
for xis in range(len(x)-1):
    plt.annotate(f'({str(x[xis])}, {str(y[xis])})', (x[xis], y[xis]))
plt.show()