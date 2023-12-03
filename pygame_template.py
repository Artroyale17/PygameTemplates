import pygame

#Задаем основыне константы
WIDTH = 577
HEIGHT = 765
FPS = 30

#Задаем цвета
BLACK = (0, 0, 0)

#Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test")
clock = pygame.time.Clock()

isOpen = True

#Основной игровой цикл
while isOpen:

    #Проверка действий окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isOpen = False

    #Заливка экрана
    screen.fill(BLACK)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()