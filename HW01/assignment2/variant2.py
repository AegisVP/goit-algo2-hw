from sys import maxsize
from time import time_ns

def min_k(in_arr, k):
  if k < 1:
    print("K must be greater than 0")
    return
  if k > len(in_arr):
    print("K must not be more than the array's length")
    return

  global min_arr
  min_arr = [maxsize] * k

  def split(in_val):
    if len(in_val) > 1:
      mid = len(in_val) // 2
      split(in_val[:mid])
      split(in_val[mid:])
      return

    global min_arr
    in_val = in_val[0]
    if k == 1:
      if in_val < min_arr[0]:
        min_arr[0] = in_val
        return

    for i in range(k-1, 0, -1):
      if in_val > min_arr[i-1] and in_val < min_arr[i]:
        min_arr[i] = in_val
      if in_val < min_arr[i-1]:
        min_arr[i] = min_arr[i-1]
        min_arr[i-1] = in_val

  split(in_arr)
  print(f"K: {k}, K-th min: {min_arr[k-1]}")

if __name__ == "__main__":
  start = time_ns()
  arr = [2, 38, 27, 43, 3, 9, 82, 10]
  min_k(arr, 3)
  print(f"Execution time: {(time_ns() - start) / 1000000} seconds")