from typing import Union

import pygame

from typingtest.config import BACKGROUND_COLOR, PATH_TO_FONT
from typingtest.gui import Choicer, Cursor, Text, Timer


class Scene:
    def __init__(self, font_size: int) -> None:
        pygame.font.init()
        self.font = pygame.font.Font(PATH_TO_FONT, font_size)
        self.elements: list = []

    def add_element(
        self, element: Union[Text, Timer, Choicer, Cursor]
    ) -> None:
        self.elements.append(element)

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill(BACKGROUND_COLOR)

        for element in self.elements:
            element.draw(screen)

    def on_key_press(self, key: int) -> bool:
        ...

    def on_event(self, event: pygame.event) -> None:
        ...
