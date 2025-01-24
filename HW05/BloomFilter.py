import mmh3

class BloomFilter:
  def __init__(self, size, num_hashes):
    self.size = size
    self.num_hashes = num_hashes
    self.bit_array = [0] * size
  # end def

  def add(self, item):
    for i in range(self.num_hashes):
      index = mmh3.hash(item, i) % self.size
      self.bit_array[index] = 1
    # end for
  # end def

  def contains(self, item):
    for i in range(self.num_hashes):
      index = mmh3.hash(item, i) % self.size
      if self.bit_array[index] == 0:
        return False
      # end if
    # end for
    return True
  # end def
# end class
