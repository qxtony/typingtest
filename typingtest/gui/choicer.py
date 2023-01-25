from typing import List, Optional

import pygame

from typingtest.config import (
    ACTIVE_TEXT_COLOR,
    ERROR_TEXT_COLOR,
    HEIGHT,
    INACTIVE_TEXT_COLOR,
    WIDTH,
)


class Choicer:
    def __init__(
        self,
        font: pygame.font.Font,
        texts: List[str],
        x: int = 0,
        y: int = 0,
        indent_x: int = 0,
        indent_y: int = 0,
        center: bool = False,
    ):
        self.font = font
        self.texts = texts
        self.x, self.y = x, y
        self.indent_x, self.indent_y = indent_x, indent_y

        self.center = center
        self.selected = 0

        self.x += self.indent_x
        self.y += self.indent_y

    def draw(self, screen: pygame.Surface) -> None:
        for index, text in enumerate(self.texts):
            if index == self.selected:
                color = ACTIVE_TEXT_COLOR
            else:
                color = INACTIVE_TEXT_COLOR

            x, y = self.x, self.y
            render_text = self.font.render(text, True, color)

            if self.center:
                x = (WIDTH - render_text.get_width()) // 2 + self.indent_x
                y = (HEIGHT - render_text.get_height()) // 2 + self.indent_y

            coordinates = (x, y + index * render_text.get_height())
            screen.blit(render_text, coordinates)

    def on_key_press(self, key: int) -> Optional[int]:
        if key == pygame.K_UP:
            self.selected -= 1

        elif key == pygame.K_DOWN:
            self.selected += 1

        elif key == pygame.K_RETURN:
            return self.selected

        if self.selected < 0:
            self.selected = len(self.texts) - 1

        elif self.selected >= len(self.texts):
            self.selected = 0
