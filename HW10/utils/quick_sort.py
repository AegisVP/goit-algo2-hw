import random


def quick_sort(arr, pivot=2):
    # Якщо масив має менше двох елементів, він вже відсортований
    if len(arr) < 2:
        return arr

    # Вибираємо випадковий індекс для опорного елемента
    match pivot:
        case 'start':
            pivot_index = 0
        case 'end':
            pivot_index = len(arr) - 1
        case 'random':
            pivot_index = random.randint(0, len(arr) - 1)
        case _:
            pivot_index = len(arr) // 2

    pivot = arr[pivot_index]

    # Розділяємо масив на частини
    left, middle, right = [], [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return quick_sort(left) + middle + quick_sort(right)
