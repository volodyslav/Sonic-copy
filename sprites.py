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


class HeartSprite(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.pos = (SCREEN_WIDTH + 500, SCREEN_HEIGHT - 250)
        self.image = pygame.image.load(join("images", "heart.png")).convert_alpha()
        self.rect = self.image.get_frect(center=self.pos).inflate(-10, 0)
        self.speed = 1
        self.speed_up = 20

    def move(self, dt):
        self.rect.y -= self.speed_up * dt

        self.rect.x += -(self.speed + dt)
        if self.rect.x < -500:
            self.kill()

    def update(self, dt):
        self.move(dt)


class Health:
    def __init__(self, i, screen):
        self.screen = screen
        # Heart
        self.image = pygame.image.load(join("images", "heart.png")).convert_alpha()
        self.rect = self.image.get_frect(center=(100 * i, 50))

    def draw(self):
        self.screen.blit(self.image, self.rect)


class PlayerRun(pygame.sprite.Sprite):
    """Running player"""
    def __init__(self, pos, groups, collision_group):
        super().__init__(groups)

        self.collision_group = collision_group
        self.image = pygame.image.load(join("images", "player", "run", "0.gif")).convert_alpha()
        self.rect = self.image.get_frect(center=pos).inflate(-10, -10)

        self.frames_run = []
        self.frames_run_index = 0

        self.load_images_run()
        self.velocity = 0
        self.gravity = 3000
        self.jump_speed = -1500

        # Sounds
        self.jump_sound = pygame.mixer.Sound(join("sounds", "jump.mp3"))
        self.jump_sound.set_volume(0.04)

    def input(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.y == PLAYER_RUN_POS:
            self.velocity = self.jump_speed
            self.jump_sound.play()

        self.velocity += self.gravity * dt
        self.rect.y += self.velocity * dt

        if self.rect.y >= PLAYER_RUN_POS:
            self.rect.y = PLAYER_RUN_POS
            self.velocity = 0

        if self.rect.y < PLAYER_RUN_POS:
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


class Bird(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "bird.png")).convert_alpha()
        pos_x, pos_y = SCREEN_WIDTH + 500, 200
        self.rect = self.image.get_frect(center=(pos_x, pos_y)).inflate(-10, -10)
        self.speed = 4

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
                                               ])).convert_alpha()

        pos_x, pos_y = SCREEN_WIDTH + 500, SCREEN_HEIGHT - 180
        self.rect = self.image.get_frect(bottomright=(pos_x, pos_y)).inflate(-10, 0)
        self.speed = 2

    def update(self, dt):
        """Moves"""
        self.rect.x += -(self.speed + dt)
        if self.rect.x < -500:
            self.kill()


class Duck(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "duck", "0.png")).convert_alpha()

        pos_x, pos_y = SCREEN_WIDTH + 500, SCREEN_HEIGHT - 180
        self.rect = self.image.get_frect(bottomright=(pos_x, pos_y)).inflate(-10, 0)

        self.speed = 2.2
        self.frames = []
        self.frame_index = 0

        self.load_images()

    def load_images(self):
        """Loads duck images"""
        for image_path, sub_folder, image_name in walk(join("images", "duck")):
            if image_name:
                for image_num in sorted(image_name, key=lambda n: int(n.split(".")[0])):
                    full_path = join(image_path, image_num)
                    surf = pygame.image.load(full_path)
                    self.frames.append(surf)

    def move_run(self, dt):
        self.frame_index = self.frame_index + 5 * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def update(self, dt):
        """Moves"""
        self.move_run(dt)

        self.rect.x += -(self.speed + dt)
        if self.rect.x < -500:
            self.kill()
