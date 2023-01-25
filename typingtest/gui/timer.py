import time

import pygame

from typingtest.config import TIMER_COLOR


class Timer:
    def __init__(
        self,
        font: pygame.font.Font,
        x: int,
        y: int,
        seconds: int,
    ) -> None:
        self.font = font
        self.x = x
        self.y = y

        self.timer = seconds
        self.seconds = seconds
        self.difference = 0

        self.start = time.monotonic()

    def draw(self, screen: pygame.Surface) -> None:
        text = self.font.render(f"{self.timer} сек.", True, TIMER_COLOR)
        screen.blit(text, (self.x, self.y))

        self.update()

    def update(self) -> None:
        self.timer = round(
            self.seconds - round(time.monotonic() - self.start, 1), 1
        )
        self.difference = round(time.monotonic() - self.start, 1)
