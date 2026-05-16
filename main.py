from pygame import *
#from time import *

#шрифты и надписи
font.init()
font1 = font.Font(None, 80)
lose_1 = font1.render('Игрок 1 проиграл', True, (255, 255, 255))
lose_2 = font1.render('Игрок 2 проиграл', True, (255, 255, 255))

#нам нужны такие картинки:
img_platform = "platform.png" #платформа
img_ball = "ball.png" #мяч
img_back = "background.png" #фон

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    #метод для управления буквами
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_y, speed_x):
        super().__init__(player_image, player_x, player_y, size_x, size_y, 0)
        self.speed_y = speed_y
        self.speed_x = speed_x

    def update(self): 
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y > win_height - 50 or self.rect.y < 0:
            self.speed_y *= -1



#окно
win_width = 1600
win_height = 900
display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))
#background = transform.scale(image.load(img_back), (win_width, win_height))
background = Surface((win_width, win_height))
background.fill((255, 255, 255))

#объекты
platform_2= Player(img_platform, 150, 300, 30, 300, 10)
platform_1= Player(img_platform, 1450, 300, 30, 300, 10)
ball = Ball(img_ball, 500, 300, 50, 50, 7, 7)

#игровой цикл
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(background, (0, 0))
    
    if not finish:
        platform_2.update_l()
        platform_2.reset()
        
        platform_1.update_r()
        platform_1.reset()
        
        ball.update()
        ball.reset()
        
        if sprite.collide_rect(platform_1, ball) or sprite.collide_rect(platform_2, ball):
            ball.speed_x *= -1
        
        if ball.rect.x < 0:
            window.blit(lose_2, (600, 400))  
            finish = True
        elif ball.rect.x > win_width - 50:
            window.blit(lose_1, (600, 400))  
            finish = True
    
    else:
        if ball.rect.x < 0:
            window.blit(lose_2, (600, 400))
        else:
            window.blit(lose_1, (600, 400))
    
    display.update()
    time.delay(60)