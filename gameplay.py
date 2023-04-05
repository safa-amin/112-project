import pygame
import math

# def game():
##setting up the display
pygame.init()
width, height = 1500,600
clock = pygame.time.Clock()
color = pygame.color.Color('#FFFFFF')
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Game")
x = 1500
y = 600
run = True
#setting up background
velocity = 20
background = pygame.image.load("whitebg.jpeg").convert()
background = pygame.transform.scale(background,(width,height))
bgWidth = background.get_width()
##setting up the character
character = pygame.image.load('character1.webp')
changecharacter = pygame.transform.scale(character, (50,100))
#setting rectangle around character
rect = changecharacter.get_rect()
##setting up the obstacles
iceblock = pygame.image.load('ice block.png')
changeiceblock = pygame.transform.scale(iceblock, (100,100))
changeiceblock1 = pygame.transform.scale(iceblock, (100,100))
changeiceblock2 = pygame.transform.scale(iceblock, (100,100))
changeiceblock3 = pygame.transform.scale(iceblock, (100,100))
changeiceblock4 = pygame.transform.scale(iceblock, (100,100))
changeiceblock5 = pygame.transform.scale(iceblock, (100,100))
changeiceblock6 = pygame.transform.scale(iceblock, (100,100))
#setting home for panda
igloo2 = pygame.image.load('igloo2 copy.png')
igloo2 = pygame.transform.scale(igloo2, (200,200))
##setting the enemies to move on their own
imgwidth = 100
imgheight = 100
monster = pygame.image.load("monster2.png")
monster = pygame.transform.scale(monster, (imgwidth,imgheight))
##initial position of image
imgposX = width - 1200
imgposY = 0 - imgheight
imgspeed = 5
imgdirection = -1
#rectangles around obstacles
blockrect = changeiceblock.get_rect()
blockrect1 = changeiceblock1.get_rect()
##defining game variables
change = 0
tiles = math.ceil(x/bgWidth)+1
## quitting game
def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
##intitiate character movement with arrow keys
while run:
    quit_game()
    clock.tick(velocity)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.x -= 5
    if keys[pygame.K_RIGHT]:
        rect.x+= 5
        
    if keys[pygame.K_UP]:
        rect.y -= 5
        
    if keys[pygame.K_DOWN]:
        rect.y += 5
    ##draw the backroun
    for i in range(0,tiles):
        screen.blit(background, (i*bgWidth + change,0))
    ## changeing
        change -= 5
    ## resetting the change
        if abs(change)>bgWidth:
            change = 0
            
#     if imgposX + imgwidth > width:
#         imgspeed -= imgspeed
#     elif imgposX<0:
#         imgspeed = abs(imgspeed)
#     imgposX += imgspeed
    
    if imgposY + imgheight > height:
        imgspeed *= -1
        imgdirection = 1
        imgposY = height - imgheight
    elif imgposY<0:
        imgspeed *= -1
        imgdirection = 1
        imgposY = 0
    imgposY += imgspeed * imgdirection
        
    ##verticle blocks
    screen.blit(changeiceblock, (400,100))
    screen.blit(changeiceblock1, (400,190))
    screen.blit(changeiceblock2, (400,280))
    screen.blit(changeiceblock3, (400,370))
    screen.blit(changeiceblock4, (400,460))
     ##horizontal blocks at top
    screen.blit(changeiceblock1, (500,100))
    screen.blit(changeiceblock2, (600,100))
    screen.blit(changeiceblock3, (700,100))
    screen.blit(changeiceblock3, (800,100))
    ##horizontal blocks at bottom
    screen.blit(changeiceblock3, (400,460))
    screen.blit(changeiceblock1, (500,460))
    screen.blit(changeiceblock2, (600,460))
    screen.blit(changeiceblock3, (700,460))
    screen.blit(changeiceblock3, (800,460))
    ##vertical blocks
    screen.blit(changeiceblock, (900,100))
    screen.blit(changeiceblock1, (900,190))
    screen.blit(changeiceblock2, (900,280))
    screen.blit(changeiceblock3, (900,370))
    screen.blit(changeiceblock4, (900,460))
    ## igloo home  
    screen.blit(igloo2, (600,235))
    ##monster
    screen.blit(changecharacter, rect)
    screen.blit(monster, (imgposX, imgposY))    
    ##collision
    if rect.colliderect(blockrect):
        pygame.draw.rect(screen,(0,0,0),rect,1)
    
    pygame.display.update()
    
pygame.quit()
    
    
