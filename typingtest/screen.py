import pygame

from typingtest.config import WIDTH, HEIGHT, TITLE, FPS
from typingtest.scenes import scenes, switch_scenes


class TypingTest:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)

        self.current_scene = scenes[0]
        self.start_game()

    def start_game(self) -> None:
        run: bool = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == pygame.KEYDOWN:
                    switch = self.current_scene.on_key_press(event.key)

                    if switch:
                        self.current_scene = switch_scenes(self.current_scene)

            self.display_update()
            self.clock.tick(FPS)

    def display_update(self) -> None:
        self.current_scene.draw(self.screen)
        pygame.display.update()
