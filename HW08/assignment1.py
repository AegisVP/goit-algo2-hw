from SlidingWindowRateLimiter import SlidingWindowRateLimiter
import time
import random

def generate_message(limiter: SlidingWindowRateLimiter, message_id: int) -> str:
    user_id = message_id % 5 + 1

    result = limiter.record_message(str(user_id))

    return (f"Повідомлення {message_id:2d} | Користувач {user_id} | "
        f"{'✓' if result else f'× (очікування {limiter.time_until_next_allowed(str(user_id)):.1f}с)'}")


def test_rate_limiter():
    # Створюємо rate limiter: вікно 10 секунд, 1 повідомлення
    limiter = SlidingWindowRateLimiter(window_size=10, max_messages_per_window=1)

    # Симулюємо потік повідомлень від користувачів (послідовні ID від 1 до 20)
    print("\n=== Симуляція потоку повідомлень ===")
    for message_id in range(1, 11):
        print(generate_message(limiter, message_id))

        # Випадкова затримка від 0.1 до 1 секунди
        time.sleep(random.uniform(0.1, 1.0))

    # Чекаємо, поки вікно очиститься
    print("\nОчікуємо 4 секунди...")
    time.sleep(4)

    print("\n=== Нова серія повідомлень після очікування ===")
    for message_id in range(11, 21):
        print(generate_message(limiter, message_id))

        # Випадкова затримка від 0.1 до 1 секунди
        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    test_rate_limiter()