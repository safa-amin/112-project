import pygame
import math
# from gameplay import game
##setting up the display

pygame.init()
width, height = 1500,600
clock = pygame.time.Clock()
color = pygame.color.Color('#FFFFFF')
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Menu")

##original height and width
screenwidth = 1500
screenheight = 600
run = True
#setting up background
velocity = 30
## i got these images from google
background = pygame.image.load("snowflakesbackground.gif").convert()
background = pygame.transform.scale(background,(width,height))
bgWidth = background.get_width()
#the logo image will be changed later to reflect my game's character and title
logo = pygame.image.load("gamelogo.webp")
logo1 = pygame.transform.scale(logo, (500,400))

##defining game variables
scroll = 0
tiles = math.ceil(width/bgWidth)+1
## quitting game
def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
##function for drawing text
def drawtext(string, font, textcolor,x, y):
    image = font.render(string, True, textcolor)
    screen.blit(image, (x,y))    
## fonts
font = pygame.font.SysFont("arialblack", 40)
##color
textcolor = (255,50,200)
gameContinue = False

while run:
    quit_game()
    clock.tick(velocity)        
    ##draw the backround
    for i in range(0,tiles):
        screen.blit(background, (i*bgWidth + scroll,0))
    ## scrolling
        scroll -= 5
    ## resetting the scroll
        if abs(scroll)>bgWidth:
            scroll = 0
            
     ##showing the text
    if gameContinue == True:
        pass
    else:
        drawtext("Press SPACE to continue", font, textcolor,500,500)
    ##keypresses
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameContinue = True
            if event.type == pygame.QUIT:
                run = False                              
    
    ##logo
    screen.blit(logo1, (screenwidth//3,screenheight//12))
    pygame.display.update()
    
pygame.quit()