def showcredits():
    import pygame
    #setting the basics
    pygame.init()
    screen = pygame.display.set_mode([1500,800])
    blue = (180,213,255)
    pink = (48,52,168)
    #getting the center x and y coordinates of the screen
    centerx = screen.get_rect().centerx
    centery = screen.get_rect().centery
    #delta y is the change
    changeY = centery + 40
    #credits that will be shown
    creditsText = ''' Programmer - Safa Amin
    Art/ Graphics - Google
    Audio - YouTube
    Thank you for playing Bear Escape!
    '''
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #decreasing delta y        
        changeY -= 3
        messageList = []
        positionList = []
        #i is initially 0
        i = 0
        screen.fill(blue)
        font = pygame.font.SysFont("Arial",30)
        #removing the new line for each line in credits text
        for line in creditsText.split("\n"):
            #putting font color 
            message = font.render(line, True, pink)
            messageList.append(message)
            #positioning text in center of screen
            pos = message.get_rect(center=(centerx, centery+changeY + i*30))
            positionList.append(pos)
            #i is total line count
            i+= 1
        if centery + changeY+30*(len(creditsText.split("\n"))) < 0:
            run = False
            
        for j in range(i):
            screen.blit(messageList[j], positionList[j])
            
        pygame.display.update()
        
    pygame.quit()
