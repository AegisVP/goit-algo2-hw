from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """

    #### Start of my code
    memo = {}

    def solve(cut_len):
        if cut_len == 0:
            return {"max_profit": 0, "cuts": [], "number_of_cuts": 0}
        # end if

        if cut_len in memo:
            return memo[cut_len]
        # end if

        max_profit = 0
        cuts = []

        for i in range(1, cut_len + 1):
            if i <= len(prices):
                res = solve(cut_len - i)
                profit = res["max_profit"] + prices[i - 1]

                if profit > max_profit:
                    max_profit = profit
                    cuts = res["cuts"] + [i]
        # end for

        number_of_cuts = len(cuts) - 1

        memo[cut_len] = {
            "max_profit": max_profit,
            "cuts": cuts,
            "number_of_cuts": number_of_cuts
        }

        return {
            "max_profit": max_profit,
            "cuts": cuts,
            "number_of_cuts": number_of_cuts
        }

    return solve(length)
    #### End of my code
# end def

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """

    #### Start of my code
    cut_profits = [0] * (length + 1)
    cuts = [0] * (length + 1)

    for cut_length in range(1, length + 1):
        max_profit = 0
        for cut in range(1, cut_length + 1):
            if cut <= len(prices):
                profit = prices[cut - 1] + cut_profits[cut_length - cut]
                if profit > max_profit:
                    max_profit = profit
                    cuts[cut_length] = cut
                # end if
            # end if
        # end for
        cut_profits[cut_length] = max_profit
    # end for

    cut_lengths = []
    while length > 0:
        cut_lengths.append(cuts[length])
        length -= cuts[length]
    # end while

    #### End of my code

    return {
        "max_profit": cut_profits[-1],
        "cuts": cut_lengths,
        "number_of_cuts": len(cut_lengths) - 1
    }
# end def

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!\n")

if __name__ == "__main__":
    run_tests()
