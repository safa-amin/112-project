def level2screen():
    import pygame
    import sys
    from level2 import main2
    from menubuttons import startbuttons
    # Initialize pygame
    pygame.init()

    # Set up screen dimensions
    screen_width = 1500
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set up colors
    blue = (180,213,250)
    white = (255, 255, 255)
    normalButtonCol = white
    buttonColHover = (200, 200, 200)
    buttonColClicked = (100, 100, 100)

    # Set up fonts
    fontTitle = pygame.font.Font(None, 80)
    fontText = pygame.font.Font(None, 50)
    buttonText = pygame.font.Font(None, 25)

    # Set up text
    titleText = fontTitle.render("Level Complete!", True, white)
    scoreText = fontText.render("Score: 1800", True, white)

    # Set up buttons
    # Set up buttons
    continue_button_width = 200
    continue_button_height = 50
    continue_button_left = screen_width // 2 - continue_button_width // 2
    continue_button_top = screen_height // 2 - continue_button_height // 2
    continue_button = pygame.Rect(continue_button_left, continue_button_top, continue_button_width, continue_button_height)

    back_button_width = 200
    back_button_height = 50
    back_button_left = screen_width // 2 - back_button_width // 2
    back_button_top = continue_button_top + continue_button_height + 20
    back_button = pygame.Rect(back_button_left, back_button_top, back_button_width, back_button_height)


    # Set up button state variables
    continue_button_hovered = False
    continue_button_clicked = False
    back_button_hovered = False
    back_button_clicked = False

    # Run game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                continue_button_hovered = continue_button.collidepoint(mouse_x, mouse_y)
                back_button_hovered = back_button.collidepoint(mouse_x, mouse_y)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if continue_button.collidepoint(mouse_x, mouse_y):
                    continue_button_clicked = True
                elif back_button.collidepoint(mouse_x, mouse_y):
                    back_button_clicked = True
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                if continue_button_clicked and continue_button.collidepoint(mouse_x, mouse_y):
                    main2()
                    # Button clicked logic for continue button
                    continue_button_clicked = False
                elif back_button_clicked and back_button.collidepoint(mouse_x, mouse_y):
                    startbuttons()
                    # Button clicked logic for back button
                    back_button_clicked = False

        # Clear screen
        screen.fill(blue)

        # Draw title text
        screen.blit(titleText, (screen_width // 2 - titleText.get_width() // 2, 150))

        # Draw score text
        screen.blit(scoreText, (screen_width // 2- scoreText.get_width() // 2, 220))

        # Draw buttons
        if continue_button_hovered:
            continue_button_color = buttonColHover
        else:
            continue_button_color = normalButtonCol

        pygame.draw.rect(screen, continue_button_color, continue_button)

        if back_button_hovered:
            back_button_color = buttonColHover
        else:
            back_button_color = normalButtonCol

        pygame.draw.rect(screen, back_button_color, back_button)

        # Draw continue button label
        if not continue_button_clicked:
            continue_label_color = blue
        else:
            continue_label_color = buttonColClicked

        continue_label = buttonText.render("Continue to next level", True, continue_label_color)
        screen.blit(continue_label, (continue_button.left + 10, continue_button.top + 10))

        # Draw back button label
        if not back_button_clicked:
            back_label_color = blue
        else:
            back_label_color = buttonColClicked

        back_label = buttonText.render("Back to main menu", True, back_label_color)
        screen.blit(back_label, (back_button.left + 20, back_button.top + 10))


        # Update screen
        pygame.display.flip()
        
