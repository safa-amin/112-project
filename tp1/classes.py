import pygame
import sys
import math

class Character:
    def __init__(self, image, rect, velocity, width, height, iceblocks):
        super().__init__()
        self.image = pygame.image.load("character1.webp")
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        self.velocity = 20
        self.width = width
        self.height = height
        self.iceblocks = iceblocks

    def update_position(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 20
            if self.rect.left < 0:
                self.rect.left = 0

        if keys[pygame.K_RIGHT]:
            self.rect.x += 20
            if self.rect.right > self.width:
                self.rect.right = self.width

        if keys[pygame.K_UP]:
            self.rect.y -= 20
            if self.rect.top < 0:
                self.rect.top = 0

        if keys[pygame.K_DOWN]:
            self.rect.y += 20
            if self.rect.bottom > self.height:
                self.rect.bottom = self.height

    def check_collision(self, iceblocks):
        for block in iceblocks:
            if self.rect.colliderect(block[1]):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.rect.x += 20
                if keys[pygame.K_RIGHT]:
                    self.rect.x -= 20
                if keys[pygame.K_UP]:
                    self.rect.y += 20
                if keys[pygame.K_DOWN]:
                    self.rect.y -= 20
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Fishy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fishy.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 200)
        self.velocity = 5

    def update(self):
        self.rect.x += self.velocity
        if self.rect.left > 1500:
            self.rect.right = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class IceBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ice block.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 5

    def update(self):
        self.rect.x += self.velocity
        if self.rect.left > 1500:
            self.rect.right = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Igloo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("igloo2 copy.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (700, 500)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Monster(pygame.sprite.Sprite):
    def __init__(self, posX, posY, direction, speed, height):
        super().__init__()
        self.image = pygame.image.load("monster3.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200
        self.speed = 5
        self.direction = 1
        self.width = 1500
        self.height = 800
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.direction = direction

    def update_position(self, width):
        self.posX += self.speed * self.direction
        if self.posX + self.width > width:
            self.speed += 1.4
            self.direction = -1
            self.posX = width - self.width
        elif self.posX < 0:
            self.speed += 1.4
            self.direction = 1
            self.posX = 400

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Initialize objects
my_class_instance = Game()
iceblocks = my_class_instance.generate_ice_blocks()
iceblocks = generate_ice_blocks() 
character = Character("character1.webp",pygame.Rect(0, 0, 50, 100), 30, 1500, 800,iceblocks )
monster1 = Monster(1500//2, 800//1.4, 50, 1, 100)
monster2 = Monster(1500 - 1000, 800-400,50, 1, 100)


class Game:
    def __init__(self):
        pygame.init()
        self.width = 1500
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.character = Character("character1.webp",pygame.Rect(0, 0, 50, 100), 30, 1500, 800,[])
        self.fishy = Fishy()
        self.ice_blocks = pygame.sprite.Group()
        self.igloo = Igloo()
        self.monster1 = Monster(1500//2, 800//1.4, 50, 1, 100)
        self.monster2 = Monster(1500 - 1000, 800-400,50, 1, 100)
        self.start_x_list = [100, 1000, 550]
        self.start_y_list = [40, 800, 1000]
        self.spacing_x = 50
        self.spacing_y = 50
        self.num_rows = 9
        self.num_cols = 7
        self.positions = []
        self.iceblocks = []
        self.fishies = []
        self.fishes = []
        self.rect = pygame.Rect(1200, 700, 50, 50)

    def generate_ice_blocks(self):
        iceblocks = []  # Define an empty list to hold the ice blocks

        # Generate positions list for each set of ice blocks
        for start_x in self.start_x_list:
            for start_y in self.start_y_list:
                for row in range(self.num_rows):
                    for col in range(self.num_cols):
                        if row == 0:
                            iceblocks.append((start_x + col * self.spacing_x, start_y))
                        elif col == 0:
                            iceblocks.append((start_x, start_y + row * self.spacing_y))
                        elif col == self.num_cols - 1:
                            iceblocks.append((start_x + col * self.spacing_x, start_y + row * self.spacing_y))

        # Remove duplicates and sort the positions list
        iceblocks = list(set(iceblocks))
        iceblocks.sort()

        # Create ice blocks with rectangles
        iceblocks_rect = []
        for position in iceblocks:
            blockrect = pygame.Rect(position[0], position[1], 50, 50)
            iceblocks_rect.append((position, blockrect))

        return iceblocks_rect  # Return the list of ice blocks

    def generate_fish(self):
        # Define the x and y ranges for generating fishies for each set of fishies
        x_range_list = [200, 1100]
        y_range_list = [125, 800, 1000]

        # Generate fishies using nested loops for each set of fishies
        for x_range in x_range_list:
            for y_range in y_range_list:
                for x in range(x_range, x_range + 200, 100):
                    for y in range(y_range, y_range + 400, 100):
                        self.fishies.append((x, y))

        # Create fish with rectangles
        for fish in self.fishies:
            fishrect = pygame.Rect(fish[0], fish[1], 80, 80)
            self.fishes.append((fish, fishrect))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.all_sprites.update()
            # Update character's position
            character.update_position()
            character.check_collision(iceblocks)
            # Draw background
            for i in range(0, tiles):
                screen.blit(background, (i * bgWidth + change, 0))
                change -= 5
                if abs(change) > bgWidth:
                    change = 0
                    
            # Update monster1 position
            monster1.update_position(width)

            # Update monster2 position
            monster2.update_position(width)
            # Draw game objects
            self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

