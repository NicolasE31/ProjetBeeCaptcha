#Fully fonctionnal V1
# -*- coding: utf-8 -*-

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

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y, bold, spacing=0):
    font = pygame.font.Font(font_name, size)
    if bold == True:
        font.set_bold(True)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    text_surface = pygame.transform.scale(text_surface, (text_rect.width+spacing, text_rect.height))
    surf.blit(text_surface, text_rect)

def draw_grid():
    for i in range(5):
        if i>2:
            pygame.draw.rect(screen, WHITE, (i*WIDTH/3-45,200,5,HEIGHT))
        else:
            pygame.draw.rect(screen, WHITE, (i*WIDTH/3,200,5,HEIGHT))
    for j in range(5):
        if j>2:
            pygame.draw.rect(screen, WHITE, (0,(j*(HEIGHT-200)/3)+200-35,WIDTH,5))
        else:
            pygame.draw.rect(screen, WHITE, (0,(j*(HEIGHT-200)/3)+200,WIDTH,5))
def draw_ui():
    pygame.draw.rect(screen, BLUE, (0,0,WIDTH,200))
    draw_text(screen, "Select all squares with", 30, 50,40, False,)
    draw_text(screen, "Bees holding pollen", 45, 45, 75, True, 50)
    draw_text(screen, "Then click on done to get new images", 30, 50, 135, False)

def new_situation():
    global all_sprites
    all_sprites=pygame.sprite.Group()
    image=0
    for i in range(3):
        for j in range(3):
            image = Image(i,j)
            all_sprites.add(image)
        
all_sprites=pygame.sprite.Group()
front_sprites=pygame.sprite.Group()
new_situation()

c = Clicker(1120,75)
front_sprites.add(c)

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
    front_sprites.update(events)
    if c.reset == True:
        new_situation()
        c.reset=False

    screen.fill(WHITE)
    all_sprites.draw(screen)
    draw_grid()
    draw_ui()
    screen.blit(captcha, (1080,10))
    pygame.draw.rect(screen, BLACK, (1120,75,WIDTH/30,WIDTH/30), border_radius=6)
    front_sprites.draw(screen)
 
    pygame.display.flip()

    clock.tick(60)
 
pygame.quit()