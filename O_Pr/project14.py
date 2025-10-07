import sys
from itertools import count
import pygame
from pygame.color import THECOLORS
pygame.init()
dis = pygame.display.set_mode((1200, 800))
color=(155,0,0)
dis.fill(THECOLORS['black'])
pygame.display.set_caption("sss")
font = pygame.font.SysFont('couriernew', 20)
counter=1
for x in range(10,1200,50):
    for y in range(1,800,50):
        pygame.draw.rect(dis,color,(x,y,40,40),1)
        for i in range(0,1,1):
            text = font.render(str(counter), True, THECOLORS['green'])
            dis.blit(text, (x, y))
            counter += 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()