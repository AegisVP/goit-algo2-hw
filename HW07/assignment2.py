from functools import lru_cache
from SplayTree import SplayTree
import timeit
import matplotlib.pyplot as plt


@lru_cache(maxsize=1000)
def fibonacci_lru(n):
  if n <= 1:
    return n
  return fibonacci_lru(n-1) + fibonacci_lru(n-2)


def fibonacci_splay(n, tree):
  res = tree.find(n)
  if res is not None:
    return res
  if n <= 1:
    tree.insert(n, n)
    return n
  fib = fibonacci_splay(n-1, tree) + fibonacci_splay(n-2, tree)
  tree.insert(n, fib)
  return fib


if __name__ == '__main__':
  timeit_results = dict()
  splay_tree = SplayTree()
  lru_label = 'LRU Cache'
  splay_label = 'Splay Tree'
  time_label = 'Time(ms)'

  print(f'{"n":<10}{f"{lru_label} {time_label}":<20}{f"{splay_label} {time_label}":<20}')
  for i in range(0, 1000, 50):
    timeit_results[i] = {
      'LRU': timeit.timeit(lambda: fibonacci_lru(i), number=1000)*1000,
      'Splay': timeit.timeit(lambda: fibonacci_splay(i, splay_tree), number=1000)*1000
    }
    print(f'{i:<10}{timeit_results[i]["LRU"]:<20.6f}{timeit_results[i]["Splay"]:<20.6f}')
  
  keys = list(timeit_results.keys())
  lru_values = list(map(lambda x: x['LRU'], timeit_results.values()))
  splay_values = list(map(lambda x: x['Splay'], timeit_results.values()))
  plt.plot(timeit_results.keys(), lru_values, label=lru_label)
  plt.plot(timeit_results.keys(), splay_values, label=splay_label)

  plt.xlabel('Fibonacci number')
  plt.ylabel(time_label)
  plt.legend()
  plt.show()
