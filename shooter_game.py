#Создай собственный Шутер!

from pygame import *
from random import randint

miss = 0
print('hello')
class GameSprite(sprite.Sprite):
    def __init__(self,player_name,speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(player_name),(50,50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -=self.speed
        elif keys[K_RIGHT] and self.rect.x < 610:
            self.rect.x += self.speed
    def shoot(self):
        bullet = Bullet('bullet.jpg',20,self.rect.centerx,self.rect.centery)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(25,675)
            self.speed = randint(1,2)
            global miss
            miss += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

win = display.set_mode((700,500))
display.set_caption('Арканоид')
fps = 120

clock = time.Clock()
background = transform.scale(image.load('galaxy.jpg'),(700,500))
ship = Player('rocket.png',7,300,400)
ufo = Enemy('ufo.png',1,200,300)
ufo1 = Enemy('ufo.png',1,200,300)
ufo2 = Enemy('ufo.png',1,200,300)
ufo3 = Enemy('ufo.png',1,200,300)
ufo4 = Enemy('ufo.png',1,200,300)
font.init()
font1 = font.SysFont('Arial', 19)
bullets = sprite.Group()
#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()
ufo13 = sprite.Group()
ufo13.add(ufo)
ufo13.add(ufo1)
ufo13.add(ufo2)
ufo13.add(ufo3)
ufo13.add(ufo4)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                 ship.shoot()
    collides = sprite.groupcollide(ufo13,bullets,True,True)
    for c in collides:
        asriel = Enemy('ufo.png', 3, 0, randint(500, 700))
        ufo13.add(asriel)
    if finish != True:
        win.blit(background,(0,0))
        text1 = font1.render('счёт:' + str(miss),1,(255,255,255), (0,0,0))
        win.blit(text1,(10,10))
        ship.reset()
        ship.update()
        ufo13.draw(win)
        ufo13.update()
        bullets.draw(win)
        bullets.update()
    if sprite.spritecollide(ship, ufo13,True,False):
        text2 = font1.render('Вы проиграли',1,(255,255,255))
        win.blit(text2,(300,200))
        finish = True
    display.update()
    clock.tick(fps)