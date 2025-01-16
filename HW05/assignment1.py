from BloomFilter import BloomFilter


def check_password_uniqueness(bloom, passwords):
  results = {}
  for password in passwords:
    if password == None or password == "":
      results[password] = "Invalid"
    elif bloom.contains(password):
      results[password] = "Used"
    else:
      results[password] = "Unique"
    # end if
  return results
# end def


if __name__ == "__main__":
  # Ініціалізація фільтра Блума
  bloom = BloomFilter(size=1000, num_hashes=3)

  # Додавання існуючих паролів
  existing_passwords = ["password123", "admin123", "qwerty123"]
  for password in existing_passwords:
    bloom.add(password)
  # end for

  # Перевірка нових паролів
  new_passwords_to_check = ["password123", "newpassword", "admin123", "guest", ""]
  results = check_password_uniqueness(bloom, new_passwords_to_check)

  # Виведення результатів
  for password, status in results.items():
    print(f"Пароль '{password}' - {status}.")
  # end for
# end if
