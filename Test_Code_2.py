

import pygame
from random import randint
#import Input_6

pygame.init()
pygame.joystick.init()
screen = pygame.display.set_mode((795, 410))
pygame.display.set_caption("Rotten Woods")
clock = pygame.time.Clock()
walkRight = [pygame.image.load('Sprites/R1.png'), pygame.image.load('Sprites/R2.png'), pygame.image.load('Sprites/R3.png'), pygame.image.load('Sprites/R4.png'), pygame.image.load('Sprites/R5.png'), pygame.image.load('Sprites/R6.png'), pygame.image.load('Sprites/R7.png'), pygame.image.load('Sprites/R8.png'), pygame.image.load('Sprites/R9.png')]
walkLeft = [pygame.image.load('Sprites/L1.png'), pygame.image.load('Sprites/L2.png'), pygame.image.load('Sprites/L3.png'), pygame.image.load('Sprites/L4.png'), pygame.image.load('Sprites/L5.png'), pygame.image.load('Sprites/L6.png'), pygame.image.load('Sprites/L7.png'), pygame.image.load('Sprites/L8.png'), pygame.image.load('Sprites/L9.png')]
bg = pygame.image.load('ArtWork/background.png')
bg_in = pygame.image.load('ArtWork/background_inside_house_1.png')
bg_mode = "Out"
char = pygame.image.load('Sprites/standing.png')
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)
font = pygame.font.SysFont("impact", 60)
font_1 = pygame.font.SysFont("impact", 25)
Player_health = 0

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = True
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.currentWeapon = 'Pistol'
        self.health = 100
        self.hit_counter = 0
        self.visible = True
        self.weapon_slot = 0


    def draw(self, screen):
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
                
            if not (self.standing):
                if self.left:
                    screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1

                elif self.right:
                    screen.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1

            else:
                if self.right:
                    screen.blit(walkRight[0], (self.x, self.y))
                else:
                    screen.blit(walkLeft[0], (self.x, self.y))
            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, 300, 20))
        pygame.draw.rect(screen, (0, 128, 0), (10, 10, 50 - (3 * (16 - self.health)), 20)) # Player's good health
        text_wep = font_1.render("Weapon: {}".format(player.currentWeapon), 25, (0, 0, 0))
        screen.blit(text_wep, (14, 30))


    def hit(self):
        self.isJump = False
        self.jumpCount = 1
        if goblin.x > self.x:
            if self.x > self.vel:
                self.x = self.x - 35
            else:
                pass

        else:
            if self.x < 795 - self.width - self.vel:
                self.x = self.x + 35

            else:
                pass

        self.y = 335

        self.walkCount = 0
        if self.health > 0:
            self.health -= goblin.dmg
            self.hit_counter = self.hit_counter + 1  # This is the player's hit counter, if is higher than 9 player dies. Food decreases counter.

            if self.hit_counter > 9:
                self.visible = False


    def die(self):
        text = font.render("GAME OVER", 1, (0, 0, 0))

        if self.visible == False:
            screen.blit(text, (420 - (text.get_width() / 2), 80))

            if goblin.x >= self.x:
                self.x = -1000

            else:
                self.x = 1000
            self.currentWeapon = 'Bones'


    def checkWep(self):
        self.weapon_slot += 1

        if self.weapon_slot > 2:
            self.weapon_slot = 0

        if self.weapon_slot == 0:
            self.currentWeapon = 'Pistol'

        elif self.weapon_slot == 1:
            self.currentWeapon = 'Bow'

        elif self.weapon_slot == 2:
            self.currentWeapon = 'Knife'


