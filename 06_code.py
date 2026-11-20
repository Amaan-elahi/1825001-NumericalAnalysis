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
    k1 = h * f(x[i], y[i])
    k2 = h * f(x[i] + h/2, y[i] + k1/2)
    k3 = h * f(x[i] + h/2, y[i] + k2/2)
    k4 = h * f(x[i] + h, y[i] + k3)

    y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6

print("x\t\ty")
for i in range(len(x)):
    print(f"{x[i]:.2f}\t\t{y[i]:.6f}")

plt.plot(x, y, 'o-', label="RK4")
plt.xlabel("x")
plt.ylabel("y")
plt.title("RK4 Method for IVP of ODE")
plt.grid()
plt.legend()
plt.show()
