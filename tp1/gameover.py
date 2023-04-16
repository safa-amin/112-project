def gameover():
    import pygame
    import math
    from menubuttons import startbuttons
    ##setting up the display
    pygame.init()
    ##original height and width
    width, height = 1500,800
    x = 1500
    #setting up clock
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Main Menu")
    #setting uo confetti moving background
    background = pygame.image.load("confetti.webp").convert()
    background = pygame.transform.scale(background,(width,height))
    bgWidth = background.get_width()
    run = True
    velocity = 30
    ##defining game variables
    scroll = 0
    tiles = math.ceil(x/bgWidth)+1
    # Set up fonts
    fontTitle = pygame.font.Font(None, 100)
    fontText = pygame.font.Font(None, 60)
    ## defining button colors
    black = (0,0,0)
    blue = (0,150,139)
    #color change when mouse on button
    buttonColor = (255,100,89)
    buttonHoverColor = (100,50,89)
    # Set up text
    titleText = fontTitle.render("You Won!!", True, black)
    ##defining button font and text
    buttonFont = pygame.font.Font(None, 35)
    textHome = buttonFont.render("Return To Home", True, (0,0,0))
    ##defining button sizes and positions
    buttonWidth, buttonHeight = 250, 150
    HomeButtonPos = (width/2 - buttonWidth/2, height - buttonHeight - 100)
    ##defining button rectangles
    HomeButtonRect = pygame.Rect(HomeButtonPos, (buttonWidth, buttonHeight))
    ##color
    while run == True:
        #to quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            ## draw buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ##checking if button is clicked
                if HomeButtonRect.collidepoint(event.pos):
                    #go to the menu buttons page
                    startbuttons()
                    break
        clock.tick(velocity)        
        ##draw the backround
        for i in range(0,tiles):
            #makes sure the background is scrolling
            screen.blit(background, (i*bgWidth + scroll,0))
        ## scrolling
            scroll -= 5
        ## resetting the scroll
            if abs(scroll)>bgWidth:
                scroll = 0
        # Draw buttons
        pygame.draw.rect(screen, blue, HomeButtonRect)
        # Check if mouse is over button and change color
        if HomeButtonRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, buttonHoverColor, HomeButtonRect)
        ##drawing button text
        screen.blit(textHome, (HomeButtonPos[0] + buttonWidth/2 - textHome.get_width()/2,
                               HomeButtonPos[1] + buttonHeight/2 - textHome.get_height()/2))
        #blitting the title of the button
        screen.blit(titleText, (width // 2 - titleText.get_width() // 2, 350))
        pygame.display.flip()


    pygame.quit()
                    
