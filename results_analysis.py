#Fully fonctionnal V1

from files import img_list
from settings import *

import shutil
import pygame

f = open("results.txt", "r")
r = f.readlines()

offset = 0
text_pos = 0

results=[]
for i in range(len(img_list)):
    results.append(0)

for i in range(len(r)):
    results[int(r[i][5:7])-1]=results[int(r[i][5:7])-1]+1
print(results)
f.close()
pollen = []
for i in range(len(results)):
    if results[i]>len(r)/(len(img_list)*2):
        pollen.append(i+1)
print(pollen)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("BeeCaptcha Results")

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y, bold, spacing=0):
    font = pygame.font.Font(font_name, size)
    if bold == True:
        font.set_bold(True)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    text_surface = pygame.transform.scale(text_surface, (text_rect.width+spacing, text_rect.height))
    surf.blit(text_surface, text_rect)

class Image(pygame.sprite.Sprite):
    def __init__(self, stage):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img_list[stage], (WIDTH/3, HEIGHT/3))
        self.rect = self.image.get_rect()
        self.rect.midtop = (stage*WIDTH+WIDTH/2,100)
        self.stage = stage

    def update(self):
        global offset
        keys = pygame.key.get_pressed()
        self.rect.x += offset

def copy_to_new_dir():
    src_dir="./images/img1.jpeg"
    dst_dir="./pollenimages/imgpollen1.jpeg"
    shutil.copy(src_dir,dst_dir)
        
        
all_sprites=pygame.sprite.Group()

for i in range(len(img_list)):
    img = Image(i)
    all_sprites.add(img)

#copy_to_new_dir()
stage=0
running = True
while running:
    events = pygame.event.get()
    offset=0
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                offset=WIDTH
            if event.key == pygame.K_RIGHT:
                offset=-WIDTH
    
    all_sprites.update()
    
    screen.fill(BLUE)
    all_sprites.draw(screen)
    text_pos+=offset
    for i in range(len(img_list)):
        try:
            if i+1 == pollen[stage]:
                draw_text(screen, "pollen", 30,i*WIDTH+WIDTH/2+text_pos, 600, False)
                stage+=1
        except:
            stage=0
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()