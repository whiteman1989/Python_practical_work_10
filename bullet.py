from abc import abstractproperty
from typing import Any
import pygame
from colors import Colors

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x: int, y: int, img: pygame.Surface, *groups: abstractproperty) -> None:
        super().__init__(*groups)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
        return super().update(*args, **kwargs)
