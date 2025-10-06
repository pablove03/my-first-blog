import sys
import pygame
from pygame.color import THECOLORS

pygame.init()
dis = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snowman")
clock = pygame.time.Clock()

font = pygame.font.SysFont('couriernew', 40)
text_x = 50
text_y = 50
text_direction = 1  # 1 = вправо, -1 = влево

def draw_scene():
    dis.fill(THECOLORS['lightblue'])

    # Текст
    text = font.render("best snowman", True, THECOLORS["red"])
    dis.blit(text, (text_x, text_y))

    # Snowman
    pygame.draw.circle(dis, (255, 255, 255), [600, 630], 160)
    pygame.draw.circle(dis, (255, 255, 255), [600, 400], 120)
    pygame.draw.circle(dis, (255, 255, 255), [600, 220], 80)

    # Руки
    pygame.draw.line(dis, (150, 75, 0), [480, 400], [210, 210], 10)
    pygame.draw.line(dis, (150, 75, 0), [980, 280], [720, 400], 10)

    # Глаза и пуговицы
    pygame.draw.circle(dis, (0, 0, 0), [640, 210], 10)
    pygame.draw.circle(dis, (0, 0, 0), [560, 210], 10)
    pygame.draw.circle(dis, (0, 0, 0), [600, 350], 10)
    pygame.draw.circle(dis, (0, 0, 0), [600, 450], 10)
    pygame.draw.circle(dis, (0, 0, 0), [600, 550], 10)

    # Нос
    pygame.draw.line(dis, (255, 141, 3), [680, 250], [620, 240], 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Изменяем позицию текста
    text_x += 3 * text_direction
    if text_x > 1000 or text_x < 0:
        text_direction *= -1  # меняем направление

    draw_scene()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
