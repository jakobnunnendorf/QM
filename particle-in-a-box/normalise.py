import matplotlib.pyplot as plt
from math import sqrt, sin, pi

# Initialize parameters
L = 1.0  # Length of the box
hc = 1.0  # m/h-bar^2
dx = 0.001  # Step size
E = 4.92  # Given energy
U = 0.0  # Potential energy
b = 1.0  # Initial derivative scaling factor

# Initialize plotting
plt.figure()
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Analytical vs Numerical Solution')

# Analytical solution
xt = 0.0
dxt = 0.001
Atemp = 0.0
xt_values = []
psiplot_values = []

while xt <= L:
    psiplot = sqrt(2 / L) * sin(pi * xt / L)
    Atemp += psiplot ** 2 * dxt
    xt += dxt
    xt_values.append(xt)
    psiplot_values.append(psiplot ** 2)

plt.plot(xt_values, psiplot_values, color='red', label='Analytical')
print(f"Analytical Total Probability = {Atemp}")

# Numerical solution
x = 0.0
psi = 0.0
dpsi = 1.0
A = 0.0
x_values = []
psiprime_values = []

while x <= L:
    ddpsi = -2 * hc * (E - U) * psi  # Second derivative of psi
    dpsi += ddpsi * dx  # Update dpsi
    psi += dpsi * dx  # Update psi
    psiprime = b * psi  # Scaled psi
    
    A += psiprime ** 2 * dx  # Update total probability
    x += dx  # Update position

    x_values.append(x)
    psiprime_values.append(psiprime ** 2)

plt.plot(x_values, psiprime_values, color='blue', label='Numerical')
print(f"Numerical Total Probability = {A}")

plt.legend()
plt.show()
