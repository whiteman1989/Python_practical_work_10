from abc import abstractproperty
from typing import Any
import pygame
import random
from colors import Colors
from os import path

class Mob(pygame.sprite.Sprite):
    def __init__(self, screen_width: int, screen_height: int, sprite: pygame.Surface, *groups: abstractproperty) -> None:
        super().__init__(*groups)
        self.image_origin = sprite
        self.image_origin.set_colorkey(Colors.BLACK)
        self.image = self.image_origin.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        #pygame.draw.circle(self.image, Colors.GREEN, self.rect.center, self.radius)
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)
        self.speed_x = random.randrange(-3, 3)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rotate()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top > self.screen_height + 10 or self.rect.left < -25 or self.rect.right > self.screen_width + 20:
            self.rect.x = random.randrange(self.screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1,8)
        return super().update(*args, **kwargs)
    
    def rotate(self) -> None:
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            new_image = pygame.transform.rotate(self.image_origin, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center