from typing import Final

import pygame

from typingtest.gui import Text, get_random_words
from typingtest.scenes.base import Scene


RUSSIAN_LETTERS: Final[list] = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")


class TypeText(Scene):
    def __init__(self) -> None:
        super().__init__(font_size=30)

        self.words = get_random_words()
        self.current_symbol_index = 0

        self.add_element(Text(self.font, self.words, center=True))

    def on_key_press(self, key: int) -> bool:
        key_name = pygame.key.name(key)

        if key_name in RUSSIAN_LETTERS:
            print(key_name)
            self.elements[0].set_color_symbol(key_name, self.current_symbol_index)
            self.current_symbol_index += 1

        return False
