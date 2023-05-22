#импортируем модули
import pygame as PG
import random as RNG
from time import sleep

#базовые переменные:
WIDTH, HEIGHT = 700, 500 #ширина, высота окна
BASEPOINT = (0, 0) #левый верхний угол
FPS = 60
Background = (86, 55, 255) #задний фон
PadClr1, PadClr2 = (255, 255, 255), (0, 0, 0) #внешний и внутренний цвет пада
BallSize = (50, 50) #размер мяча

#инициация всех функций pygame:
PG.init()
screen = PG.display.set_mode((WIDTH, HEIGHT))
clock = PG.time.Clock()
Ball = PG.transform.scale(
    PG.image.load('ball.jpg'), #обьект: pygame.image из файла ball.jpg
    BallSize
) #создаём обьект мяча

running = True #переменная отвечаюшая за то что окно открыто
while running: #пока окно открыто
    clock.tick(FPS) #работать в 60 кадров в секунду
    screen.fill(Background) #заполнить задний фон цветом из переменной

    for e in PG.event.get(): #для всех ивентов полученных от event.get()
        if e.type == PG.QUIT: #если ивент: выход
            running = False #закрыть окно программы
    
    PG.display.flip() #обновить картинку.