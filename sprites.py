from settings import *


class Player(pygame.sprite.Sprite):
    """T-rex sprite"""
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "Player", "stand", "0.gif")).convert_alpha()
        self.rect = self.image.get_frect(center=pos)

        self.frames_stand = []
        self.frames_stand_index = 0
