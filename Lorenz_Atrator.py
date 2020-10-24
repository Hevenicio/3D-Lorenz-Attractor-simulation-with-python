from matplotlib.animation import PillowWriter
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

plt.style.use(['dark_background'])

# Dados de entrada
t0 = 0.
dt = 0.009
tmax = 100.

x = 1.
y = 1.
z = 20.

rho = 28.0
sigma = 10.0
beta = 8.0/3.0

# Evolução temporal
vec_t = np.arange(t0, tmax, dt)
n = len(vec_t)

# Definição do sistema de EDOs de Lorenz
def F1(t, x, y, z):
    return sigma*(y - x)

def F2(t, x, y, z):
    return rho*x - y - x*z

def F3(t, x, y, z):
    return x*y - beta*z

# Parâmetros do método de RK4
k0 = np.array([0.0, 0.0, 0.0])
k1 = np.array([0.0, 0.0, 0.0])
k2 = np.array([0.0, 0.0, 0.0])
k3 = np.array([0.0, 0.0, 0.0])

# Definiãço do método de Runge-Kutta de 4ª ordem
def RK4(t, x, y, z, f1, f2, f3, dt):
    k0[0] = dt*f1(t, x, y, z)
    k0[1] = dt*f2(t, x, y, z)
    k0[2] = dt*f3(t, x, y, z)

    k1[0] = dt*f1(t + dt/2.0, x + k0[0]/2.0, y + k0[1]/2.0, z + k0[2]/2.0)
    k1[1] = dt*f2(t + dt/2.0, x + k0[0]/2.0, y + k0[1]/2.0, z + k0[2]/2.0)
    k1[2] = dt*f3(t + dt/2.0, x + k0[0]/2.0, y + k0[1]/2.0, z + k0[2]/2.0)

    k2[0] = dt*f1(t + dt/2.0, x + k1[0]/2.0, y + k1[1]/2.0, z + k1[2]/2.0)
    k2[1] = dt*f2(t + dt/2.0, x + k1[0]/2.0, y + k1[1]/2.0, z + k1[2]/2.0)
    k2[2] = dt*f3(t + dt/2.0, x + k1[0]/2.0, y + k1[1]/2.0, z + k1[2]/2.0)

    k3[0] = dt*f1(t + dt, x + k2[0], y + k2[1], z + k2[2])
    k3[1] = dt*f2(t + dt, x + k2[0], y + k2[1], z + k2[2])
    k3[2] = dt*f3(t + dt, x + k2[0], y + k2[1], z + k2[2])

    x = x + (k0[0] + 2.0*k1[0] + 2.0*k2[0] + k3[0])/6.0
    y = y + (k0[1] + 2.0*k1[1] + 2.0*k2[1] + k3[1])/6.0
    z = z + (k0[2] + 2.0*k1[2] + 2.0*k2[2] + k3[2])/6.0

    return np.array([x, y, z])

# Evolução das EDOs
evol = np.zeros((n, 3))
evol[0,0] = x
evol[0,1] = y
evol[0,2] = z

# Saída dos resultados
for i in range(n-1):
    evol[i+1,:] = RK4(vec_t[i], evol[i,0], evol[i,1], evol[i,2], F1, F2, F3, dt)

fig = plt.figure(figsize = (12, 6), dpi = 100) #(12, 6); (12, 7); (14, 9)
ax = fig.gca(projection = '3d')
fig.canvas.set_window_title('Atrator de Lorenz')

fig.set_facecolor('k')

# Planos não transparentes
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False

# Planos transparentes ((0.0, 0.0, 0.0, 0.0))
ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
#plt.close(fig)

def update(i):
    ax.view_init(25, -15 + i/2)
    ax.clear()

    #ax.autoscale_view()
    fig.tight_layout()
    ax.plot(evol[:i,0], evol[:i,1], evol[:i,2], color = plt.cm.prism(i), lw = 0.7, label = 'Atrator de Lorenz: t = ' + str(i))
    ax.legend(fontsize = 12)

    # Removendo grid lines
    ax.grid(False)

    # Retirando os ticks
    ax.w_xaxis.line.set_lw(0.)
    ax.set_xticks([])
    ax.w_yaxis.line.set_lw(0.)
    ax.set_yticks([])
    ax.w_zaxis.line.set_lw(0.)
    ax.set_zticks([])

    # Removendo os tick labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

ani = animation.FuncAnimation(fig, update, np.arange(10000), interval = 5, repeat = False)
#ani.save('Lorenz1.gif', writer = PillowWriter(fps = 160))

plt.show()