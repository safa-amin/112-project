import pygame, sys
import math
from menubuttons import startbuttons
from creditspage import showcredits
##setting up the display
pygame.init()
width, height = 1500,800
clock = pygame.time.Clock()
color = pygame.color.Color('#FFFFFF')
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Menu")

##original height and width
screenwidth = 1500
screenheight = 800
run = True
#setting up background 
velocity = 30 
## i got these images from google
background = pygame.image.load("snowflakesbackground.gif").convert()
background = pygame.transform.scale(background,(width,height))
bgWidth = background.get_width()
#original logo that i made
logo = pygame.image.load("bearofficiallogo.png")
logo1 = pygame.transform.scale(logo, (500,500))

##defining game variables
scroll = 0
tiles = math.ceil(width/bgWidth)+1
##function for drawing text
def drawtext(string, font, textcolor,x, y):
    image = font.render(string, True, textcolor)
    screen.blit(image, (x,y))    
## fonts
font = pygame.font.SysFont("arialblack", 40)
##color
textcolor = (48,52,168)
gameContinue = False
##collision boolean

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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
        startbuttons()
        break
    else:
        drawtext("Press SPACE to continue", font, textcolor,450,600)
    ##keypresses
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                gameContinue = True
        if event.type == pygame.QUIT:  
            run = False
            pygame.quit()
            sys.exit()
    
    ##logo
    screen.blit(logo1, (screenwidth//3,screenheight//12))
    pygame.display.update()


pygame.quit()