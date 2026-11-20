import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y - x*y

x0 = 0
y0 = 1
h = 0.1
xn = 1

x = np.arange(x0, xn + h, h)
y = np.zeros(len(x))

y[0] = y0

for i in range(len(x) - 1):
    y[i + 1] = y[i] + h * f(x[i], y[i])

print("x\t\ty")
for i in range(len(x)):
    print(f"{x[i]:.2f}\t\t{y[i]:.6f}")

plt.plot(x, y, 'o-', label="Euler Method")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler's Method for IVP of ODE")
plt.grid()
plt.legend()
plt.show()
