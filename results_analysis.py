#Fully fonctionnal V1

import pygame
from files import img_list
from settings import *
from objects import *

f = open("results.txt", "r")
r = f.readlines()

results=[]
for i in range(len(img_list)):
    results.append(0)

for i in range(len(r)):
    results[int(r[i][5:7])-1]=results[int(r[i][5:7])-1]+1
print(results)
f.close()