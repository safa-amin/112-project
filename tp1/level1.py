def main():  
    import pygame, sys
    import math
    from death import dead
    from level2screen import level2screen
    from menubuttons import startbuttons

    pygame.init()
    width, height = 1500,800
    clock = pygame.time.Clock()
    # Set up game state and countdown
    gameState = "Playing"
    countdown = 60
    frame_counter = 0
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Main Menu")
    run = True
    score = 0
    #setting up background
    velocity = 20
    level = 1
    background = pygame.image.load("whitebg.jpeg").convert()
    background = pygame.transform.scale(background,(width,height))
    bgWidth = background.get_width()

    ##setting up the character
    character = pygame.image.load('character1.webp')
    changecharacter = pygame.transform.scale(character, (50,100))
    #setting rectangle around character
    rect = changecharacter.get_rect()


    ##setting up the fishes as scores
    fishy = pygame.image.load('fishy.png')
    changefishy = pygame.transform.scale(fishy, (50,50))
    #setting rectangle around character
    fishrect = changecharacter.get_rect()

    ##setting up the obstacles
    iceblock = pygame.image.load('ice block.png')
    changeiceblock = pygame.transform.scale(iceblock, (90,90))
    #rectangles around obstacles
    blockrect = changeiceblock.get_rect()

    #setting home for character
    igloo2 = pygame.image.load('igloo2 copy.png')
    igloo2 = pygame.transform.scale(igloo2, (125,125))
    ##initial position of igloo
    iglooPosX = 625
    iglooPosY = 325

    ##setting the enemies to move on their own
    monster1width = 100
    monster1height = 100

    #setting up monster1
    monster = pygame.image.load("wintermonster.png").convert_alpha()
    #transforming monster image to fit the screen
    monsternew = pygame.transform.scale(monster, (monster1width,monster1height))
    #getting mosnter rectangle
    monster1rect = monster.get_rect()

    #setting up monster2
    monster2height = 100
    monster2 = pygame.image.load("wintermonster.png").convert_alpha()
    #transforming monster image to fit the screen
    monster2new = pygame.transform.scale(monster2, (monster1width,monster1height))
    #getting mosnter rectangle
    monster2rect = monster2.get_rect()

    ##initial position of monster1
    monster1posX = width - 1300 #the monster on the left side
    monster1posY = 0 - monster1height
    monster1speed = 8 
    monster1Direction = -1#making sure it goes up and down

    ##initial position of monster2
    monster2posX = 1100#monster on the right side
    monster2posY = height
    monster2speed = 5
    monster2Direction = 1 #up and down but opposite monster 1

    ##level
    level = 1
    ##establishin font function
    def drawtext(string, font, pink,x, y):
        image = font.render(string, True, pink)
        screen.blit(image, (x,y))    
    font = pygame.font.SysFont("arialblack", 20)
    ##color of font
    pink = (255,50,200)
    color = (118,56,98)
    BLUE = (180,213,255)
    ##defining block list
    change = 0
    tiles = math.ceil(width/bgWidth)+1
    #the positions list is the x and y coordinate of where the iceblocks are
    positions = [
    (300, 100), (300, 190), (300, 280), (300, 370), (300, 460), (300, 560),
    (600, 100), (500, 100), (900, 100), (800, 100), (700, 100), (1000, 100),(400, 100),
    (500, 560), (400, 560),(800, 560), (900, 560),
    (1000, 100), (1000, 190), (1000, 280), (1000, 370), (1000, 460), (1000, 560),]
    iceblocks = []
    for position in positions:
            #setting rectangle for each iceblock by using each tuple
            blockrect = pygame.Rect(position[0], position[1], 80, 80)
            #appending into new list to use for blit and collision
            iceblocks.append((position,blockrect))
            
  
    ##list of the fishes as their x and y coordinates for positions
    fishies = [(400, 200), (400, 500), (500, 200),(500, 500),
           (800, 200),(800, 500), (900, 200), (900, 500),
           (1100, 125),(1100, 200), (200,200),(200, 125),
           (200, 500), (200, 425),(200, 575), (1100, 500), (1100, 425),(1100, 575)]

    fishes = []
    for fish in fishies:
        # setting rectangle for each fish
        fishrect = pygame.Rect(fish[0], fish[1], 80, 80)
        fishes.append((fish, fishrect))   
    ##intitiate character movement with arrow keys
    rect = pygame.Rect(650, 700, 50, 50)
    while run:
        #quitgame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #when esc button is press, return to main menu
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                startbuttons()
        #setting up a timer
        # Update game state and countdown
        if gameState == "Playing":
            frame_counter += 1
            if frame_counter % 20 == 0:#mod 20 to get each sec
                countdown -= 1
                if countdown == 0:
                    gameState = "Dead" #when it is gameover

        clock.tick(velocity)
        
        #only do character movment if no collision is detected
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:#if left arrow key is press, character moves left
            rect.x -= 20
            if rect.left < 0:
                rect.left = 0
            
        if keys[pygame.K_RIGHT]:#if right arrow key is press, character moves left
            rect.x+= 20
            if rect.right > width:
                rect.right = width
            
        if keys[pygame.K_UP]: #if up arrow key is press, character moves left
            rect.y -= 20
            if rect.top < 0:
                rect.top = 0
                    
        if keys[pygame.K_DOWN]:#if down arrow key is press, character moves left
            rect.y += 20
            if rect.bottom > height:
                rect.bottom = height - rect.height 
        
        
        
        for block in iceblocks:
            if rect.colliderect(block[1]):
                # stop character movement after character rectangle collide w block
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    rect.x += 20
                if keys[pygame.K_RIGHT]:
                    rect.x -= 20
                if keys[pygame.K_UP]:
                    rect.y += 20
                if keys[pygame.K_DOWN]:
                    rect.y -= 20
                

        ##draw the backroun
        for i in range(0,tiles):
            screen.blit(background, (i*bgWidth + change,0))
        ## changeing
            change -= 5
        ## resetting the change
            if abs(change)>bgWidth:
                change = 0
                
        ##make monster go up and down        
        if monster1posY + monster1height > height:
            monster1speed *= -1
            monster1Direction = 1 #change to go up and down
            monster1posY = height - monster1height
        elif monster1posY<0:
            monster1speed *= -1
            monster1Direction = 1
            monster1posY = 0
        monster1posY += monster1speed * monster1Direction
        monster1rect.topleft = (monster1posX, monster1posY)
        
        ##make monster2 go up and down        
        if monster2posY + monster2height > height:
            monster2speed *= -1
            monster2Direction = -1 # Change direction to -1 for upward movement
            monster2posY = height - monster2height
        elif monster2posY < 0:
            monster2speed *= -1
            monster2Direction = 1 # Change direction to 1 for downward movement
            monster2posY = 0
        monster2posY += monster2speed * monster2Direction
        monster2rect.topleft = (monster2posX, monster2posY)
        
        #masking
        charactermask = pygame.mask.from_surface(changecharacter)
        charactermaskrect = charactermask.get_rect()
        charactermaskrect.center = rect.center
        # Update monster mask position
        monster1mask = pygame.mask.from_surface(monsternew)
        monster1maskrect = monster1mask.get_rect()
        monster1maskrect.center = monster1rect.center
        # Update monster2 mask position
        monster2mask = pygame.mask.from_surface(monster2new)
        monster2maskrect = monster2mask.get_rect()
        monster2maskrect.center = monster2rect.center
        #igloo mask
        igloomask = pygame.mask.from_surface(igloo2)
        igloomaskrect = igloomask.get_rect()
        igloomaskrect = pygame.Rect(iglooPosX + 20, iglooPosY + 20, igloo2.get_width() - 20, igloo2.get_height() - 40)
        igloomaskrect.left = igloomaskrect.left
        
            # Update fish masks position
        fishmasks = []
        for fish in fishes:
            fishmask = pygame.mask.from_surface(changefishy)
            fishmaskrect = fishmask.get_rect()
            fishmaskrect.center = fish[1].center
            fishmasks.append((fish, fishmask, fishmaskrect)) 
                
        # Check for collision with fish
        for fish in fishmasks:
            if charactermaskrect.colliderect(fish[2]):
                score += 100
                fishes.remove(fish[0])
                    
       
        for iceblock in iceblocks:
            iceblockpos, blockrect = iceblock
            screen.blit(changeiceblock, iceblockpos)
            
        #monster collision
        #set up the new x and y position of mosnters as they are changing
        monster1maskrect.x = monster1posX
        monster1maskrect.y = monster1posY
        monster2maskrect.x = monster2posX
        monster2maskrect.y = monster2posY
        if charactermaskrect.colliderect(monster1maskrect) \
           or charactermaskrect.colliderect(monster2maskrect):
                dead()
                
        # Update igloo mask position and make sure after collision, character dont move
        if charactermaskrect.colliderect(igloomaskrect):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                rect.x += 20
            if keys[pygame.K_RIGHT]:
                rect.x -= 20
            if keys[pygame.K_UP]:
                rect.y += 20
            if keys[pygame.K_DOWN]:
                rect.y -= 20
            

        #if character got all fish points AND went back to igloo = level 2
        if charactermaskrect.colliderect(igloomaskrect) and len(fishes)==0:
            if charactermaskrect.right >= igloomaskrect.left \
               and charactermaskrect.right <= igloomaskrect.left + (igloomaskrect.width // 2):

                    level = 2
                    level2screen()
                
                    iglooPosX = 625
                    iglooPosY = 325
            
        ##showibg score incrementer
        if score >=0:
            drawtext("Score: {}".format(score), font, pink, 1300, 40)
        
        ##show fishes
        for fish in fishes:
            screen.blit(changefishy, fish[1])
        ## show igloo home  
        screen.blit(igloo2, (iglooPosX, iglooPosY))
        ##show character and monster
        screen.blit(changecharacter, rect)
        screen.blit(monsternew, (monster1posX, monster1posY))
        screen.blit(monster2new, (monster2posX, monster2posY))

        if gameState == "Dead":
            dead()
        drawtext("Time Left: {}s".format(countdown), font, color, 1300, 10)
        text = font.render("Level: {}".format(level), True, (0,0,0))
        screen.blit(text, (10, 10))
            

        pygame.display.update()
        clock.tick(80)

    pygame.quit()    



        
