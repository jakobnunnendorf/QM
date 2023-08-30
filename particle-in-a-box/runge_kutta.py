import matplotlib.pyplot as plt
import numpy as np
import os

def find_energy_level(E=0, show_plot=True):
    
    if show_plot:
        plt.figure()
        plt.xlabel('x')
        plt.ylabel('psi')
        plt.title('Wave Function for Particle in a Box')
    
    L = 1.0  # Length of the box
    hc = 1.0  # m/h-bar^2
    dx = 0.001  # Step size
    dE = 0.02  # Energy step size
    searching = True  # search condition
    
    while searching:
        x = 0.0  # initial Position
        psi = 0.0  # Wave function
        dpsi = 1.0  # Derivative of the wave function
        x_values = []  # temp store x values for plotting
        psi_values = []  # temp store psi values for plotting

        while x <= L:
            k1 = dx * dpsi
            l1 = dx * (-2 * hc * E * psi)
            
            k2 = dx * (dpsi + 0.5 * l1)
            l2 = dx * (-2 * hc * E * (psi + 0.5 * k1))
            
            k3 = dx * (dpsi + 0.5 * l2)
            l3 = dx * (-2 * hc * E * (psi + 0.5 * k2))
            
            k4 = dx * (dpsi + l3)
            l4 = dx * (-2 * hc * E * (psi + k3))
            
            psi += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            dpsi += (l1 + 2 * l2 + 2 * l3 + l4) / 6
            x += dx

            x_values.append(x)
            psi_values.append(psi)

        if show_plot:
            plt.plot(x_values, psi_values, label=f'E = {E:.2f}')
            plt.pause(0.00001)
            plt.clf()

        if abs(psi) < 0.002:
            searching = False
            return E

        E += dE

    if show_plot:
        plt.show()

def find_n_solutions(n, show_plot=True):
    first_energy = round(find_energy_level(0, show_plot), 2)
    solutions = [first_energy]
    while len(solutions) < n:
        index = len(solutions) - 1
        energy_guess = solutions[index] + 2
        new_solution = round(find_energy_level(energy_guess, show_plot), 2)
        solutions.append(new_solution)
        os.system('clear')
        print('solutions: ', solutions)
    return solutions

first_10_energies = find_n_solutions(10, False)
n_values = np.arange(1, 11)
plt.figure()
plt.scatter(n_values**2, first_10_energies)
plt.xlabel('$n^2$')
plt.ylabel('$E_n$')
plt.title('Proportionality of $E_n$ and $n^2$')
plt.show()
