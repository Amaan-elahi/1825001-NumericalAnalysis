import numpy as np

A = np.array([
    [4, 1, 1],
    [1, 5, 2],
    [1, 2, 6]
], dtype=float)

x = np.ones(len(A))
tol = 1e-6
max_iter = 100

for i in range(max_iter):
    y = np.linalg.solve(A, x)
    eigenvalue = np.max(np.abs(y))
    x_new = y / eigenvalue

    if np.linalg.norm(x_new - x, np.inf) < tol:
        break

    x = x_new

smallest_eigenvalue = 1 / eigenvalue

print("Smallest Eigenvalue =", smallest_eigenvalue)
print("Eigenvector =", x_new)
print("Iterations =", i + 1)
