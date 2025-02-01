import random
import timeit
import matplotlib.pyplot as plt
from utils.quick_sort import quick_sort



def create_random_array(n):
  return list(random.randint(0, n) for _ in range(n))


def test_sort_times(length):
  arr = create_random_array(length)
  num_tests = 5
  print_width = 50

  print('\n' + f' Starting tests for length: {length/1000:.0f}k '.center(print_width, '-'))

  time_sort_random = timeit.timeit(lambda: quick_sort(arr, 'random'), number=num_tests)
  print(f'{"Time of quick sort (pivot = random):":<37} {(time_sort_random / num_tests):.4f}s'.center(print_width))

  time_sort_start = timeit.timeit(lambda: quick_sort(arr, 'start'), number=num_tests)
  print(f'{"Time of quick sort (pivot = start):":<37} {(time_sort_start / num_tests):.4f}s'.center(print_width))

  time_sort_end = timeit.timeit(lambda: quick_sort(arr, 'end'), number=num_tests)
  print(f'{"Time of quick sort (pivot = end):":<37} {(time_sort_end / num_tests):.4f}s'.center(print_width))

  time_sort_center = timeit.timeit(lambda: quick_sort(arr, 'center'), number=num_tests)
  print(f'{"Time of quick sort (pivot = center):":<37} {(time_sort_center / num_tests):.4f}s'.center(print_width))

  print(f' Finished {num_tests} tests each '.center(print_width, '-'))
  return {
    'time_sort_random': time_sort_random,
    'time_sort_start': time_sort_start,
    'time_sort_end': time_sort_end,
    'time_sort_center': time_sort_center
  }


if __name__ == '__main__':
  time_start = timeit.default_timer()
  times_10k = test_sort_times(10_000)
  times_50k = test_sort_times(50_000)
  times_100k = test_sort_times(100_000)
  times_500k = test_sort_times(500_000)

  times_rand = [times_10k['time_sort_random'], times_50k['time_sort_random'], times_100k['time_sort_random'], times_500k['time_sort_random']]
  times_start = [times_10k['time_sort_start'], times_50k['time_sort_start'], times_100k['time_sort_start'], times_500k['time_sort_start']]
  times_end = [times_10k['time_sort_end'], times_50k['time_sort_end'], times_100k['time_sort_end'], times_500k['time_sort_end']]
  times_center = [times_10k['time_sort_center'], times_50k['time_sort_center'], times_100k['time_sort_center'], times_500k['time_sort_center']]

  total_time = timeit.default_timer() - time_start
  print(f'\nTotal time taken: {total_time:.4f}s\n')

  labels = ['10_000', '50_000', '100_000', '500_000']
  plt.plot(labels, times_rand, label='random')
  plt.plot(labels, times_start, label='start')
  plt.plot(labels, times_end, label='end')
  plt.plot(labels, times_center, label='center')
  plt.legend(title='Pivot location', title_fontproperties={'weight': 'bold'})
  plt.xlabel('Array length')
  plt.ylabel('Time (s)')
  plt.title('Sorting times')
  plt.show()
