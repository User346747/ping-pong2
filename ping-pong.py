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

#создание спрайтов
class Sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#персонажи игры
class PlatformPlayer():
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = platform.scale(image.load(), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#создание спрайт-мяча
class Ball():
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = ball.scale(image.load(), (65, 65))
        self.speed = ball_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#отображение провала(пропуска мяча) 
def fail():
    pass

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