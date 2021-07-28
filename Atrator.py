import numpy as np, matplotlib.pyplot as plt, matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

x, y, z  = 0, 1, 10 # ... estado inicial

rho, sigma, beta = 28, 10, 8/3 # ... parâmetros

t0 = 0     # ... tempo inicial
tf = 100   # ... tempo final
dt = 0.008 # ... passo
t = np.arange(t0, tf + dt, dt) # ... evolução temporal
n = len(t)

def EDOs(t, r): # ... definição do sistema de EDOs de Lorenz
    x, y, z = r
    return np.array([sigma*(y - x),   # ... dx/dt
                     rho*x - y - x*z, # ... dy/dt
                     x*y - beta*z])   # ... dz/dt

def RK4(t, r, f, dt): # ... definiãço do método de Runge-Kutta de 4ª ordem
    k1 = dt*f(t, r)
    k2 = dt*f(t + dt/2, r + k1/2)
    k3 = dt*f(t + dt/2, r + k2/2)
    k4 = dt*f(t + dt, r + k3)
    return r + (k1 + 2*k2 + 2*k3 + k4)/6

r = [x, y, z] # ... vetor estado inicial

evol = np.zeros((n, 3)) # ... evolução das EDOs
evol[0,0], evol[0,1],  evol[0,2] = r[0], r[1], r[2]

for i in range(n - 1):
    evol[i + 1] = RK4(t[i], [evol[i,0], evol[i,1], evol[i,2]], EDOs, dt)
    
fig = plt.figure('Atrator de Lorenz', facecolor = 'k', figsize = (10, 9))
fig.tight_layout()
ax = fig.gca(projection = '3d')

def update(i): # ... craindo a animação
    ax.view_init(-6, -56 + i/2)
    ax.clear()
    ax.set(facecolor = 'k')
    ax.set_axis_off()
    ax.plot(evol[:i,0], evol[:i,1], evol[:i,2], color= 'lime', lw = 0.9)

ani = animation.FuncAnimation(fig, update, np.arange(15000), interval = 2, repeat = False)
plt.show()