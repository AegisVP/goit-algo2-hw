
import os.path as path
import json
import timeit
from HyperLogLog import HyperLogLog


def generate_set(file_path):
  ip_set = set()
  with open(file_path, 'rt') as file:
    for row in file:
      try:
        ip_set.add(json.loads(row)['remote_addr'])
      except Exception as e:
        print(f'Unable to add line {row}')
      # end try
    # end for
  # end with
  return ip_set
# end def


def generate_hll(file_path):
  hll = HyperLogLog()
  with open(file_path, 'rt') as file:
    for row in file:
      try:
        hll.add(json.loads(row)['remote_addr'])
      except Exception as e:
        print(f'Unable to add line {row}')
      # end try
    # end for
  # end with
  return hll
# end def

def count_ips_hll(hll):
  return hll.get_cardinality()
# end def


def to_time(sec):
  return f'{(sec * 1000):.4f}'
# end def


if __name__ == "__main__":
  t = f"╔{'═'*15}╤{'═'*10}╤{'═'*10}╗"
  h = "║{0:^15}│{1:^10}│{2:^10}║"
  m = f"╠{'═'*15}╪{'═'*10}╪{'═'*10}╣"
  s = f"╟{'─'*15}┼{'─'*10}┼{'─'*10}╢"
  r = "║ {0:<13} │ {1:>8} │ {2:>8} ║"
  b = f"╚{'═'*15}╧{'═'*10}╧{'═'*10}╝"
  # load_start = timeit.default_timer()
  file_name = path.dirname(__file__) + '/lms-stage-access.log'
  # file_data = load_data(file_name)
  # load_time = timeit.default_timer() - load_start
  # print(f'File with {len(file_data)} log entries loaded in {to_time(load_time)} ms')

  set_start_populate = timeit.default_timer()
  ip_set = generate_set(file_name)
  ip_set_count = '{0:.4f}'.format(len(ip_set))
  set_duration_populate = timeit.default_timer() - set_start_populate
  set_duration_count = timeit.timeit(lambda: len(ip_set), number=100)
  set_duration_total = (set_duration_populate + set_duration_count)

  hll_start_populate = timeit.default_timer()
  ip_hll = generate_hll(file_name)
  ip_hll_count = '{0:.4f}'.format(count_ips_hll(ip_hll))
  hll_duration_populate = timeit.default_timer() - hll_start_populate
  hll_duration_count = timeit.timeit(lambda: count_ips_hll(ip_hll), number=100)
  hll_duration_total = (hll_duration_populate + hll_duration_count)
  print(t)
  print(h.format('Statistics',' SET',' HLL'))
  print(m)
  print(r.format('Unique IPs', ip_set_count, ip_hll_count))
  print(s)
  print(r.format('Populate (ms)', to_time(set_duration_populate), to_time(hll_duration_populate)))
  print(r.format('Count in (ms)', to_time(set_duration_count), to_time(hll_duration_count)))
  print(s)
  print(r.format('Total (ms)', to_time(set_duration_total), to_time(hll_duration_total)))
  print(b)
# end if
