#Fully fonctionnal V1

import pygame
import random
import time
import os

from files import *
from settings import *
from objects import *

pygame.init()
#screen = pygame.display.set_mode((1920,1080))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("BeeCaptcha")

click=False

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
def new_situation():
    image=0
    for i in range(3):
        for j in range(3):
            image = Image(i,j)
            all_sprites.add(image)

all_sprites=pygame.sprite.Group()
new_situation()

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    all_sprites.update(events)

    screen.fill(BLACK)
    all_sprites.draw(screen)
 
    pygame.display.flip()

    clock.tick(60)
 
pygame.quit()