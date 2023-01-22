from random import sample
from typing import List


def get_random_words(count: int = 50) -> List[str]:
    words = read_file_with_words()
    return sample(words, count)


def read_file_with_words() -> List[str]:
    with open("typingtest/resources/russian.txt") as file:
        data = file.read()

    return data.splitlines()
