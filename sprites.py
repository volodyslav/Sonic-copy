import pygame
from random import choice
from settings import *


class PlayerStand(pygame.sprite.Sprite):
    """Standing player"""
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player", "stand", "0.gif")).convert_alpha()
        self.rect = self.image.get_frect(center=pos)

        self.frames_stand = []
        self.frames_stand_index = 0

        self.load_images_stand()


    def load_images_stand(self):
        """Loads standing images"""
        for image_path, sub_folder, image_name in walk(join("images", "player", "stand")):
            if image_name:
                for image_num in sorted(image_name, key=lambda n: int(n.split(".")[0])):
                    full_path = join(image_path, image_num)
                    surf = pygame.image.load(full_path)
                    self.frames_stand.append(surf)

    def move_stand(self, dt):
        self.frames_stand_index = self.frames_stand_index + 5 * dt
        self.image = self.frames_stand[int(self.frames_stand_index) % len(self.frames_stand)]

    def update(self, dt):
        self.move_stand(dt)


class PlayerRun(pygame.sprite.Sprite):
    """Running player"""
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player", "run", "0.gif")).convert_alpha()
        self.rect = self.image.get_frect(center=pos)

        self.frames_run = []
        self.frames_run_index = 0

        self.load_images_run()
        print(self.rect.y)

    def input(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.y -= 2000 * dt

        if self.rect.y < 300 and self.rect.y != 398:

            self.image = pygame.image.load(join("images", "player", "jump.png")).convert_alpha()



    def load_images_run(self):
        """Loads standing images"""
        for image_path, sub_folder, image_name in walk(join("images", "player", "run")):
            if image_name:
                for image_num in sorted(image_name, key=lambda n: int(n.split(".")[0])):
                    full_path = join(image_path, image_num)
                    surf = pygame.image.load(full_path)
                    self.frames_run.append(surf)

    def move_run(self, dt):
        self.frames_run_index = self.frames_run_index + 5 * dt
        self.image = self.frames_run[int(self.frames_run_index) % len(self.frames_run)]

    def update(self, dt):
        self.move_run(dt)
        self.input(dt)


class Clouds(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "cloud.png")).convert_alpha()
        pos_x, pos_y = SCREEN_WIDTH + 100, choice([SCREEN_HEIGHT / 2, 100, 200, 300])
        self.rect = self.image.get_frect(center=(pos_x, pos_y))
        self.speed = 2

    def update(self, dt):
        """Moves"""
        self.rect.x += -(self.speed + dt)
        if self.rect.x < -200:
            self.kill()


class Trees(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(choice([join("images", "palm2-min.png"), join("images", "palm-min.png")])).convert_alpha()
        pos_x, pos_y = SCREEN_WIDTH + 500, SCREEN_HEIGHT - 200
        self.rect = self.image.get_frect(bottomright=(pos_x, pos_y))
        self.speed = 2

    def update(self, dt):
        """Moves"""
        self.rect.x += -(self.speed + dt)
        if self.rect.x < -500:
            self.kill()


class Objects(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(choice([join("images", "rock.png"),
                                               join("images", "spike.png")
                                               ]))

        pos_x, pos_y = SCREEN_WIDTH + 500, SCREEN_HEIGHT - 180
        self.rect = self.image.get_frect(bottomright=(pos_x, pos_y))
        self.speed = 2

    def update(self, dt):
        """Moves"""
        self.rect.x += -(self.speed + dt)
        if self.rect.x < -500:
            self.kill()
