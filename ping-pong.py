#создай игру "Лабиринт"!

from pygame import *

from random import randint

clock = time.Clock()

FPS = 60

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")
background = transform.scale(image.load("nightcity.jpg"), (700, 500))

destroyed = 0 #разбито/уничтожено кораблей
text_destroyed = 0

#персонажи игры

# увеличить счетчик "пропущено"

#создание объектов класса

#настройка окна

#игровая сцена:

#настройка циклов

game = True 

finish = False

while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)

    display.update()