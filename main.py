from settings import *
from sprites import *
from random import choice

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sonic")

        ## Ground
        self.ground_image = pygame.image.load(join("images", "player", "grass.png"))
        self.ground_rect = self.ground_image.get_frect(topleft=(0, SCREEN_HEIGHT - 200))

        # Groups
        self.group_sprites = pygame.sprite.Group()
        self.objects_group = pygame.sprite.Group()

        self.player = Player((PLAYER_POSITION_X, PLAYER_POSITION_Y), self.group_sprites)
        # Dt
        self.clock = pygame.time.Clock()

        # Custom events
        self.cloud_event = pygame.event.custom_type()
        pygame.time.set_timer(self.cloud_event, choice([300, 2000]))

        self.trees_event = pygame.event.custom_type()
        pygame.time.set_timer(self.trees_event, choice([800, 1000, 1500]))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == self.cloud_event:
                    Clouds(self.objects_group)
                if event.type == self.trees_event:
                   Trees(self.objects_group)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.show_screen()

    def show_screen(self):
        dt = self.clock.tick() / 1000

        # Fill the screen
        self.screen.fill(SCREEN_COLOR)
        # Draw the ground
        self.screen.blit(self.ground_image, self.ground_rect)
        # dRAW CLOUDS
        self.objects_group.draw(self.screen)
        self.objects_group.update(dt)

        # Draw the group sprite
        self.group_sprites.draw(self.screen)
        self.group_sprites.update(dt)

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