class Enemy(object):
    walkRight = [pygame.image.load('Sprites/R1E.png'), pygame.image.load('Sprites/R2E.png'), pygame.image.load('Sprites/R3E.png'), pygame.image.load('Sprites/R4E.png'), pygame.image.load('Sprites/R5E.png'), pygame.image.load('Sprites/R6E.png'), pygame.image.load('Sprites/R7E.png'), pygame.image.load('Sprites/R8E.png'), pygame.image.load('Sprites/R9E.png'), pygame.image.load('Sprites/R10E.png'), pygame.image.load('Sprites/R11E.png')]
    walkLeft = [pygame.image.load('Sprites/L1E.png'), pygame.image.load('Sprites/L2E.png'), pygame.image.load('Sprites/L3E.png'), pygame.image.load('Sprites/L4E.png'), pygame.image.load('Sprites/L5E.png'), pygame.image.load('Sprites/L6E.png'), pygame.image.load('Sprites/L7E.png'), pygame.image.load('Sprites/L8E.png'), pygame.image.load('Sprites/L9E.png'), pygame.image.load('Sprites/L10E.png'), pygame.image.load('Sprites/L11E.png')]


    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x+17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = False
        self.dmg = 10
        self.life = True

    def draw(self, screen):
            self.move()

            if self.visible:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0


                if self.vel > 0:
                    screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                    
                else:
                    screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
                pygame.draw.rect(screen, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                self.hitbox = (self.x+17, self.y + 2, 31, 57)

    def move(self):
        if Pause == False:
            if self.vel > 0:
                if self.x + self.vel < player.x + 20:
                    self.x += self.vel

                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0

            else:
                if self.x - self.vel > player.x - 20:
                    self.x += self.vel

                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0


    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 3
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 16 * facing


class Bullet(Projectile):
    def __init__(self, x, y, radius, color, facing):
        Projectile.__init__(self, x, y, radius, color, facing)
        self.vel = 24 * facing


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))

class Arrow(Projectile):
    def __init__(self, x, y, radius, color, facing):
        Projectile.__init__(self, x, y, radius, color, facing)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), int(self.width), int(self.height)))

class Knife(Projectile):
    def __init__(self, x, y, radius, color, facing):
        Projectile.__init__(self, x, y, radius, color, facing)
        self.vel = 8 * facing

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), int(self.width), int(self.height)))



##########################################################################

class Materials(object):
    def __init__(self, x, y, m, health):
        self.x = x
        self.y = y
        self.hit_counter = 0
        self.visible = True
        self.m = m

        def addFood(self, item):
            self._foods.append(item)

        def delFoods(self, item):
            self._foods.remove(item)

    def draw(self, screen):
        #if the players health goes less than 60
        if player.health < 100:
            x = 30
            #this draws the health box at this point
            pygame.draw.rect(screen, (255, 0, 0), (x, 380, 20, 20))
        else:
            m = -20
        #if the player goes to the same place as the box when the players
        #health is less than 60 increase the players health by goblin damage
        if player.x == food.x and player.health <= 60:
            player.health += goblin.dmg
            player.hit_counter = player.hit_counter - 1
        #makes sure players health does not go over 100
        if player.health >= 100:
            player.health = 100
##################################################################



def redrawGameWindow():
    door_x = 730
    door_y = 335
    screen.blit(bg, (0,-55))
    font_1 = pygame.font.SysFont("impact", 25)
    text_wep = font_1.render("Weapon: {}".format(player.currentWeapon), 0, (0, 0, 0))
    screen.blit(text_wep, (14, 30))
    pygame.draw.rect(screen, BROWN, (door_x, door_y, 32, 64))

    if Pause == True:
        pygame.draw.rect(screen, (0, 0, 0), (300, 100, 35, 200))
        pygame.draw.rect(screen, (0, 0, 0), (450, 100, 35, 200))

    if player.visible == False:
        player.die()
        
    player.draw(screen)
    food.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for arrow in arrows:
        arrow.draw(screen)

    for knife in stabs:
        knife.draw(screen)

    for goblin in goblins:
        goblin.draw(screen)
        
    pygame.display.update()

def spawn_range(x):
    if (player.x - 50) <= x:
        x -= 50
        return x

    if (player.x + 50) >= x:
        x += 50
        return x

def proj_cycle(proj, projs):
    if Pause == False:
        if goblin.visible == True:
            if proj.y - proj.radius < goblin.hitbox[1] + goblin.hitbox[3] and proj.y + proj.radius > goblin.hitbox[1]:
                if proj.x + proj.radius > goblin.hitbox[0] and proj.x - proj.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    projs.pop(projs.index(proj))

            if proj.x < 795 and proj.x > 0:
                proj.x += proj.vel

            else:
                projs.pop(projs.index(proj))

        if goblin.visible == False:
            if proj.x < 795 and proj.x > 0:
                proj.x += proj.vel

            else:
                projs.pop(projs.index(proj))





##################################################################


player = Player(300, 335, 64, 64)
goblin = Enemy(100, 340, 64, 64, 400)
#allows the health box to pop up
food = Materials(200, 355, 64, 64)
weapon = [0, 1, 2]
bullets = []
arrows = []
stabs = []
goblins = []
shootLoop = 0
cooldown = 0
run = True
Pause = False



