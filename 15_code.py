import numpy as np
import matplotlib.pyplot as plt

def f(x, y, z):
    return -np.pi**2 * np.sin(np.pi * x)

a = 0
b = 1
alpha = 0
beta = 0

h = 0.01
s1 = 0
s2 = 4

def solve(s):
    x = np.arange(a, b + h, h)
    y = np.zeros(len(x))
    z = np.zeros(len(x))

    y[0] = alpha
    z[0] = s

    for i in range(len(x) - 1):
        k1y = h * z[i]
        k1z = h * f(x[i], y[i], z[i])

        k2y = h * (z[i] + k1z / 2)
        k2z = h * f(x[i] + h/2, y[i] + k1y/2, z[i] + k1z/2)

        k3y = h * (z[i] + k2z / 2)
        k3z = h * f(x[i] + h/2, y[i] + k2y/2, z[i] + k2z/2)

        k4y = h * (z[i] + k3z)
        k4z = h * f(x[i] + h, y[i] + k3y, z[i] + k3z)

        y[i+1] = y[i] + (k1y + 2*k2y + 2*k3y + k4y) / 6
        z[i+1] = z[i] + (k1z + 2*k2z + 2*k3z + k4z) / 6

    return x, y

for i in range(20):
    x, y1 = solve(s1)
    x, y2 = solve(s2)

    if abs(y2[-1] - y1[-1]) < 1e-10:
        break

    s = s2 + (beta - y2[-1]) * (s2 - s1) / (y2[-1] - y1[-1])

    s1 = s2
    s2 = s

x, y = solve(s2)

print("Initial slope =", s2)
print("Boundary value y(b) =", y[-1])

plt.plot(x, y, label="Shooting Method")
plt.plot(x, np.sin(np.pi*x), '--', label="Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Shooting Method for BVP")
plt.grid()
plt.legend()
plt.show()
