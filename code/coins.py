import pygame
from settings import *


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        img = pygame.image.load("../img/coin.png")
        self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

coin_group = pygame.sprite.Group()
