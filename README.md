# 3D-Lorenz-Attractor-simulation-with-python

3D animation of the Lorenz Attractor trajectory, implemented in Python using the 4th order Runge-Kutta method.

<!--![Lorenz](https://user-images.githubusercontent.com/65929471/97719774-3f127680-1aa6-11eb-9b83-0535a56469f5.gif)-->

<div align="center"> 
    <img width=80% height=50% src="https://github.com/Hevenicio/3D-Lorenz-Attractor-simulation-with-python/assets/65929471/22a68478-b00f-4672-9371-ed1d8d91d612"/>
</div>

## Theory
The Lorenz attractor is a set of chaotic solutions to a system of ordinary differential equations called the Lorenz system. First studied by Edward Lorenz with the help of Ellen Fetter, who developed a simplified mathematical model for atmospheric convection. The model is a system of three ODEs:

$$
\frac{dx}{dt} = \sigma (y - x)
$$

$$
\frac{dy}{dt} = x(\rho - z) - y
$$


$$
\frac{dz}{dt} = xy - \beta z
$$

The state variables are x, y and z. The rate at which states are changing is denoted by dx/dt, dy/dt and dz/dt respectively. The constants σ, ρ and β are the physical parameters.

## A snippet of the code:

```python
def EDOs(t, r):
    """Definition of the Lorenz ODE system"""
    x, y, z = r
    return np.array([sigma*(y - x),   # dx/dt
                     x*(rho - z) - y, # dy/dt
                     x*y - beta*z])   # dz/dt

def RK4(t, r, f, dt):
    """Definition of the 4th order Runge-Kutta method"""
    k1 = dt*f(t, r)
    k2 = dt*f(t + dt/2, r + k1/2)
    k3 = dt*f(t + dt/2, r + k2/2)
    k4 = dt*f(t + dt, r + k3)
    return r + (k1 + 2*k2 + 2*k3 + k4)/6
```


