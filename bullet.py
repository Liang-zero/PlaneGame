import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,screen,plane):
       Sprite.__init__(self)
       self.screen=screen
       self.image=pygame.image.load("images/飞船.png")
       self.rect=self.image.get_rect()
       self.rect.centerx=plane.rect.centerx
       self.rect.top=plane.rect.top-30


 

    def update(self,gameSet):
        self.screen.blit(self.image,self.rect)
        self.rect.top -= gameSet.bulletSpeed


