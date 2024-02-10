import pygame
import math
class Background:
    def __init__(self,screen,bg,width,height):
        self.screen = screen
        self.background = pygame.transform.scale(pygame.image.load(bg).convert(),(width,height))
        self.width = width
        self.bg_width = self.background.get_width()
        self.tiles = math.ceil(self.width / self.bg_width) + 1
    def scroll(self,movement):
        for i in range(self.tiles):
            self.screen.blit(self.background,(i * self.bg_width + movement,0))

class Shooter(pygame.sprite.Sprite):
    def __init__(self,shoot_pic,shoot_sound):
        super().__init__()
        self.image = pygame.image.load(shoot_pic).convert_alpha()
        self.rect = self.image.get_rect()
        self.shoot_sound = pygame.mixer.Sound(shoot_sound)
    def shoot(self,shoot,alien_A,alien_B):
        self.shoot_sound.play()
        if pygame.sprite.spritecollide(shoot,alien_A,True) or pygame.sprite.spritecollide(shoot,alien_B,True):
            return 1
        else:
            return 0
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Alien(pygame.sprite.Sprite):
    def __init__(self,alien_pic,x,y):
        super().__init__()
        self.image = pygame.image.load(alien_pic).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.x = x
        self.y = y
    def update(self,move):
        self.rect.center = [self.x+move,self.y]
