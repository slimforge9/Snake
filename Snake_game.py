import sys

import pygame

from Settings import Settings
from Snake_player import Snake


class SnakeGame:
    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobow."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")

        self.apples_eaten = 3
        self.direction = 'left'
        self.snake = Snake(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.snake.update()
            pygame.display.flip()


game = SnakeGame()
game.run_game()
