import sys 

import pygame

from settings import Settings


class CosmicCombat:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Cosmic Combat")
        self.clock = pygame.time.Clock()
        self.bg_color = (179, 179, 255)
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def run_game(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    cc = CosmicCombat()
    cc.run_game()