##################################################################



while run:
    clock.tick(27)
    keys = pygame.key.get_pressed()
    x = randint(50, 745)
    
    if Pause == False:
        if goblin.visible == True:
            if player.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and player.hitbox[1] + player.hitbox[3] > goblin.hitbox[1]:
                if player.hitbox[0] + player.hitbox[2] > goblin.hitbox[0] and player.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                    if cooldown == 0:
                        player.hit()
                        cooldown += 5

                    if cooldown > 0:
                        cooldown -= 1


    if shootLoop > 0:
        shootLoop += 1

    if player.currentWeapon == 'Pistol' or player.currentWeapon == 'Knife':
        if shootLoop > 10:
            shootLoop = 0


    elif player.currentWeapon == 'Bow':
        if shootLoop > 20:
            shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if Pause == False:
                    Pause = True
                    pygame.draw.rect(screen, (0, 0, 0), (100, 100, 100, 100))
                elif Pause == True:
                    Pause = False

            if event.key == pygame.K_e:
                if player.x in range(698, 762):
                    if bg_mode == "Out":
                        bg = pygame.image.load('ArtWork/background_inside_house_1.png')
                        bg_mode = "In"

                        if goblin.visible == True:
                            goblins.pop(goblins.index(goblin))
                            spawn_range(x)
                            goblin = Enemy(x, 340, 64, 64, 400)

                    elif bg_mode == "In":
                        bg = pygame.image.load('ArtWork/background.png')
                        bg_mode = "Out"

                        if goblin.visible == True:
                            goblin.visible = False
                            goblins.pop(goblins.index(goblin))


    if Pause == False:
        if keys[pygame.K_c]: # Switch to Pistol - C key
            player.currentWeapon = "Pistol"

        if keys[pygame.K_b]: # Switch to Knife - B key
            player.currentWeapon = "Knife"

        if keys[pygame.K_n]: # Switch to Knife - N key
            player.currentWeapon = "Bow"

        for bullet in bullets:
            proj_cycle(bullet, bullets)

        for arrow in arrows:
            proj_cycle(arrow, arrows)

        for knife in stabs:
            proj_cycle(knife, stabs)


            try:
                if knife.x > player.x + 48:
                    stabs.pop(stabs.index(knife))


                if knife.x < player.x:
                    stabs.pop(stabs.index(knife))



            except:
                pass





        if keys[pygame.K_v]:  # Spawns Zombie - V key
            if len(goblins) < 1:
                goblin.visible = True
                goblins.append(goblin)



            if goblin.visible == False:
                goblins.pop(goblins.index(goblin))
                spawn_range(x)
                goblin = Enemy(x, 340, 64, 64, 400)



        if keys[pygame.K_SPACE] and shootLoop == 0: # Shoots projectile - Space Key
            if player.left:
                facing = -1

            else:
                facing = 1


            if player.currentWeapon == 'Pistol':
                bullets.append(Bullet(round(player.x + player.width // 2), round(player.y + player.height // 2 + 5),  2, (255,255,0), facing))

            if player.currentWeapon == 'Bow':
                arrows.append(Arrow(round(player.x + player.width // 2), round(player.y + player.height // 2 + 5), 4, (162, 42, 42), facing))

            if player.currentWeapon == 'Knife':
                stabs.append(Knife(round((player.x - 5) + player.width // 2), round(player.y + player.height // 2 + 5), 2, (0, 0, 0), facing))
            shootLoop = 1

        if keys[pygame.K_a] and player.x > player.vel: # Moves left - A key
            player.x -= player.vel
            player.left = True
            player.right = False
            player.standing = False

        elif keys[pygame.K_d] and player.x < 795 - player.width - player.vel: # Moves right - D key
            player.x += player.vel
            player.left = False
            player.right = True
            player.standing = False


        else:
            player.standing = True
            player.walkCount = 0

        if not(player.isJump):
            if keys[pygame.K_w]:
                player.isJump = True
                player.walkCount = 0

        else:

            if player.jumpCount >= -10:

                neg = 1

                if player.jumpCount < 0:

                    neg = -1

                player.y -= (player.jumpCount ** 2) * 0.3 * neg
                player.jumpCount -= 1

            else:
                player.isJump = False
                player.jumpCount = 10

    else:
        pass

    redrawGameWindow()


pygame.quit()



