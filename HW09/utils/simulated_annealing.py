import random
import math
import numpy as np

# Simulated Annealing
# def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
def simulated_annealing(sphere_function, bounds, temperature=1000, cooling_rate=0.95):

    def generate_neighbor(solution):
        x_min, x_max = bounds[0]
        y_min, y_max = bounds[1]
        x, y = solution
        new_x = np.inf
        new_y = np.inf
        while x_min > new_x or x_max < new_x:
            new_x = x + random.uniform(-1, 1)
        while y_min > new_y or y_max < new_y:
            new_y = y + random.uniform(-1, 1)
        return (new_x, new_y)

    current_solution = tuple(np.random.uniform(low, high) for low, high in bounds)
    current_energy = sphere_function(current_solution)

    while temperature > 0.001:
        new_solution = generate_neighbor(current_solution)
        new_energy = sphere_function(new_solution)
        delta_energy = new_energy - current_energy

        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temperature):
            current_solution = new_solution
            current_energy = new_energy

        temperature *= cooling_rate

    return current_solution, current_energy


