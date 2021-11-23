import pygame
from config import *
import math
import random


class Spratethesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x,y,width,height):
        sprite =pygame.Surface([width,height])
        sprite.blit(self.sheet,(0,0), (x,y,width,height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x,y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.player_sprite
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.character_spritesheet.get_sprite(18,12,SHIP_WIDTH, SHIP_HEIGHT)



        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movment()

        self.rect.x += self.x_change
        self.rect.y += self.y_change


        self.x_change = 0
        self.y_change = 0


    def movment(self):
        keys = pygame.key.get_pressed()
        event = pygame.event.get()

        self.image = self.game.character_spritesheet.get_sprite(18, 12, SHIP_WIDTH, SHIP_HEIGHT)

        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.image = self.game.character2_spritesheet.get_sprite(0, 0, SHIP_WIDTH, SHIP_HEIGHT)

            if self.rect.x <=0:
                self.x_change = 0


        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.image = self.game.character1_spritesheet.get_sprite(0, 0, SHIP_WIDTH, SHIP_HEIGHT)

            if self.rect.x >=590:
                self.x_change = 0

        if keys[pygame.K_SPACE] and len(self.game.projectile_player)<3:
            Projectile(self.game, self.rect.x, self.rect.y)



class Projectile(pygame.sprite.Sprite):
    def __init__(self, game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.projectile_player
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y

        self.width = PROJECTILE_TILE_WIDTH
        self.height = PROJECTILE_TILE_HEIGHT

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.projectile_sprite_sheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.y -=6
        self.colide_enemy()
        print(self.rect.y)
        if self.rect.y <= 0:
            self.kill()


    def colide_enemy(self):
        colide_enemy = pygame.sprite.spritecollide(self,self.game.enemies,True)
        if colide_enemy:
            self.kill()






class Ground(pygame.sprite.Sprite):
    def __init__(self,game,x,y, building_number):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.buildings

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y


        self.buildings = [self.game.terrain_spritesheet.get_sprite(320,12,50,100),
                          self.game.terrain_spritesheet.get_sprite(370,12,50,100),
                          self.game.terrain_spritesheet.get_sprite(370,110,50,50),
                          self.game.terrain_spritesheet.get_sprite(60,10,30,50)]


        self.image= self.buildings[building_number]
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.y +=2

class Eneimes(pygame.sprite.Sprite):
    def __init__(self, game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.enemies

        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x
        self.y = y

        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.character_spritesheet.get_sprite(270, 160, ENEMY_SHIP_WIDTH, ENEMY_SHIP_HEIGHT)
        self.image = pygame.transform.rotate(self.image, 180)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.speed_enemy_loop = 1


    def update(self):
        self.movment()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movment(self):
        self.x_change += self.speed_enemy_loop

        if self.rect.x >=600:
            self.speed_enemy_loop = -1
            self.y_change += 20

        if self.rect.x <=0:
            self.speed_enemy_loop = 1
            self.y_change += 20

class ProjectileEnemies(pygame.sprite.Sprite):
    def __init__(self, game,x,y):
        self.game = game
        self.x = x
        self.y = y
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.projectile_enemie,
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.width = PROJECTILE_TILE_WIDTH
        self.height = PROJECTILE_TILE_HEIGHT

        self.image = self.game.projectile_sprite_sheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.y +=6
        if self.rect.y > 481:
            print(len(self.game.projectile_enemie))
            self.kill()
        self.collide_player()

    def collide_player(self):
        colide_player = pygame.sprite.spritecollide(self,self.game.player_sprite, False)
        if colide_player:
            self.kill()
            pygame.quit()

