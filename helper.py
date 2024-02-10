from characters import Alien, Shooter
import pygame
import random
def create_aliens(img,SCREEN_WIDTH,SCREEN_HEIGHT,side):
    alien_group = pygame.sprite.Group()
    aliens = []
    alien_cnt = 0
    start = 0
    end = 0

    if side == "front":
        start = SCREEN_WIDTH
        end = SCREEN_WIDTH*2
    elif side == "back":
        start = SCREEN_WIDTH*2
        end = SCREEN_WIDTH*3

    while alien_cnt < 12:
        shld_add = True
        new_alien = Alien(img,random.randrange(start, end), random.randrange(150,SCREEN_HEIGHT-100))
        for alien in aliens:
            if pygame.sprite.collide_rect(alien,new_alien) == True:
                shld_add = False
                break
        if shld_add == True:
            aliens.append(new_alien)
            alien_group.add(new_alien)
            alien_cnt += 1

    return alien_group

def score_board(score,width,height,screen):
    font = pygame.font.SysFont("Arial",40)
    display = font.render(score,True,(255,255,255))
    displayRect = display.get_rect()
    displayRect.center = (width-200,height-800)
    screen.blit(display,displayRect)

def timer(frame,width,height,screen,fps):
    time = frame//fps
    font = pygame.font.SysFont("Arial", 40)
    display = font.render(str(time), True, (255, 255, 255))
    displayRect = display.get_rect()
    displayRect.center = (30,height-820)
    screen.blit(display, displayRect)
    return time

def game_over(width,height,screen):
    font = pygame.font.SysFont("Arial", 100)
    display = font.render("GAME OVER", True, (255, 255, 255))
    displayRect = display.get_rect()
    displayRect.center = (width//2-40, height//2)
    screen.blit(display, displayRect)



