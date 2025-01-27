from time import time_ns

def merge(left,right):
  res = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      res.append(left[i])
      i += 1
    else:
      res.append(right[j])
      j += 1
  while i < len(left):
    res.append(left[i])
    i += 1
  while j < len(right):
    res.append(right[j])
    j += 1
  return res

def merge_sort(in_arr):
  if len(in_arr) == 1:
    return in_arr

  mid = len(in_arr) // 2

  left = merge_sort(in_arr[:mid])
  right = merge_sort(in_arr[mid:])

  return merge(left, right)

def min_k(arr, k=1):
  if k < 1:
    print("K must be greater than 0")
    return
  sorted_arr = merge_sort(arr)
  print(f"K-th: {k}, Min: {sorted_arr[k-1]}")

if __name__ == "__main__":
  start = time_ns()
  arr = [38, 27, 43, 3, 9, 82, 10]
  min_k(arr,1)
  print(f"Execution time: {(time_ns() - start) / 1000000} seconds")
