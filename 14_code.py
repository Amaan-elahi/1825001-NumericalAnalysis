import numpy as np

A = np.array([
    [4, 1, 1],
    [1, 5, 2],
    [1, 2, 6]
], dtype=float)

B = np.array([6, 7, 9], dtype=float)

n = len(A)

aug = np.zeros((n, 2 * n))

for i in range(n):
    for j in range(n):
        aug[i, j] = A[i, j]

for i in range(n):
    aug[i, i + n] = 1

for i in range(n):
    aug[i] = aug[i] / aug[i, i]

    for j in range(n):
        if i != j:
            factor = aug[j, i]

            for k in range(2 * n):
                aug[j, k] -= factor * aug[i, k]

inverse = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        inverse[i, j] = aug[i, j + n]

X = np.zeros(n)

for i in range(n):
    for j in range(n):
        X[i] += inverse[i, j] * B[j]

print("Solution:")

for i in range(n):
    print(f"x{i+1} = {X[i]:.6f}")
