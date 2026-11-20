import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
n = 20

alpha = 0
beta = 0

h = (b - a) / n
x = np.linspace(a, b, n + 1)

A = np.zeros((n - 1, n - 1))
B = np.zeros(n - 1)

for i in range(n - 1):
    xi = x[i + 1]

    A[i, i] = -2

    if i > 0:
        A[i, i - 1] = 1

    if i < n - 2:
        A[i, i + 1] = 1

    B[i] = -h**2 * np.pi**2 * np.sin(np.pi * xi)

B[0] -= alpha
B[-1] -= beta

y_internal = np.linalg.solve(A, B)

y = np.zeros(n + 1)
y[0] = alpha
y[-1] = beta
y[1:-1] = y_internal

print("x\t\ty")

for i in range(n + 1):
    print(f"{x[i]:.2f}\t\t{y[i]:.6f}")

plt.plot(x, y, 'o-', label="Finite Difference Method")
plt.plot(x, np.sin(np.pi * x), '--', label="Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Finite Difference Method for BVP")
plt.grid()
plt.legend()
plt.show()
