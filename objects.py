#Fully fonctionnal V1

from settings import *
from files import *
import pygame
import random

class Image(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.random_seed = random.randint(0,len(img_list)-1)
        self.image_chosen = img_list[self.random_seed]
        self.image = pygame.transform.scale(self.image_chosen, (WIDTH/3, (HEIGHT-200)/3))
        self.rect = self.image.get_rect()
        self.rect.x = posx*WIDTH/3
        self.rect.y = posy*(HEIGHT-200)/3+200
        self.posx=posx
        self.posy=posy
        self.mouse_pos = (0,0)

    def update(self, event_list):
        self.image = pygame.transform.scale(self.image_chosen, (WIDTH/3, (HEIGHT-200)/3))

        self.mouse_pos = pygame.mouse.get_pos()
        if self.mouse_pos[0]>self.posx*WIDTH/3 and self.mouse_pos[0]<self.posx*WIDTH/3+WIDTH/3:
            if self.mouse_pos[1]>self.posy*(HEIGHT-200)/3+200 and self.mouse_pos[1]<self.posy*(HEIGHT-200)/3+(HEIGHT-200)/3+200:
                self.image.set_alpha(210)
                for event in event_list:
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        f = open("results.txt", "a")
                        f.write(f"image{self.random_seed+1} : Pollen \n")
                        f.close()
                        self.random_seed = random.randint(0,len(img_list)-1)
                        self.image_chosen = img_list[self.random_seed]

                                    
class Clicker(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(clickable, (WIDTH/30, WIDTH/30))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.reset = False
        self.last=0
        self.reset_instance = False

    def update(self, event_list):
        self.image.set_alpha(256)
        self.mouse_pos = pygame.mouse.get_pos()
        if self.reset_instance == False:
            if self.mouse_pos[0]>self.rect.x and self.mouse_pos[0]<self.rect.x+WIDTH/30:
                if self.mouse_pos[1]>self.rect.y and self.mouse_pos[1]<self.rect.y+WIDTH/30:
                    self.image.set_alpha(230)
                    for event in event_list:
                        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                            self.image = pygame.transform.scale(clicked, (WIDTH/30, WIDTH/30))
                            self.reset=True
                            self.reset_instance = True
                            self.last = pygame.time.get_ticks()
                            
        if self.reset_instance == True:
            now = pygame.time.get_ticks()
            if now - self.last>1000:
                self.reset_instance = False
                self.last=now
                self.image = pygame.transform.scale(clickable, (WIDTH/30, WIDTH/30))

        
