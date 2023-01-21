import pygame

from typingtest.config import *


class TypingTest:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.start_game()

    def start_game(self) -> None:
        run: bool = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

                elif event.type == pygame.KEYDOWN:
                    self.on_key_press(event.key)

            self.display_update()
            self.clock.tick(60)

    def display_update(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        pygame.display.update()

    def on_key_press(self, pressed_key: int) -> None:
        pass
