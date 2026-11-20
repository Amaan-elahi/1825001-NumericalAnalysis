import numpy as np

x = np.array([0, 1, 2, 3, 4], dtype=float)
y = np.array([1, 2, 5, 10, 17], dtype=float)

xp = 2.5

h = x[1] - x[0]
n = len(x)

diff = [y.copy()]

for i in range(1, n):
    diff.append(np.diff(diff[-1]))

mid = n // 2
u = (xp - x[mid]) / h

result = y[mid]
term = 1

for i in range(1, n):
    if i % 2 == 1:
        k = (i + 1) // 2
        term *= (u + k - 1) if i == 1 else (u + k - 1)
        term *= (u - k)
        term /= i
        result += term * diff[i][mid - k]
    else:
        k = i // 2
        term *= (u + k - 1)
        term *= (u - k)
        term /= i
        result += term * diff[i][mid - k]

print("Interpolated value =", result)
