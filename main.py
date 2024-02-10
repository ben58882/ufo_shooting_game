import pygame, sys
from characters import Background
from helper import *

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 864
fps = 15

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

score = 0
frame_cnt = 0
game_play_time = 60
gameover = False


background = Background(screen,"space.webp",SCREEN_WIDTH,SCREEN_HEIGHT)
movement = 0
move = -5

shooter = Shooter("crosshair_red_small.png","shoot_sound.mp3")
shooter_grp = pygame.sprite.Group()
shooter_grp.add(shooter)

alien_grp_A = create_aliens("ufos-red-1-1.png",SCREEN_WIDTH,SCREEN_HEIGHT,"front")
alien_grp_A_cnt = [0,SCREEN_WIDTH*2]

alien_grp_B = create_aliens("ufos-red-1-1.png",SCREEN_WIDTH,SCREEN_HEIGHT,"back")
alien_grp_B_cnt = [0,SCREEN_WIDTH*3]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            score += shooter.shoot(shooter,alien_grp_A,alien_grp_B)

    pygame.display.flip()
    background.scroll(movement)
    score_board(str(score),SCREEN_WIDTH,SCREEN_HEIGHT,screen)

    if timer(frame_cnt,SCREEN_WIDTH,SCREEN_HEIGHT,screen,fps) == game_play_time:
        move = 0
        gameover = True
    else:
        frame_cnt += 1

    movement += move

    if abs(movement) > background.bg_width:
        movement = 0

    if abs(alien_grp_A_cnt[0]) >= alien_grp_A_cnt[1]:
        alien_grp_A = create_aliens("target_red3_outline.png",SCREEN_WIDTH,SCREEN_HEIGHT,"front")
        alien_grp_A_cnt[0] = 0
        alien_grp_A_cnt[1] = SCREEN_WIDTH*2

    elif abs(alien_grp_B_cnt[0]) >= alien_grp_B_cnt[1]:
        alien_grp_B = create_aliens("target_red3_outline.png",SCREEN_WIDTH,SCREEN_HEIGHT,"front")
        alien_grp_B_cnt[0] = 0
        alien_grp_B_cnt[1] = SCREEN_WIDTH * 2

    alien_grp_A.draw(screen)
    alien_grp_A.update(alien_grp_A_cnt[0])
    alien_grp_A_cnt[0] += move

    alien_grp_B.draw(screen)
    alien_grp_B.update(alien_grp_B_cnt[0])
    alien_grp_B_cnt[0] += move

    shooter_grp.draw(screen)
    if gameover == False:
        shooter_grp.update()
    else:
        game_over(SCREEN_WIDTH, SCREEN_HEIGHT, screen)

    clock.tick(fps)

pygame.quit()

