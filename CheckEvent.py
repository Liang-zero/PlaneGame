import pygame
from bullet import Bullet
from enemy import Enemy
from pygame.sprite import *
from random import *
import sys
from time import sleep


def keydown(event, plane, bullets, screen, gameSet):
    if event.key == pygame.K_SPACE:
        spaceClick(bullets, gameSet, screen, plane)
    if event.key == pygame.K_RIGHT:
        plane.moveRight = True
    if event.key == pygame.K_LEFT:
        plane.moveLeft = True
    if event.key == pygame.K_UP:
        plane.moveUp = True
    if event.key == pygame.K_DOWN:
        plane.moveDown = True
    if event.key == pygame.K_ESCAPE:
        sys.exit()





def spaceClick(bullets, gameSet, screen, plane):
    if len(bullets) <= gameSet.bulletCapacity:
        newBullet = Bullet(screen, plane)
        bullets.add(newBullet)


def keyup(event, plane):
    if event.key == pygame.K_RIGHT:
        plane.moveRight = False
    if event.key == pygame.K_LEFT:
        plane.moveLeft = False
    if event.key == pygame.K_UP:
        plane.moveUp = False
    if event.key == pygame.K_DOWN:
        plane.moveDown = False


def event(plane, bullets, screen, gameSet,stats,play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown(event, plane, bullets, screen, gameSet)
        elif event.type == pygame.KEYUP:
            keyup(event, plane)
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, mouse_x, mouse_y, stats)

def check_play_button(play_button,mouse_x,mouse_y,stats):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        pygame.mouse.set_visible(False)
        stats.game_active=True

def creatEnemy(screen, enemies, gameSet, plane):
    newEnemy = Enemy(screen)
    enemyWidth = newEnemy.rect.width
    enemyHeight = newEnemy.rect.height
    numberx = countNum_x(gameSet, enemyWidth)
    numbery = conuntNum_y(plane, gameSet, enemyHeight)
    for numy in range(numbery + 1):
        for numx in range(numberx + 1):
            enemyCreate_xy(screen, numy, numx, enemyHeight, enemies, enemyWidth)


# 计算x轴能容纳多少敌机
def countNum_x(gameSet, enemyWidth):
    enemyNumx = int((gameSet.height - enemyWidth * 2) / (enemyWidth * 2))
    return enemyNumx


def conuntNum_y(plane, gameSet, enemyHeight):
    enemyNumy = int((gameSet.height - plane.rect.height - 8 * enemyHeight) / (2 * enemyHeight))
    return enemyNumy


# x轴和y轴结合，创建敌机组群
def enemyCreate_xy(screen, numy, numx, enemyHeight, enemies, enemyWidth):
    newEnemy = Enemy(screen)
    everyEnemy_x = enemyWidth + 2 * numx * enemyWidth
    newEnemy.rect.x = everyEnemy_x
    everyEnemy_y = enemyHeight + numy * enemyHeight
    newEnemy.rect.y = everyEnemy_y
    enemies.add(newEnemy)



def updateScreen(plane, bullets, gameSet, enemies, screen,play_button,stats,sbd):
    plane.screen.blit(plane.image, plane.rect)
    enemies.draw(screen)
    sbd.show_score()
    sbd.show_final_score()
    # stats.level = 0
    # sbd.prep_level()
    sbd.level_show()
    if stats.game_active==False:
        sbd.prep_score()
        sbd.prep_level()
        stats.level = 0
        stats.score=0
        play_button.draw_button()
        # for b in enemies.sprites():
        #     b.y+=gameSet.enemySpeed
        #     b.rect.top=b.y
        #     b.updateEnemy()
    pygame.display.flip()


# def bulletRemove(bullets):
#     for b in bullets.copy():
#         if b.rect.bottom <= 0:
#             bullets.remove(b)
#             # print(bullets)


def check_bianyuan(gameSet, enemies):
    for enemy in enemies.sprites():
        if enemy.check_edges():
            change_direction(gameSet,enemies)
            break
        # else:
        #     gameSet.enemyDirection *= -1

def change_direction(gameSet,enemies):
    for enemy in enemies.sprites():
        enemy.rect.y+=gameSet.enemydownSpeed
    gameSet.enemyDirection*=-1

def enemy_update(enemies, gameSet,plane,stats,screen,bullets):
    check_bianyuan(gameSet, enemies)
    enemies.update(gameSet)
    if pygame.sprite.spritecollideany(plane,enemies)!=None:
        plane_hit(gameSet,stats,screen,plane,enemies,bullets)
    check_enemy_bottom(gameSet, stats, screen, plane, enemies, bullets)

def plane_hit(gameSet,stats,screen,plane,enemies,bullets):
    if stats.plane_left>0:
        stats.plane_left-=1
        enemies.empty()
        bullets.empty()
        creatEnemy(screen, enemies, gameSet, plane)
        plane.plane_center()
        sleep(1)
    if stats.plane_left<=0:
        gameSet.chushi()
        pygame.mouse.set_visible(True)
        stats.plane_left=gameSet.heartCount
        stats.game_active=False


def bullet_update(bullets,gameSet, enemies, plane,screen,stats,sbd):
    for a in bullets.sprites():
        a.update(gameSet)
    # bullets.update(gameSet)
    for b in bullets.copy():
        if b.rect.bottom <= 0:
            bullets.remove(b)
            print(bullets)
    removeCount = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if removeCount:
        for enemies in removeCount.values():
            stats.score +=5*len(enemies)
            sbd.prep_score ()
        if stats.score>=stats.final_score:
            stats.final_score=stats.score
            sbd.prep_final_score()
        else:
            stats.final_score=stats.final_score
            sbd.prep_final_score()
    if len(enemies) == 0:
        # bullets.empty()


        # sbd.level_show()
        gameSet.increase_speed()
        stats.level += 1
        sbd.prep_level()
        creatEnemy(screen, enemies, gameSet, plane)

def check_enemy_bottom(gameSet,stats,screen,plane,enemies,bullets):
    screen_rect=screen.get_rect()
    for a in enemies.sprites():
        if a.rect.bottom>screen_rect.bottom:
            plane_hit(gameSet, stats, screen, plane, enemies, bullets)
            break



