import numpy as np

A = np.array([
    [4, 1, 1],
    [1, 5, 2],
    [1, 2, 6]
], dtype=float)

B = np.array([6, 7, 9], dtype=float)

n = len(B)
x = np.zeros(n)

tol = 1e-6
max_iter = 100

for k in range(max_iter):
    x_old = x.copy()

    for i in range(n):
        s = 0

        for j in range(n):
            if j != i:
                s += A[i, j] * x[j]

        x[i] = (B[i] - s) / A[i, i]

    if np.linalg.norm(x - x_old, np.inf) < tol:
        break

print("Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")

print("Iterations =", k + 1)
