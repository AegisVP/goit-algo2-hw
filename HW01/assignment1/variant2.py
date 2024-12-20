from time import time_ns
import sys

def min_max(in_arr):
  global min_val
  global max_val
  min_val = sys.maxsize
  max_val = -sys.maxsize

  def split(in_val):
    global min_val
    global max_val
    if len(in_val) == 1:
      in_val = in_val[0]
      min_val = in_val if in_val < min_val else min_val
      max_val = in_val if in_val > max_val else max_val
    else:
      mid = len(in_val) // 2
      split(in_val[:mid])
      split(in_val[mid:])

  split(in_arr)
  return (min_val, max_val)

if __name__ == "__main__":
  start = time_ns()
  arr = [38, 27, 43, 3, 9, 82, 10]
  (min_val, max_val) = min_max(arr)
  print(f"Min: {min_val}, Max: {max_val}")
  print(f"Execution time: {((time_ns() - start) / 1000000):.3f} seconds")