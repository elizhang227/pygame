import pygame

KEY_UP = 273       ## For arrow key inputs
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Character(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        self.speed = 5        

class Hero(Character):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        self.vx = 5
        self.vy = 5        

class Monster(Character):
    def update(self, width, height):
        self.x += self.speed
        self.y += self.speed
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0    

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    background_image = pygame.image.load('images/background.png').convert_alpha()   ## LOAD IMAGES TO SCREEN
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()

    player = Hero(hero_image, 250, 250)
    # player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    # player.vx = 5
    # player.vy = 5

    monster = Monster(monster_image, 70, 70)

    player_group = pygame.sprite.Group()
    player_group.add(player)

    monster_group = pygame.sprite.Group()
    monster_group.add(monster)

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        # Event handling

        key = pygame.key.get_pressed()

        for i in range(2):                               # MOVES THE CHARACTER
            if key[player.move[i]]:
                player.rect.x += player.vx * [-1, 1][i]

        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy * [-1, 1][i]          

            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        
        hit = pygame.sprite.spritecollide(player, monster_group, True)

        if hit:
            # if collision is detected call a function in your case destroy
            # bullet
            monster.image.fill((255, 255, 255))   

        #player.update(width, height)     
        monster.update(width, height)
        # Draw background
        screen.blit(background_image, [0,0]) # top left coordinates [0,500] = bottom left [500,0] = top right
        # Game display
        player_group.draw(screen)
        monster_group.draw(screen)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
