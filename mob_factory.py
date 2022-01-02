from random import choice as randchoice, random
import pygame
from os import path
from mob import Mob
from pygame.sprite import Group

class MobFactory():
    def __init__(self, screen_width: int, screen_height: int, img_dir: path, all_sprites: Group, all_mobs: Group) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.meteor_image = pygame.image.load(path.join(img_dir, 'meteorBrown_med1.png')).convert()
        self.meteor_images = []
        self.all_sprites = all_sprites
        self.all_mobs = all_mobs
        image_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png', 'meteorBrown_tiny1.png']
        for img in image_list:
            self.meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())
            
    def create_mob(self) -> Mob:
        mob = Mob(self.screen_width, self.screen_height, randchoice(self.meteor_images))
        self.all_mobs.add(mob)
        self.all_sprites.add(mob)
        