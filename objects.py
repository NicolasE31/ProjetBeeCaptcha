from settings import *
from files import *
import pygame
import random

class Image(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.random_seed = random.randint(0,len(img_list)-1)
        self.image_chosen = img_list[self.random_seed]
        self.image = pygame.transform.scale(self.image_chosen, (WIDTH/3, HEIGHT/3))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = posx*WIDTH/3
        self.rect.y = posy*HEIGHT/3
        self.posx=posx
        self.posy=posy
        self.mouse_pos = (0,0)

    def update(self, event_list):
        self.image = pygame.transform.scale(self.image_chosen, (WIDTH/3, HEIGHT/3))

        self.mouse_pos = pygame.mouse.get_pos()
        if self.mouse_pos[0]>self.posx*WIDTH/3 and self.mouse_pos[0]<self.posx*WIDTH/3+WIDTH/3:
            if self.mouse_pos[1]>self.posy*HEIGHT/3 and self.mouse_pos[1]<self.posy*HEIGHT/3+HEIGHT/3:
                self.image.set_alpha(210)
                for event in event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        f = open("results.txt", "a")
                        f.write(f"image{self.random_seed+1} : Pollen \n")
                        f.close()
                        self.random_seed = random.randint(0,len(img_list)-1)
                        self.image_chosen = img_list[self.random_seed]
                        

