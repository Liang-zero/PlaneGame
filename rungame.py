import pygame
from gameSetting import Setting
from plane import Plane
from CheckEvent import *
# from bullet import Bullet
from pygame.sprite import Group
from enemy import Enemy
from game_qingkuang import Gameqingkuang
from button import Button
from integral import Integral
from multiprocessing import Process
def rungame():
    pygame.init()
    gameSet=Setting()
    screen=pygame.display.set_mode((gameSet.height,gameSet.width))
    plane = Plane(screen)
    # bullet = Bullet(screen, plane)
    # plane = Plane(screen)
    # bullet = Bullet(screen,plane)
    play_button=Button(screen,"Play")

    pygame.display.set_caption("飞机大战")
    bullets=Group()
    enemies=Group()
    stats=Gameqingkuang(gameSet)
    sbd=Integral(screen,gameSet,stats)
    creatEnemy(screen,enemies,gameSet,plane)

    while True:

        event(plane, bullets, screen, gameSet,stats,play_button)
        screen.fill(gameSet.color)
        updateScreen(plane, bullets, gameSet, enemies, screen, play_button, stats,sbd)
        if stats.game_active:

            plane.update(gameSet)
            bullet_update(bullets,gameSet, enemies, plane,screen,stats,sbd)
            enemy_update(enemies, gameSet,plane,stats,screen,bullets)
            updateScreen(plane,bullets,gameSet,enemies,screen,play_button,stats,sbd)
            # if stats.plane_left==0:
            #     stats.game_active = False
            #     break

        # print(stats.game_active)
            print(stats.plane_left)




        # bullets.update()
        # pygame.display.update()






def main():
    rungame()

if __name__ == '__main__':
    main()