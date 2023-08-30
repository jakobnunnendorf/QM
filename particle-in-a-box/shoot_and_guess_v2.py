import matplotlib.pyplot as plt
import numpy as np
import time
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
    dE = 0.02  # Initial energy step size
    searching = True  # search condition
    
    # Set tolerance and range for the energy steps
    min_dE=0.001
    max_dE=0.1
    tolerance=0.002
    
    while searching:
        x = 0.0  # initial Position
        psi = 0.0  # Wave function
        dpsi = 1.0  # Derivative of the wave function

        while x <= L:
            ddpsi = -2 * hc * E * psi  # Second derivative of psi
            dpsi += ddpsi * dx  # Update dpsi
            psi += dpsi * dx  # Update psi
            x += dx  # Update position

        # Adaptive energy step
        if abs(psi) > tolerance:
            dE = min(max_dE, abs(psi) * 0.01)  # Larger step if far from zero
        else:
            dE = max(min_dE, abs(psi) * 0.1)  # Smaller step if close to zero

        # Plotting
        if show_plot:
            plt.plot([x for x in range(int(L/dx) + 1)], [psi for _ in range(int(L/dx) + 1)], label=f'E = {E:.2f}')
            plt.pause(0.00001)
            plt.clf()

        # Check boundary condition
        if abs(psi) < tolerance:
            searching = False
            return E

        E += dE  # Update energy for the next iteration


def find_n_solutions(n, show_plot = True):
    start_time = time.time()
    first_energy = round(find_energy_level(0, show_plot),2)
    solutions = [first_energy]
    while(len(solutions) < n):
        index = len(solutions)-1
        energy_guess = solutions[index]+2
        new_solution = round(find_energy_level(energy_guess, show_plot), 2)
        solutions.append(new_solution)
        
        os.system('clear')
        print('solutions: ',solutions)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Time taken: {elapsed_time:.2f} seconds")

    return solutions

# Show that E_n is proportional to n^2
first_10_energies = find_n_solutions(10, False)
n_values = np.arange(1, 11)
plt.figure()
plt.scatter(n_values**2, first_10_energies)
plt.xlabel('$n^2$')
plt.ylabel('$E_n$')
plt.title('Proportionality of $E_n$ and $n^2$')
plt.show()