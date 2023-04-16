def dead():
    import pygame
    import sys
    from creditspage import showcredits
    from menubuttons import startbuttons
    # Initialize pygame
    pygame.init()

    # Set up screen dimensions
    screen_width = 1500
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set up colors
    blue = (0,0,139)
    black = (255,255, 255)
    normalButtonCol = black
    buttonColHover = (200, 200, 200)
    buttonColClicked = (100, 100, 100)

    # Set up fonts
    fontTitle = pygame.font.Font(None, 100)
    fontText = pygame.font.Font(None, 60)
    buttonText = pygame.font.Font(None, 25)

    # Set up text
    titleText = fontTitle.render("GAME OVER", True, black)
    scoreText = fontText.render("Better Luck Next Time", True, black)

    # Set up buttons
    # Set up buttons
    retry_button_width = 200
    retry_button_height = 50
    retry_button_left = screen_width // 2 - retry_button_width // 2
    retry_button_top = screen_height // 2 - retry_button_height // 2
    retry_button = pygame.Rect(retry_button_left, retry_button_top, retry_button_width, retry_button_height)

    back_button_width = 200
    back_button_height = 50
    back_button_left = screen_width // 2 - back_button_width // 2
    back_button_top = retry_button_top + retry_button_height + 20
    back_button = pygame.Rect(back_button_left, back_button_top, back_button_width, back_button_height)


    # Set up button state variables
    retry_button_hovered = False
    retry_button_clicked = False
    back_button_hovered = False
    back_button_clicked = False

    # Run game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #mouse events to check if hovering over buttons   
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                retry_button_hovered = retry_button.collidepoint(mouse_x, mouse_y)
                back_button_hovered = back_button.collidepoint(mouse_x, mouse_y)
             #if the mouses collide with button change boolean   
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if retry_button.collidepoint(mouse_x, mouse_y):
                    retry_button_clicked = True
                elif back_button.collidepoint(mouse_x, mouse_y):
                    back_button_clicked = True
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                #if the button is clicked bc boolean is true and mouse x y point collide w button
                if retry_button_clicked and retry_button.collidepoint(mouse_x, mouse_y):
                    #credit screen
                    showcredits()
                    print("retry button clicked")
                    # Button clicked logic for continue button
                    retry_button_clicked = False
                elif back_button_clicked and back_button.collidepoint(mouse_x, mouse_y):
                    #menu screen
                    startbuttons()
                    print("back button clicked")
                    # Button clicked logic for back button
                    back_button_clicked = False

        # Clear screen
        screen.fill(blue)
        # Draw title text
        screen.blit(titleText, (screen_width // 2 - titleText.get_width() // 2, 150))
        # Draw score text
        screen.blit(scoreText, (screen_width // 2- scoreText.get_width() // 2, 280))
        # Draw buttons
        if retry_button_hovered:
            retry_button_color = buttonColHover
        else:
            retry_button_color = normalButtonCol

        pygame.draw.rect(screen, retry_button_color, retry_button)

        if back_button_hovered:
            back_button_color = buttonColHover
        else:
            back_button_color = normalButtonCol

        pygame.draw.rect(screen, back_button_color, back_button)

        # Draw continue button label
        if not retry_button_clicked:
            retry_label_color = blue
        else:
            retry_label_color = buttonColClicked
        continue_label = buttonText.render("Credits", True, retry_label_color)
        screen.blit(continue_label, (retry_button.left + 10, retry_button.top + 10))
        # Draw back button label
        if not back_button_clicked:
            back_label_color = blue
        else:
            back_label_color = buttonColClicked

        back_label = buttonText.render("Back to main menu", True, back_label_color)
        screen.blit(back_label, (back_button.left + 20, back_button.top + 10))


        # Update screen
        pygame.display.flip()
