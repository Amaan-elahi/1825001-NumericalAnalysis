import numpy as np
import math

x = np.array([0, 1, 2, 3, 4], dtype=float)
y = np.array([1, 2, 5, 10, 17], dtype=float)

xp = 2.5
h = x[1] - x[0]
n = len(x)

diff = [y.copy()]
for i in range(1, n):
    diff.append(np.diff(diff[-1]))

# Newton Forward Interpolation
u = (xp - x[0]) / h
forward = y[0]

for i in range(1, n):
    term = u
    for j in range(1, i):
        term *= (u - j)
    forward += (term / math.factorial(i)) * diff[i][0]

# Newton Backward Interpolation
u = (xp - x[-1]) / h
backward = y[-1]

for i in range(1, n):
    term = u
    for j in range(1, i):
        term *= (u + j)
    backward += (term / math.factorial(i)) * diff[i][-1]

print("Newton Forward Interpolation =", forward)
print("Newton Backward Interpolation =", backward)
