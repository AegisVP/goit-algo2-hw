from trie import Trie


class Homework(Trie):
  def count_words_with_suffix(self, suffix) -> int:
    if not suffix or not isinstance(suffix, str):
      raise TypeError(f"Illegal argument for countWordsWithSuffix: 'suffix' must be a non-empty string")
    # end if

    count = 0

    for word in self:
      if word.endswith(suffix): count += 1
    # end for

    return count
  # end def


  def has_prefix(self, prefix) -> bool:
    if not prefix or not isinstance(prefix, str):
      raise TypeError(f"Illegal argument for hasPrefix: 'prefix' must be a non-empty string")
    # end if

    node = self.root
    for char in prefix:
      if char not in node.children:
        return False
      # end if

      node = node.children[char]
      # end if
    # end for

    return True
  # end def
# end class


if __name__ == "__main__":
  trie = Homework()
  words = ["apple", "application", "banana", "cat"]
  for i, word in enumerate(words):
      trie.put(word)

  # Перевірка кількості слів, що закінчуються на заданий суфікс
  print(f'Asserting count_words_with_suffix("e") == 1   # apple')
  assert trie.count_words_with_suffix("e") == 1  # apple
  print('   - Pass\n')

  print(f'Asserting count_words_with_suffix("ion") == 1   # application')
  assert trie.count_words_with_suffix("ion") == 1  # application
  print('   - Pass\n')

  print(f'Asserting count_words_with_suffix("a") == 1   # banana')
  assert trie.count_words_with_suffix("a") == 1  # banana
  print('   - Pass\n')

  print(f'Asserting count_words_with_suffix("at") == 1   # cat')
  assert trie.count_words_with_suffix("at") == 1  # cat
  print('   - Pass\n')

  # Перевірка наявності префікса
  print('Asserting has_prefix("app") == True  # apple, application ')
  assert trie.has_prefix("app") == True  # apple, application
  print('    - Pass\n')

  print('Asserting has_prefix("bat") == False')
  assert trie.has_prefix("bat") == False
  print('    - Pass\n')

  print('Asserting has_prefix("ban") == True  # banana ')
  assert trie.has_prefix("ban") == True  # banana
  print('    - Pass\n')

  print('Asserting has_prefix("ca") == True  # cat ')
  assert trie.has_prefix("ca") == True  # cat
  print('    - Pass\n')
# end if
