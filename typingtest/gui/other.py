from random import sample
from typing import List

from typingtest.config import (
    PATH_TO_EASY_WORDS,
    PATH_TO_HARD_WORDS,
    PATH_TO_NORMAL_WORDS,
)


def get_random_words(path: str, count: int = 50) -> List[str]:
    words = read_file_with_words(path)
    return sample(words, count)


def read_file_with_words(path: str) -> List[str]:
    with open(path) as file:
        data = file.read()

    return [word + " " for word in data.splitlines() if word]


def get_words_per_minute(
    typing_symbols_count: int,
    incorrect_symbols_count: int,
    timer: int,
    second_in_minute: int = 60,
    round_length: int = 5,
) -> int:
    try:
        wpm = round(
            ((typing_symbols_count / round_length) - incorrect_symbols_count)
            / (timer / second_in_minute)
        )
    except ZeroDivisionError:
        wpm = 0

    return wpm if wpm > 0 else 0


def get_random_words_from_complexity(complexity: int) -> List[str]:
    difficulties = {
        0: PATH_TO_EASY_WORDS,
        1: PATH_TO_NORMAL_WORDS,
        2: PATH_TO_HARD_WORDS,
    }
    return get_random_words(difficulties[complexity])
