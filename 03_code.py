import numpy as np
import matplotlib.pyplot as plt

w = 1.0
wc = 0.5

dt = 0.01
t_max = 20

x1 = 1.0
v1 = 0.0
x2 = 0.0
v2 = 0.0

t = np.arange(0, t_max + dt, dt)

x1_values = []
x2_values = []

def f(t, x1, v1, x2, v2):
    dx1 = v1
    dv1 = -w**2 * x1 + wc**2 * (x2 - x1)
    dx2 = v2
    dv2 = -w**2 * x2 + wc**2 * (x1 - x2)
    return dx1, dv1, dx2, dv2

for ti in t:
    x1_values.append(x1)
    x2_values.append(x2)

    k1, l1, m1, n1 = f(ti, x1, v1, x2, v2)

    k2, l2, m2, n2 = f(
        ti + dt/2,
        x1 + dt*k1/2,
        v1 + dt*l1/2,
        x2 + dt*m1/2,
        v2 + dt*n1/2
    )

    k3, l3, m3, n3 = f(
        ti + dt/2,
        x1 + dt*k2/2,
        v1 + dt*l2/2,
        x2 + dt*m2/2,
        v2 + dt*n2/2
    )

    k4, l4, m4, n4 = f(
        ti + dt,
        x1 + dt*k3,
        v1 + dt*l3,
        x2 + dt*m3,
        v2 + dt*n3
    )

    x1 += dt * (k1 + 2*k2 + 2*k3 + k4) / 6
    v1 += dt * (l1 + 2*l2 + 2*l3 + l4) / 6
    x2 += dt * (m1 + 2*m2 + 2*m3 + m4) / 6
    v2 += dt * (n1 + 2*n2 + 2*n3 + n4) / 6

plt.plot(t, x1_values, label="x1")
plt.plot(t, x2_values, label="x2")
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Coupled Oscillations using RK4")
plt.legend()
plt.grid()
plt.show()
