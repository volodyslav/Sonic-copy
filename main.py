import pygame

from settings import *
from sprites import *
from random import choice


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sonic")

        ## Ground
        self.ground_image = pygame.image.load(join("images", "grass.png"))
        self.ground_rect = self.ground_image.get_frect(topleft=(0, SCREEN_HEIGHT - 200))

        # Groups
        self.group_sprites = pygame.sprite.Group()
        self.cloud_group = pygame.sprite.Group()
        self.tress_group = pygame.sprite.Group()
        self.collision_group = pygame.sprite.Group()

        # Game settings
        self.start_game = False
        if not self.start_game:
            self.player = PlayerStand((PLAYER_POSITION_X, PLAYER_POSITION_Y), self.group_sprites)


        # Dt
        self.clock = pygame.time.Clock()

        # Custom events
        self.cloud_event = pygame.event.custom_type()
        pygame.time.set_timer(self.cloud_event, choice([200, 500, 900]))

        self.trees_event = pygame.event.custom_type()
        pygame.time.set_timer(self.trees_event, choice([1000, 1400]))

        self.objects_event = pygame.event.custom_type()
        pygame.time.set_timer(self.objects_event, choice([1500, 2000]))

        self.score_event = pygame.event.custom_type()
        pygame.time.set_timer(self.score_event, 1000)

        # Score
        self.score = 0

        # Text nad font
        self.font = pygame.font.Font(None, 100)
        self.score_font = pygame.font.Font(None, 50)
        self.start_text = self.font.render("Press 'S' to start", True, (255, 255, 255))

        # Heart
        self.health = 4

        # Musics
        pygame.mixer.init()
        pygame.mixer.music.load(join("sounds", "mainMusic.wav"))
        pygame.mixer.music.play()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == self.score_event and self.start_game:
                    self.score += 1
                if event.type == self.objects_event and self.start_game:
                    Objects((self.group_sprites, self.collision_group))
                if event.type == self.cloud_event:
                    Clouds(self.cloud_group)
                if event.type == self.trees_event and self.start_game:
                    Trees(self.tress_group)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_s:
                        self.start_game = True
                        # Change from stand to run
                        self.player.kill()
                        self.player = PlayerRun((PLAYER_POSITION_X, PLAYER_RUN_POS), self.group_sprites, self.collision_group)

            self.show_screen()

    def draw_health(self):
        image_health = pygame.image.load(join("images", "heart.png")).convert_alpha()
        for i in range(1, self.health + 1):
            rect_health = image_health.get_frect(center=( 100 * i, 50))
            self.screen.blit(image_health, rect_health)

    def show_screen(self):
        dt = self.clock.tick() / 1000

        # Fill the screen
        self.screen.fill(SCREEN_COLOR)
        # Draw the ground
        self.screen.blit(self.ground_image, self.ground_rect)
        # dRAW CLOUDS
        self.cloud_group.draw(self.screen)
        self.cloud_group.update(dt)

        # Draw trees
        self.tress_group.draw(self.screen)
        self.tress_group.update(dt)

        # Draw the group sprite
        self.group_sprites.draw(self.screen)
        self.group_sprites.update(dt)

        if not self.start_game:
            self.screen.blit(self.start_text, self.start_text.get_frect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)))
        else:
            text_score = self.score_font.render(f"Score: {self.score}", True, (255, 0, 0))
            self.screen.blit(text_score, text_score.get_frect(center=(SCREEN_WIDTH - 100, 50)))

            self.draw_health()

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
