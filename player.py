from abc import abstractproperty
from posixpath import join
from typing import Any, Collection, List
import pygame
from pygame.scrap import set_mode
from colors import Colors
from bullet import Bullet
from pygame.sprite import Group
from os import path

class Player(pygame.sprite.Sprite):
    def __init__(self, window_width: int, window_height: int, bullets: Group, all_sprites: Group, img_path: path, *groups: abstractproperty) -> None:
        super().__init__(*groups)
        sprite = pygame.image.load(path.join(img_path, 'player.png')).convert_alpha()
        self.image = pygame.transform.scale(sprite, (50, 50))
        self.image.set_colorkey(Colors.BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        #pygame.draw.circle(self.image, Colors.RED, self.rect.center, self.radius)
        self.rect.centerx = window_width / 2
        self.rect.bottom = window_height - 10
        self.speedx = 0
        self.horizontal_speed = 8
        self.window_width = window_width
        self.window_height = window_height
        self.bullets = bullets
        self.all_sprites = all_sprites
        self.bullet_img = pygame.image.load(path.join(img_path, 'laserRed01.png')).convert()
        self.bullet_img.set_colorkey(Colors.BLACK)

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = self.horizontal_speed * -1
        if keystate[pygame.K_RIGHT]:
            self.speedx = self.horizontal_speed
        self.rect.x += self.speedx
        if self.rect.right > self.window_width:
            self.rect.right = self.window_width
        if self.rect.left < 0:
            self.rect.left = 0
        return super().update(*args, **kwargs)
    
    def shoot(self) -> None:
        bullet = Bullet(self.rect.centerx, self.rect.top, self.bullet_img)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)
