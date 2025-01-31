import numpy as np

# Hill Climbing
def hill_climbing(sphere_function, bounds, max_iterations=100, step_size=0.1):
    current_point = tuple(np.random.uniform(low, high) for low, high in bounds)
    current_value = -sphere_function(current_point)

    def get_neighbors(current, bounds, step_size=0.1):
      x_min, x_max = bounds[0]
      y_min, y_max = bounds[1]
      x, y = current
      ret_array = []
      if x - step_size >= x_min:
          ret_array.append((x - step_size, y))
      if x + step_size <= x_max:
          ret_array.append((x + step_size, y))
      if y - step_size >= y_min:
          ret_array.append((x, y - step_size))
      if y + step_size <= y_max:
          ret_array.append((x, y + step_size))
      return ret_array

    for iteration in range(max_iterations):
        neighbors = get_neighbors(current_point, bounds, step_size)

        # Пошук найкращого сусіда
        next_point = None
        next_value = -np.inf

        for neighbor in neighbors:
            value = -sphere_function(neighbor)
            if value >= next_value:
                next_point = neighbor
                next_value = value

        # Якщо не вдається знайти кращого сусіда — зупиняємось
        if next_value < current_value:
            break

        # Переходимо до кращого сусіда
        current_point, current_value = next_point, next_value

    return current_point, -current_value
