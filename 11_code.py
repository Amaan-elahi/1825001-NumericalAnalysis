import numpy as np

A = np.array([
    [4, 1, 1],
    [1, 5, 2],
    [1, 2, 6]
], dtype=float)

B = np.array([6, 7, 9], dtype=float)

n = len(B)

for i in range(n):
    for j in range(i + 1, n):
        factor = A[j, i] / A[i, i]

        for k in range(i, n):
            A[j, k] -= factor * A[i, k]

        B[j] -= factor * B[i]

x = np.zeros(n)

for i in range(n - 1, -1, -1):
    x[i] = (B[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

print("Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")
