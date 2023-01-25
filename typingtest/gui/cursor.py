import pygame

from typingtest.config import TIMER_COLOR


class Cursor:
    def __init__(self, font: pygame.font.Font) -> None:
        self.font = font
        self.x = 0
        self.y = 0

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(
            screen, TIMER_COLOR, (self.x, self.y, 3, self.font.size(" ")[1])
        )

    def update(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
