def startbuttons():
    from level1 import main
    from creditspage import showcredits
    import pygame
    import math
    #setting up pygame
    pygame.init()
    ##screen height and width
    width, height = 1500,800
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Main Menu")
    run = True
    #setting up background
    velocity = 30
    ## i got these images from google
    background = pygame.image.load("snowflakesbackground.gif").convert()
    background = pygame.transform.scale(background,(width,height))
    bgWidth = background.get_width()
    ##defining game variables
    scroll = 0
    tiles = math.ceil(width/bgWidth)+1

    ## defining button colors
    buttonColor = (255,178,102)
    buttonHoverColor = (182,219,255)

    ##defining button font and text
    buttonFont = pygame.font.Font(None, 35)
    textPlay = buttonFont.render("Play", True, (0,0,0))
    textCredits = buttonFont.render("Credits", True, (0,0,0))

    ##defining button sizes and positions
    buttonWidth, buttonHeight = 150, 50
    #play button
    PlayButtonPos = (width/2 - buttonWidth/2, height/2 - buttonHeight/2)
    #creditsbutton
    CreditsButtonPos = (width/2 - buttonWidth/2, height/2 - buttonHeight/2 + 100)

    ##defining button rectangles
    PlayButtonRect = pygame.Rect(PlayButtonPos, (buttonWidth, buttonHeight))
    CreditButtonRect = pygame.Rect(CreditsButtonPos, (buttonWidth, buttonHeight))

    while run:
        clock.tick(velocity)        
        ##draw the backround
        for i in range(0,tiles):
            screen.blit(background, (i*bgWidth + scroll,0))
        ## scrolling
            scroll -= 5
        ## resetting the scroll
            if abs(scroll)>bgWidth:
                scroll = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            ## draw buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:
            ##checking if button is clicked
                if PlayButtonRect.collidepoint(event.pos):
                        main()
                        print("Play button clicked")
                elif CreditButtonRect.collidepoint(event.pos):
                        showcredits()
                        print("Credits button clicked")
            
        # Drawing buttons
        pygame.draw.rect(screen, buttonColor, PlayButtonRect)
        pygame.draw.rect(screen, buttonColor, CreditButtonRect)
        
        # Check if mouse is over play button and change color
        if PlayButtonRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, buttonHoverColor, PlayButtonRect)
        # Check if mouse is over credit button and change color
        if CreditButtonRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, buttonHoverColor, CreditButtonRect)
            
        ##drawing button text
        screen.blit(textPlay, (PlayButtonPos[0] + 50, PlayButtonPos[1] + 10))
        screen.blit(textCredits, (CreditsButtonPos[0] + 30, CreditsButtonPos[1] + 10))
        
        pygame.display.update()


    pygame.quit()
