def main2():
    import pygame, sys
    import math
    from death import dead
    from gameover import gameover
    from menubuttons import startbuttons
    ##setting up the display
    pygame.init()
    width, height = 1500,800
    clock = pygame.time.Clock()
    # Set up game state and countdown
    gameState = "Playing"
    countdown = 60
    frame_counter = 0
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Main Menu")
    x = 1500
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
    changeiceblock = pygame.transform.scale(iceblock, (70,70))
    #rectangles around obstacles
    blockrect = changeiceblock.get_rect()

    #setting home for character
    igloo2 = pygame.image.load('igloo2 copy.png')
    igloo2 = pygame.transform.scale(igloo2, (125,125))
    igloorect = igloo2.get_rect()

    ##setting the enemies to move on their own
    monster1width = 100
    monster1height = 100

    #setting up monster1
    monster = pygame.image.load("monster3.png").convert_alpha()
    monsternew = pygame.transform.scale(monster, (monster1width,monster1height))
    monster1rect = monster.get_rect()

    ##initial position of monster1
    monster1posX = width//2
    monster1posY = height//1.4
    monster1speed = 50
    monster1Direction = 1

    ##setting up monster 2
    monster2 = pygame.image.load("wintermonster.png").convert_alpha()
    monster2new = pygame.transform.scale(monster2, (monster1width,monster1height))
    monster2rect = monster2.get_rect()

    #initial position of monster2
    monster2posX = width - 1000
    monster2posY = height-400


    ##initial position of igloo
    iglooPosX = 660
    iglooPosY = 100

    level = 2
    ##establishin font function
    def drawtext(string, font, textcolor,x, y):
        image = font.render(string, True, textcolor)
        screen.blit(image, (x,y))    
    font = pygame.font.SysFont("arialblack", 20)
    ##color of font
    textcolor = (255,50,200)
    color = (118,56,98)
    BLUE = (180,213,255)
    ##defining block list
    change = 0
    tiles = math.ceil(x/bgWidth)+1
    # Define the initial starting positions and spacing between ice blocks for each set of ice blocks
    start_x_list = [100, 1000, 550]  # Example list of different start x positions
    start_y_list = [40, 800, 1000]         # Example list of different start y positions
    spacing_x = 50
    spacing_y = 50

    # Define the number of rows and columns for the L shape
    num_rows = 9
    num_cols = 7

    # Generate positions list for each set of ice blocks
    positions = []
    for start_x in start_x_list:
        for start_y in start_y_list:
            for row in range(num_rows):
                for col in range(num_cols):
                    # Add positions for the top horizontal row
                    if row == 0:
                        positions.append((start_x + col * spacing_x, start_y))
                    # Add positions for the vertical column on the left side
                    elif col == 0:
                        positions.append((start_x, start_y + row * spacing_y))
                    # Add positions for the vertical column on the right side
                    elif col == num_cols - 1:
                        positions.append((start_x + col * spacing_x, start_y + row * spacing_y))

    # Remove duplicates and sort the positions list
    positions = list(set(positions))
    positions.sort()
    iceblocks = []
    for position in positions:
        # Setting rectangle for each ice block
        blockrect = pygame.Rect(position[0], position[1], 50, 50)
        iceblocks.append((position, blockrect))
    ## fishy list
    # Define the x and y ranges for generating fishies for each set of fishies
    x_range_list = [200, 1100]  # Example list of different x ranges for fishies
    y_range_list = [125, 800, 1000]  # Example list of different y ranges for fishies

    # Generate fishies using nested loops for each set of fishies
    fishies = [(650,300), (750,300), (650,400), (750,400), ]
    for x_range in x_range_list:
        for y_range in y_range_list:
            for x in range(x_range, x_range + 200, 100):  # Change the step value as needed for desired spacing
                for y in range(y_range, y_range + 400, 100):  # Change the step value as needed for desired spacing
                    fishies.append((x, y))

            
    fishes = []
    for fish in fishies:
        # setting rectangle for each fish
        fishrect = pygame.Rect(fish[0], fish[1], 80, 80)
        fishes.append((fish, fishrect))   
    ##intitiate character movement with arrow keys
    rect = pygame.Rect(1200, 700, 50, 50)  # Update the starting position of the character's rectangle here
    start_time = pygame.time.get_ticks()
    while run:
        #quitgame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                 startbuttons()
                
        if gameState == "Playing":
            frame_counter += 1
            if frame_counter % 20 == 0:
                countdown -= 1
                if countdown == 0:
                    gameState = "Dead"        # Update character's position
        
        clock.tick(velocity)
        #only do character movment if no collision is detected
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect.x -= 20
            if rect.left < 0:
                rect.left = 0
            
        if keys[pygame.K_RIGHT]:
            rect.x+= 20
            if rect.right > width:
                rect.right = width
            
        if keys[pygame.K_UP]:
            rect.y -= 20
            if rect.top < 0:
                rect.top = 0
                    
        if keys[pygame.K_DOWN]:
            rect.y += 20
            if rect.bottom > height:
                rect.bottom = height - rect.height  # Set the y-coordinate to the height of the screen minus the height of the character
        
            
        
        for block in iceblocks:
            if rect.colliderect(block[1]):
                # stop character movement
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
        monster1posX += monster1speed * monster1Direction/3
        monster2posX += monster1speed * monster1Direction/3


        ## make monster1 go left and right        
        if monster1posX + monster1width > width:
            monster1speed += 1.4
            monster1Direction = -1
            monster1posX = width - monster1width
        elif monster1posX < 0:
            monster1speed += 1.4
            monster1Direction = 1
            monster1posX = 400
        monster1rect.topleft = (monster1posX, monster1posY)

    ## make monster2 go left and right        
        if monster2posX + monster1width > width:
            monster2Direction = -1 # update to monster2Direction
            monster2posX = width - 300
        elif monster2posX < 0:
            monster2Direction = 1 # update to monster2Direction
            monster2posX = 0
            
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
        monster1maskrect.y = monster1posY
        monster2maskrect.x = monster2posX
        monster2maskrect.y = monster2posY
        if charactermaskrect.colliderect(monster1maskrect) \
           or charactermaskrect.colliderect(monster2maskrect) :
                dead()
        
        # Update igloo mask position

        if charactermaskrect.colliderect(igloomaskrect):
            print("igloo colllision")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                rect.x += 20
            if keys[pygame.K_RIGHT]:
                rect.x -= 20
            if keys[pygame.K_UP]:
                rect.y += 20
            if keys[pygame.K_DOWN]:
                rect.y -= 20
                
        if charactermaskrect.colliderect(igloomaskrect) and score==2000:
            if charactermaskrect.right >= igloomaskrect.left \
               and charactermaskrect.right <= igloomaskrect.left + (igloomaskrect.width // 2):
                
                    gameover()
                    iglooPosX = 650
                    iglooPosY = 200
            
        ##showibg score incrementer
        if score >=0:
            drawtext("Score: {}".format(score), font, textcolor, 1120, 10)
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


