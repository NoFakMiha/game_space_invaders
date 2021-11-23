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
        self.timer_enemie_projectile = 10
        self.x_enemies = []
        self.y_enemies = []

        self.character_spritesheet = Spratethesheet("img/shipsheetparts.PNG")
        self.character1_spritesheet = Spratethesheet("img/player/player_right.png")
        self.character2_spritesheet = Spratethesheet("img/player/player_left.png")
        self.projectile_sprite_sheet = Spratethesheet("img/jrob774-explosion_2-sheet-alpha.png")
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
        self.player_sprite = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.projectile_player = pygame.sprite.LayeredUpdates()
        self.projectile_enemie = pygame.sprite.LayeredUpdates()


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
        self.timer_enemie_projectile -=1

        if self.timer_enemie_projectile == 0:
            for enemies in self.enemies:
                self.x_enemies.append(enemies.rect.x)
                self.y_enemies.append(enemies.rect.y)
            ProjectileEnemies(self,random.choice(self.x_enemies),random.choice(self.y_enemies) )
            self.timer_enemie_projectile = 60
            self.x_enemies = []
            self.y_enemies = []

        for sprite in self.buildings:
            if sprite.rect.y >=482:
                sprite.rect.y = -100


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