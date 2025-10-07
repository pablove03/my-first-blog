# from greeting import hello
# class laptop:
#     def __init__(self,model,GPU,price):
#         self.m=model
#         self.g=GPU
#         self.p=price
# laptop1=laptop("ASUS ROG Strix SCAR 18 G835LX","RTX 5090","2 899 990 T")
# laptop2=laptop("MSI Titan 18 HX AI A2XWJG-649KZ","RTX 5090","3 198 000")
# print(laptop1.m)
# print(laptop2.g)
# if __name__=="__main__":
#     my_laptop=laptop("Lenovo","Intel Iris",700)
#     my_laptop.show_greeting()
#///
import pygame
pygame.init()
dis=pygame.display.set_mode((1200,800))
# квадрат для дома
r = pygame.Rect(400, 300, 400, 400)
pygame.draw.rect(dis, (255, 255, 0), r, 2)

#(треугольник)
roof_points = [(400, 300), (800, 300), (600, 150)]
pygame.draw.polygon(dis, (255, 0, 0), roof_points)

#дверь
door = pygame.Rect(550, 500, 100, 200)
pygame.draw.rect(dis, (139, 69, 19), door)  # Коричневая дверь

#окно
window = pygame.Rect(650, 350, 80, 80)
pygame.draw.rect(dis, (0, 0, 255), window)  # Синее окно

#ручка двери
pygame.draw.circle(dis,(255,255,255),[630,590],10)
dis_over=False
while not dis_over:
    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
pygame.display.update()
quit()
