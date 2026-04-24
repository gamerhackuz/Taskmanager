from datetime import datetime, timedelta
import re

class Task:
    def __init__(self, title: str, priority: int, deadline: str):
        self.title = self._validate_title(title)
        self.priority = self._validate_priority(priority)
        self.deadline = self._validate_deadline(deadline)

    @staticmethod
    def _validate_deadline(ds: str) -> datetime:
        fmt = "%Y-%m-%d %H:%M"
        dt = datetime.strptime(ds, fmt)
        if dt < datetime.now():
            raise ValueError("Muddat o'tib ketgan!")
        return dt

    def is_expired(self) -> bool:
        return datetime.now() > self.deadline
