import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

pos = {
  "T01": (1, 2),
  "T02": (5, 2),
  "C01": (2, 3),
  "C02": (4, 3),
  "C03": (2, 1),
  "C04": (4, 1),
  "M01": (0, 4),
  "M02": (1, 4),
  "M03": (2, 4),
  "M04": (3, 4),
  "M05": (4, 4),
  "M06": (5, 4),
  "M07": (0, 0),
  "M08": (1, 0),
  "M09": (2, 0),
  "M10": (3, 0),
  "M11": (4, 0),
  "M12": (5, 0),
  "M13": (6, 0),
  "M14": (7, 0),
}

graph = [
  (  0,  0, 25, 20, 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0, 10, 15, 30,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0, 15, 10, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0, 15, 10, 25,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 15, 10,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 10, 15,  5, 10),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
]

G = nx.DiGraph()

for i in range(len(graph)):
  for j in range(len(graph[i])):
    if graph[i][j] != 0:
      G.add_edge(list(pos.keys())[i], list(pos.keys())[j], weight=graph[i][j])

# Функція для пошуку збільшуючого шляху (BFS)
def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in range(len(capacity_matrix)):
            # Перевірка, чи є залишкова пропускна здатність у каналі
            if not visited[neighbor] and capacity_matrix[current_node][neighbor] - flow_matrix[current_node][neighbor] > 0:
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)

    return False

# Основна функція для обчислення максимального потоку
def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]  # Ініціалізуємо матрицю потоку нулем
    parent = [-1] * num_nodes
    max_flow = 0

    # Поки є збільшуючий шлях, додаємо потік
    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        # Знаходимо мінімальну пропускну здатність уздовж знайденого шляху (вузьке місце)
        path_flow = float('Inf')
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(path_flow, capacity_matrix[previous_node][current_node] - flow_matrix[previous_node][current_node])
            current_node = previous_node

        # Оновлюємо потік уздовж шляху, враховуючи зворотний потік
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node

        # Збільшуємо максимальний потік
        max_flow += path_flow

    return max_flow

sources = ['T01', 'T02']
sinks = ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13', 'M14']

if __name__ == '__main__':
  t = "╔══════════╤═════════╤════════════════════╗"
  m = "╠══════════╪═════════╪════════════════════╣"
  s = "╟──────────┼─────────┼────────────────────╢"
  b = "╚══════════╧═════════╧════════════════════╝"
  r = "║{:^10}│{:^9}│{:^20}║"
  print(t)
  print(r.format('Термінал', 'Магазин', 'Максимальний потік'))
  for i in range(len(sources)):
    print(m)
    for j in range(len(sinks)):
      max_flow = edmonds_karp(graph, list(pos.keys()).index(sources[i]), list(pos.keys()).index(sinks[j]))
      if max_flow == 0: max_flow = '-- Немає --'
      print (r.format(sources[i], sinks[j], max_flow))
      if j+1 != len(sinks): print(s)
  print(b)

  plt.figure(figsize=(10, 7))
  nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1300)
  nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
  plt.show()
