from typing import List


class Statistic:
    def __init__(self) -> None:
        self.words_per_minute = 0
        self.wrongly_typed = 0
        self.all_typed = 0
        self.accuracy = 0
        self.words: List[str] = [""]

    def add_statistic(
        self,
        words_per_minute: int,
        wrongly_typed: int,
        all_typed: int,
        accuracy: float,
    ) -> None:
        self.words_per_minute = words_per_minute
        self.wrongly_typed = wrongly_typed
        self.all_typed = all_typed
        self.accuracy = accuracy


statistic = Statistic()
