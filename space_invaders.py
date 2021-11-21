import pygame
from all_sprites_in_the_game import *
from config import *
import sys


class SpaceInvaders:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = Spratethesheet("img/shipsheetparts.PNG")
        self.character1_spritesheet = Spratethesheet("img/player/player_right.png")
        self.character2_spritesheet = Spratethesheet("img/player/player_left.png")
        self.terrain_spritesheet = Spratethesheet("img/background/colony.png")

    def createTilemap(self):
        self.buidlings =[
            Ground(self, 10, -210, random.randint(0, 2)),
            Ground(self, 50, -280, random.randint(0, 2)),
            Ground(self,90,-100,random.randint(0, 2)),
            Ground(self,140,-190,random.randint(0, 2)),
            Ground(self,190,-50,random.randint(0, 2)),
            Ground(self,250,-120,random.randint(0, 2)),
            Ground(self,280,-380,random.randint(0, 2)),
            Ground(self,580,-300,random.randint(0, 2)),
            Ground(self, 90, -620, random.randint(0, 2)),
            Ground(self, 140, -430, random.randint(0, 2)),
            Ground(self, 190, -330, random.randint(0, 2)),
            Ground(self, 250, -480, random.randint(0, 2)),
            Ground(self, 280, -550, random.randint(0, 2)),
            Ground(self, 430, -620, random.randint(0, 2)),
            Ground(self, 490, -430, random.randint(0, 2)),
            Ground(self, 550, -130, random.randint(0, 2)),
            Ground(self, 660, -480, random.randint(0, 2)),
            Ground(self, 350, -550, random.randint(0, 2))
        ]









    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.buildings = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attack = pygame.sprite.LayeredUpdates()


        self.player = Player(self,320,400) # the numbers is giving a position of the character

        x=50
        for i in range(11):
            Eneimes(self,x,50)
            x+=50
        self.createTilemap()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False


    def update(self):
        self.all_sprites.update()

        for sprite in self.buildings:
            if sprite.rect.y >=482:
                sprite.rect.y = -100

        # for sprite in self.enemies:
        #     sprite.rect.x += self.speed_enemy
        #     if sprite.rect.x >=550:
        #         self.speed_enemy = 0
        #         self.speed_enemy=-1
        #
        #     if sprite.rect.x <=10:
        #         self.speed_enemy = 0
        #         self.speed_enemy = 1


    def draw(self):
        self.screen.fill(GREEN_BACKGROUND)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass


g = SpaceInvaders()
g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()