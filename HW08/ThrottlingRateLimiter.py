import time
from typing import Dict

class ThrottlingRateLimiter:
    def __init__(self, min_interval: float = 10.0):
        self.min_interval = min_interval
        self.messages: Dict[str, float] = {}

    def can_send_message(self, user_id: str) -> bool:
        now = time.time()

        if user_id not in self.messages:
            return True
        if now - self.messages[user_id] >= self.min_interval:
            return True
        return False

    def record_message(self, user_id: str) -> bool:
        now = time.time()

        can_send = self.can_send_message(user_id)
        if can_send:
            self.messages[user_id] = now
        return can_send

    def time_until_next_allowed(self, user_id: str) -> float:
        now = time.time()

        if user_id not in self.messages:
            return 0
        return max(0, self.min_interval - (now - self.messages[user_id]))