import random
import numpy as np


# Реалізація алгоритму «Випадковий локальний пошук»
def random_local_search(sphere_function, bounds, max_iterations=100, step_size=0.5, probability=0.2):
    current_point = tuple(np.random.uniform(low, high) for low, high in bounds)
    current_value = sphere_function(current_point)

    def get_random_neighbor(current, bounds, step_size=0.5):
        x_min, x_max = bounds[0]
        y_min, y_max = bounds[1]
        x, y = current
        new_x = np.inf
        new_y = np.inf
        while x_min > new_x or x_max < new_x:
            new_x = x + random.uniform(-step_size, step_size)
        while y_min > new_y or y_max < new_y:
            new_y = y + random.uniform(-step_size, step_size)
        return (new_x, new_y)

    for iteration in range(max_iterations):
        # Отримання випадкового сусіда
        new_point = get_random_neighbor(current_point, bounds, step_size)
        new_value = sphere_function(new_point)

        # Перевірка умови переходу
        if new_value < current_value or random.random() < probability:
            current_point, current_value = new_point, new_value

    return current_point, current_value