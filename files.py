import pygame
from os import path
from settings import *

pygame.init()
pygame.display.init()

i=0
img_list = []
while True:
    i+=1
    try:
        try:
            img = pygame.image.load(path.join(IMG_DIR, f"img{i}.jpeg"))
            img_list.append(img)
        except:
            try:
                img = pygame.image.load(path.join(IMG_DIR, f"img{i}.png"))
                img_list.append(img)
            except:
                img = pygame.image.load(path.join(IMG_DIR, f"img{i}.jpg"))
                img_list.append(img)
    except:
        break

print(img_list)