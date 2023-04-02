import matplotlib.pyplot as plt
from vpython import *

g1 = graph(title="linear drag", xtitle="t [s]", ytitle="Position [m]", width=500, height=250)
f1 = gcurve(color=color.blue)
f2 = gcurve(color=color.red)

# create empty lists to store time, x, and y values
t_list = []
x_list = []
y_list = []

g = vector(0, -9.8, 0)
R = 0.1
M = 0.01
rho = 1.2
A = pi * R ** 2
C = 0.47
v0 = 5
theta = 360 * pi / 180
ground = box(pos=vector(0, 0, 0), size=vector(10, 0.5, 2), color=color.green)
ball = sphere(pos=vector(-4.5, 5, 0), radius=2 * R, make_trail=True)
ball.m = M
ball.p = ball.m * v0 * vector(cos(theta), sin(theta), 0)
t = 0
dt = 0.01

while ball.pos.y > .25:
    rate(100)
    ball.v = ball.p / ball.m
    F = ball.m * g - .5 * rho * A * C * mag(ball.v) ** 2 * norm(ball.v)
    ball.p = ball.p + F * dt
    ball.pos = ball.pos + ball.p * dt / ball.m

    # append time, x, and y values to the respective lists
    t_list.append(t)
    x_list.append(ball.pos.x)
    y_list.append(ball.pos.y)

    #Graph plots
    f1.plot(t, ball.pos.x)
    f2.plot(t, ball.pos.y)
    t = t + dt

print("final position = ", ball.pos, "m")
print("Time = ", t, " s")

# plot graph using matplotlib (saves to local)
plt.plot(t_list, y_list, color='red', label='y')
plt.xlabel('t [s]')
plt.ylabel('y [m]')

plt.plot(t_list, x_list, color='blue', label='x')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.legend()
plt.show()

