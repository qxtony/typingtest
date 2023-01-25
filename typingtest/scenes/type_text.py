from typing import Final
import string

import pygame

from typingtest.config import BACKGROUND_COLOR, TIMER_SECONDS, TITLE
from typingtest.gui import Cursor, Text, Timer, get_words_per_minute
from typingtest.resources import statistic
from typingtest.scenes.base import Scene

RUSSIAN_LETTERS: Final[list] = (
    list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя ")
    + list(string.punctuation)
)


class TypeText(Scene):
    def __init__(self) -> None:
        super().__init__(font_size=30)
        self.start = True

        self.words = statistic.words
        self.current_symbol_index = 0

        timer_y = self.font.size(self.words[0])[1]
        timer_x = timer_y

        self.timer = Timer(self.font, timer_x, timer_y, TIMER_SECONDS)
        self.text = Text(self.font, self.words, center=True)
        self.cursor = Cursor(self.font)

        self.add_element(self.text)
        self.add_element(self.timer)
        self.add_element(self.cursor)

    def on_key_press(self, key: int) -> bool:
        key_name = pygame.key.name(key)

        if (
            self.current_symbol_index == len("".join(self.words))
            or not self.start
        ):
            self.add_statistic()
            return True

        if key_name == "space":
            key_name = " "

        if key_name in RUSSIAN_LETTERS:
            self.text.set_color_symbol(key_name, self.current_symbol_index)
            self.current_symbol_index += 1

        elif key_name == "backspace":
            if self.current_symbol_index > 0:
                self.current_symbol_index -= 1
                self.text.set_color_symbol(
                    key_name, self.current_symbol_index, True
                )

        self.cursor.update(*self.text.get_current_text_coordinates)
        return False

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill(BACKGROUND_COLOR)

        for element in self.elements:
            element.draw(screen)

        wpm = get_words_per_minute(
            self.current_symbol_index,
            self.text.wrongly_typed,
            self.timer.difference,
        )
        accuracy = self.text.get_typing_accuracy(self.current_symbol_index)
        pygame.display.set_caption(
            f"Words per minute: {wpm} | Accuracy: {accuracy}%"
        )

        if self.timer.timer < 0:
            pygame.display.set_caption(TITLE)
            self.start = False

            self.add_statistic()
            self.on_key_press(pygame.K_SPACE)

    def add_statistic(self) -> None:
        wpm = get_words_per_minute(
            self.current_symbol_index,
            self.text.wrongly_typed,
            self.timer.difference,
        )
        accuracy = self.text.get_typing_accuracy(self.current_symbol_index)

        statistic.add_statistic(
            wpm, self.text.wrongly_typed, self.current_symbol_index, accuracy
        )
