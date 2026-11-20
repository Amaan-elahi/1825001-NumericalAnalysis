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

# First step using RK4
k1 = h * f(x[0], y[0])
k2 = h * f(x[0] + h/2, y[0] + k1/2)
k3 = h * f(x[0] + h/2, y[0] + k2/2)
k4 = h * f(x[0] + h, y[0] + k3)

y[1] = y[0] + (k1 + 2*k2 + 2*k3 + k4) / 6

# Simpson's 1/3 predictor-corrector
for i in range(1, len(x) - 1):

    y_predict = y[i] + h * f(x[i], y[i])

    y_next = y_predict

    for _ in range(10):
        y_next = y[i-1] + (h/3) * (
            f(x[i-1], y[i-1])
            + 4*f(x[i], y[i])
            + f(x[i+1], y_next)
        )

    y[i+1] = y_next

print("x\t\ty")

for i in range(len(x)):
    print(f"{x[i]:.2f}\t\t{y[i]:.6f}")

plt.plot(x, y, 'o-', label="Simpson's 1/3 Method")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Simpson's 1/3 Method for ODE")
plt.grid()
plt.legend()
plt.show()
