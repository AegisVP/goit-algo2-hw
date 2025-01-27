import random
from timeit import default_timer as timer
from LRUcache import LRUCache


K = 100
N_len = 100000
Q_len = 5000
cache_ver = 1


def range_sum_no_cache(array, L, R):
  # print(f'Calculating un-cached sum for range {L} - {R}')
  sum = 0
  for i in range(L, R):
    sum += array[i]
  return sum


def update_no_cache(array, index, value):
  # print(f'Updating idx: {index} to value: {value}')
  array[index] = value


def range_sum_with_cache(array, cache, L, R):
  global cache_ver
  if (cache.get((L,R,cache_ver)) == -1):

    print("Because of the manual addition to cache there's no chance this will run, but it's needed for normal operation of the chache")
    cache.put((L,R,cache_ver), range_sum_no_cache(array, L, R))
  # print(f'Retrieving from cache sum for range {L} - {R}, version: {cache_ver}')
  return cache.get((L,R,cache_ver))


def update_with_cache(array, cache, index, value):
  global cache_ver
  update_no_cache(array, index, value)
  print(f'Invalidating cache')
  cache_ver += 1


if __name__ == '__main__':
  cache = LRUCache(K)
  myArr = [i+1 for i in range(N_len)]

  action_update = 'Update'
  action_range = 'Range'
  half_point = N_len // 2
  actions = []

  for i in range(Q_len):
    A1 = A2 = 0
    while A1 == A2:
      A1 = random.randint(0, N_len-1)
      A2 = random.randint(0, N_len-1)

    if (A1 > A2):
      (A1, A2) = (A2, A1)

    action_type = action_update if random.randint(1, 1000) == 1 else action_range # 1/100 chance of getting an Update
    actions.append((action_type, A1, A2))

  update_no_cache_timer = 0
  update_with_cache_timer = 0
  range_no_cache_timer = 0
  range_with_cache_timer = 0
  update_actions = 0
  range_actions = 0

  for action in actions:
    L = action[1]
    R = action[2]
    if (action[0] == action_update):
      update_actions += 1
      new_value = random.randint(1, 100_000)

      start_with_cache = timer()
      update_with_cache(myArr, cache, L, new_value)
      update_with_cache_timer += timer() - start_with_cache

      start_no_cache = timer()
      update_no_cache(myArr, L, new_value)
      update_no_cache_timer += timer() - start_no_cache
    else:
      range_actions += 1

      start_no_cache = timer()
      res = range_sum_no_cache(myArr, L, R)
      range_no_cache_timer += timer() - start_no_cache

      # Because of the large difference in indexes, there's almost no chance for a cache hit.
      # For the next operation to get a cache hit, we add the result into the cache manually.
      if (cache.get((L, R, cache_ver)) == -1):
        cache.put((L, R, cache_ver), res)

      start_with_cache = timer()
      range_sum_with_cache(myArr, cache, L, R)
      range_with_cache_timer += timer() - start_with_cache

  print(f'Update actions: {update_actions}')
  print(f'Range actions: {range_actions}')
  print(f'Cache version: {cache_ver}')
  print(f'Update no cache time: {"{:.4f}".format(update_no_cache_timer * 1000)} ms')
  print(f'Update with cache time: {"{:.4f}".format(update_with_cache_timer * 1000)} ms')
  print(f'Range no cache time: {"{:.4f}".format(range_no_cache_timer * 1000)} ms')
  print(f'Range with cache time: {"{:.4f}".format(range_with_cache_timer * 1000)} ms')
