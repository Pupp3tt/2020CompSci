import pygame
pygame.init()
pygame.joystick.init()

screen = pygame.display.set_mode((852, 480))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
walkRight = [pygame.image.load('Sprites/R1.png'), pygame.image.load('Sprites/R2.png'), pygame.image.load('Sprites/R3.png'), pygame.image.load('Sprites/R4.png'), pygame.image.load('Sprites/R5.png'), pygame.image.load('Sprites/R6.png'), pygame.image.load('Sprites/R7.png'), pygame.image.load('Sprites/R8.png'), pygame.image.load('Sprites/R9.png')]
walkLeft = [pygame.image.load('Sprites/L1.png'), pygame.image.load('Sprites/L2.png'), pygame.image.load('Sprites/L3.png'), pygame.image.load('Sprites/L4.png'), pygame.image.load('Sprites/L5.png'), pygame.image.load('Sprites/L6.png'), pygame.image.load('Sprites/L7.png'), pygame.image.load('Sprites/L8.png'), pygame.image.load('Sprites/L9.png')]
bg = pygame.image.load('ArtWork/background.png')
char = pygame.image.load('Sprites/standing.png')
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.currentWeapon = 'Gun'
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

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        if goblin.x > self.x:
            self.x = self.x - 35
        else:
            self.x = self.x + 35
        self.y = 410
        self.walkCount = 0
        if self.health > 0:
            self.health -= goblin.dmg
            self.hit_counter = self.hit_counter + 1  # This is the player's hit counter, if is higher than 9 player dies. Food decreases counter.
            if self.hit_counter > 9:
                self.visible = False
                self.x = 280
                self.y = 280
                self.isJump = True

    def die(self):
        font = pygame.font.SysFont("impact", 60)
        text = font.render("GAME OVER", 1, (0, 0, 0))
        if self.visible == False:
            screen.blit(text, (440 - (text.get_width() / 2), 60))

    def checkWep(self):
        self.weapon_slot += 1
        if self.weapon_slot > 2:
            self.weapon_slot = 0

        if self.weapon_slot == 0:
            self.currentWeapon = 'Gun'
        elif self.weapon_slot == 1:
            self.currentWeapon = 'Bow'
        elif self.weapon_slot == 2:
            self.currentWeapon = 'Spear'

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
        self.vel = 1
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

    def spawn(self):
        self.life = True
        if self.life == True:
            self.move()
            self.draw(screen)
        elif self.life == False:
            self.spawn()


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 3
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, screen):
        if player.currentWeapon == 'Gun':
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))
        elif player.currentWeapon == 'Bow' or player.currentWeapon == 'Spear':
            pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), int(self.width), int(self.height)))

##########################################################################

class Materials(object):
    pass


class food(Materials):
    def __init__(self):
        Materials.__init__(self)

    pass


class drinks(Materials):
    def __init__(self):
        Materials.__init__(self)

    pass

def redrawGameWindow():
    screen.blit(bg, (0,0))
    if player.visible == False:
        player.die()
    player.draw(screen)
    for projectile in projectiles:
        projectile.draw(screen)
    for goblin in goblins:
        goblin.spawn()
    pygame.display.update()

player = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
projectiles = []
goblins = []
shootLoop = 0
run = True

while run:
    clock.tick(27)

    keys = pygame.key.get_pressed()

    if goblin.visible == True:
        if player.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and player.hitbox[1] + player.hitbox[3] > goblin.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > goblin.hitbox[0] and player.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                player.hit()

    if shootLoop > 0:
        shootLoop += 1
    if player.currentWeapon == 'Gun':
        if shootLoop > 10:
            shootLoop = 0
    elif player.currentWeapon == 'Bow':
        if shootLoop > 20:
            shootLoop = 0
    elif player.currentWeapon == 'Spear':
        if shootLoop > 10:
            shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                player.checkWep()


    if goblin.visible == True:
        for projectile in projectiles: #projectile
            if projectile.y - projectile.radius < goblin.hitbox[1] + goblin.hitbox[3] and projectile.y + projectile.radius > goblin.hitbox[1]:
                if projectile.x + projectile.radius > goblin.hitbox[0] and projectile.x - projectile.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    projectiles.pop(projectiles.index(projectile))
            if projectile.x < 852 and projectile.x > 0:
                if player.currentWeapon == 'Gun':
                    projectile.x += projectile.vel * 2
                elif player.currentWeapon == 'Bow':
                    projectile.x += projectile.vel
                elif player.currentWeapon == 'Spear':
                    projectile.x += projectile.vel
                    try:
                        if projectile.x > player.x + 48:
                            projectiles.pop(projectiles.index(projectile))
                        if projectile.x < player.x:
                            projectiles.pop(projectiles.index(projectile))
                    except:
                        pass

            else:
                projectiles.pop(projectiles.index(projectile))
    if goblin.visible == False:
        for projectile in projectiles: #projectile
            if projectile.x < 852 and projectile.x > 0:
                if player.currentWeapon == 'Gun':
                    projectile.x += projectile.vel * 2
                elif player.currentWeapon == 'Bow':
                    projectile.x += projectile.vel
                elif player.currentWeapon == 'Spear':
                    projectile.x += projectile.vel
                    try:
                        if projectile.x > player.x + 48:
                            projectiles.pop(projectiles.index(projectile))
                        if projectile.x < player.x:
                            projectiles.pop(projectiles.index(projectile))
                    except:
                        pass

            else:
                projectiles.pop(projectiles.index(projectile))

    if keys[pygame.K_v] and len(goblins) < 1:
        goblin.visible = True
        goblins.append(goblin)
        if len(goblins) < 1:
            if goblin.visible == False:
                print
                goblins.pop(goblins.index(goblin))


    if keys[pygame.K_SPACE] and shootLoop == 0:
        if player.left:
            facing = -1
        else:
            facing = 1
        if len(projectiles) < 5:
            if player.currentWeapon == 'Gun':
                projectiles.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2),  2, (255,255,0), facing))
            elif player.currentWeapon == 'Bow':
                projectiles.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 4, (162, 42, 42), facing))
            elif player.currentWeapon == 'Spear':
                projectiles.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2 + 5), 2, (0, 0, 0), facing))
        shootLoop = 1
    if keys[pygame.K_a] and player.x > player.vel: # left and might be able to use pygame.joystick command
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_d] and player.x < 865 - player.width - player.vel: # right, use pygame.joystick command
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
            player.right = False
            player.left = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    redrawGameWindow()

pygame.quit()
