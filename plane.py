import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
class Plane(Sprite,Group):
    def __init__(self,screen):
        Sprite.__init__(self)
        Group.__init__(self)
        #读取图片
        self.image=pygame.image.load('images/plane.jpg')
        self.screen=screen
        #获取图片矩形
        self.rect=self.image.get_rect()
        #获取屏幕矩形
        self.screenRect=self.screen.get_rect()
        self.rect.centerx=self.screenRect.centerx
        self.rect.bottom=self.screenRect.bottom
        self.moveRight=False
        self.moveLeft=False
        self.moveUp = False
        self.moveDown = False

    def update(self,gameSet):
        if self.moveRight==True and self.rect.right<self.screenRect.right:
            self.rect.centerx+=gameSet.planeSpeed
        if self.moveLeft==True and self.rect.left>0:
            self.rect.centerx-=gameSet.planeSpeed
        if self.moveUp==True and self.rect.top>0:
            self.rect.centery-=gameSet.planeSpeed
        if self.moveDown==True and self.rect.bottom!=self.screenRect.bottom:
            self.rect.centery+=gameSet.planeSpeed
    def plane_center(self):
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom
    # def blitme(self,bullet):
    #     self.screen.blit(self.image,self.planeRect)
    #     self.screen.blit(bullet.image,bullet.bulletRect)
    #     pygame.display.flip()

