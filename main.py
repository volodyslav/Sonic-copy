from settings import *


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("T-Rex run")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

    def show_screen(self):
        self.screen.fill(SCREEN_COLOR)
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
