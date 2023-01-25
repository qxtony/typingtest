from __future__ import annotations

from typing import Union

import pygame

from typingtest.config import (
    ACTIVE_TEXT_COLOR,
    ERROR_TEXT_COLOR,
    HEIGHT,
    INACTIVE_TEXT_COLOR,
    WIDTH,
)


class Text:
    def __init__(
        self,
        font: pygame.font.Font,
        text: Union[str, list],
        center: bool = False,
        indent_x: int = 0,
        indent_y: int = 0,
        x: int = 0,
        y: int = 0,
        color: tuple[int, int, int] = INACTIVE_TEXT_COLOR,
    ) -> None:
        self.data = text
        self.texts = {}
        self.font = font
        self.center = center
        self.indent_x, self.indent_y = indent_x, indent_y

        self.current_coordinates = (x, y)

        self.color = color
        self.wrongly_typed: int = 0
        self.set_coordinates(text, (x, y))

    def draw(self, screen: pygame.Surface) -> None:
        for text, (coordinates, *_) in self.texts.items():
            screen.blit(text, coordinates)

    def set_coordinates(
        self, text: Union[str, list], coordinates: tuple[int, int]
    ) -> None:
        if isinstance(text, list):
            self.set_coordinates_list(text, *coordinates)

        else:
            render_text = self.font.render(text, True, self.color)

            if self.center:
                coordinates = (
                    (WIDTH - render_text.get_width()) // 2 + self.indent_x,
                    (HEIGHT - render_text.get_height()) // 2 + self.indent_y,
                )

            self.texts[render_text] = (coordinates, text)

    def set_coordinates_list(
        self,
        words: list,
        x: int,
        y: int,
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

    def set_color_symbol(
        self,
        pressed_symbol: str,
        index: int,
        default: bool = False,
    ) -> None:
        counter = 0

        for text, (coordinates, symbol) in self.texts.items():
            if counter == index:
                if default:
                    color = INACTIVE_TEXT_COLOR
                    text.fill(color, special_flags=pygame.BLEND_RGBA_MULT)
                    self.wrongly_typed -= 1

                elif symbol == pressed_symbol:
                    color = ACTIVE_TEXT_COLOR

                else:
                    color = ERROR_TEXT_COLOR
                    self.wrongly_typed += 1

                text.fill(color, special_flags=pygame.BLEND_RGB_MAX)
                index = list(self.texts.keys()).index(text) + 1

                if index > len(self.texts) - 1:
                    return

                self.current_coordinates = list(self.texts.values())[index][0]
                break

            counter += 1

    def get_typing_accuracy(self, count_typing_symbols: int) -> float:
        accuracy = round(
            100 - (self.wrongly_typed / (count_typing_symbols + 1)) * 100, 2
        )

        return min(accuracy, 100)

    @property
    def get_current_text_coordinates(self) -> tuple[int, int]:
        return self.current_coordinates
