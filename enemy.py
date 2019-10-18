import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
class Enemy(Sprite,Group):
    def __init__(self,screen):
        Sprite.__init__(self)
        Group.__init__(self)
        self.screen=screen
        self.image=pygame.image.load("images/enemy.png")
        self.rect=self.image.get_rect()
        # self.screen_rect=self.screen.get_rect()
        self.rect.y=float(self.rect.height)
        self.x=float(self.rect.x)
        # self.enemyRect.left=randint(0,800)
        # self.enemyRect.top=randint(-5*1200,0)
        # self.enemyNum=int((self.screen_rect.width)/(self.enemyRect.width*2))

    # def updateEnemy(self):
    #     self.screen.blit(self.image,self.rect)
    def update(self,gameSet):
            self.rect.x += gameSet.enemyrlSpeed*gameSet.enemyDirection

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        if self.rect.left<=0:
            return True