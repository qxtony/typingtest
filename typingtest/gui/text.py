from __future__ import annotations
from typing import Union

import pygame

from typingtest.config import INACTIVE_TEXT_COLOR, WIDTH, HEIGHT, ACTIVE_TEXT_COLOR, ERROR_TEXT_COLOR


class Text:
    def __init__(
        self,
        font: pygame.font.Font,
        text: Union[str, list],
        center: bool = False,
        x: int = 0,
        y: int = 0,
    ) -> None:
        self.texts = {}
        self.font = font
        self.center = center

        self.set_coordinates(text, (x, y))

    def draw(self, screen: pygame.Surface) -> None:
        for text, (coordinates, *_) in self.texts.items():
            screen.blit(text, coordinates)

    def set_coordinates(
        self,
        text: Union[str, list],
        coordinates: tuple[int, int]
    ) -> None:
        if isinstance(text, list):
            self.set_coordinates_list(text, *coordinates)

        else:
            render_text = self.font.render(text, True, INACTIVE_TEXT_COLOR)

            if self.center:
                coordinates = (
                    (WIDTH - render_text.get_width()) // 2,
                    (HEIGHT - render_text.get_height()) // 2,
                )

            self.texts[render_text] = (coordinates, text)

    def set_coordinates_list(
        self,
        words: list,
        x: int, y: int,
        indent: int = 15,
    ) -> None:
        x_symbol, y_symbol = x + indent, y

        if self.center:
            all_text_height = len(words) * self.font.get_height()
            y_symbol = (all_text_height // 2 - HEIGHT) // 2

        for word in words:
            x_word, y_word = self.font.size(word)

            if x_symbol + x_word > WIDTH:
                x_symbol = x + indent
                y_symbol += y_word

            for symbol in word:
                text = self.font.render(symbol, True, INACTIVE_TEXT_COLOR)
                self.texts[text] = ((x_symbol, y_symbol), symbol)
                x_symbol += text.get_width()

            x_symbol += indent

    def set_color_symbol(self, pressed_symbol: str, index: int) -> None:
        counter = 0

        for text, (_, symbol) in self.texts.items():
            if counter == index:
                print(symbol)
                if symbol == pressed_symbol:
                    text.fill(ACTIVE_TEXT_COLOR)

                else:
                    text.fill(ERROR_TEXT_COLOR)

                break

            counter += 1
