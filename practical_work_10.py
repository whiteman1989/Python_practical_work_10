from random import randrange
from colors import Colors
from mob import Mob
from mob_factory import MobFactory
from player import Player
import pygame
from pygame.constants import K_SPACE
from os import path

from score_menager import ScoreManager

width = 480
height = 600
fps = 60

img_dir = path.join(path.dirname(__file__), 'sprites')
snd_dir = path.join(path.dirname(__file__), 'sounds')

#init pygame and window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Практична робота 9")
clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
mob_factroy = MobFactory(width, height, img_dir, all_sprites, mobs)   
bullets = pygame.sprite.Group()
player = Player(width, height, bullets, all_sprites, img_dir, snd_dir)
all_sprites.add(player)
for i in  range(8):
    m = mob_factroy.create_mob()

score = ScoreManager(width/2, 10, screen)

#game loop
runing = True
while runing:
    #tick rate
    clock.tick(fps)
    #process event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    #updating
    all_sprites.update()
    #on collission
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        m = mob_factroy.create_mob()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score.add_score(50 - hit.radius)
        m = mob_factroy.create_mob()
    #rendering
    screen.fill(Colors.BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    score.draw()
    pygame.display.flip()

pygame.quit()