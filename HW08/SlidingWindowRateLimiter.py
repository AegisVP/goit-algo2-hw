from collections import deque
from datetime import timedelta, datetime


class SlidingWindowRateLimiter:
    def __init__ (self, window_size: int, max_messages_per_window: int):
        self.window_size = window_size
        self.max_messages_per_window = max_messages_per_window
        self.messages = {}
    # end def


    def _verify(self, user: str) -> None:
        if user not in self.messages:
            self.messages[user] = deque()
        # end if
        self._cleanup_window(user)
    # end def


    def _cleanup_window (self, user: str) -> None:
        current_time = datetime.now() - timedelta(seconds=self.window_size)
        while self.messages[user] and self.messages[user][0] < current_time:
            self.messages[user].popleft()
        # end while
    # end def


    def can_send_message (self, user: str) -> bool:
        self._verify(user)
        return len(self.messages.get(user, [])) < self.max_messages_per_window
    # end def


    def record_message (self, user: str) -> bool:
        self._verify(user)
        now = datetime.now()

        if self.can_send_message(user):
            self.messages[user].append(now)
            return True
        # end if
        return False
    # end def


    def time_until_next_allowed(self, user: str) -> float:
        self._verify(user)
        now = datetime.now()

        if len(self.messages[user]) < self.max_messages_per_window:
            return 0
        # end if
        return (self.messages[user][-1] + timedelta(seconds=self.window_size) - now).seconds
    # end def
# end class