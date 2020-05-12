import pygame

pygame.init() #Refresh (required)

#set screen size

screen_width = 480 #width
screen_height = 640 #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title
pygame.display.set_caption("Sample Game") #game title

#FPS
clock = pygame.time.Clock()


#set background image
background = pygame.image.load("C:\\Users\\wshhw\\Documents\\VisualStudio Project\\Python\\Game Project\\PythonGame1\\PythonGame1\\pygame_basic\\background.png")

#set character 
character = pygame.image.load("C:\\Users\\wshhw\\Documents\\VisualStudio Project\\Python\\Game Project\\PythonGame1\\PythonGame1\\pygame_basic\\character.png")
character_size = character.get_rect().size #call image size
character_width = character_size[0] 
character_height = character_size[1]

character_x_pos = (screen_width/2)-(character_width/2) #half position of screen
character_y_pos = screen_height-character_height #max position of screen (lowest position)

#location to move
to_x = 0 
to_y = 0

#speed character
character_speed = 0.8

#check event
running = True
while running: 
    dt = clock.tick(60) # set 30 FPS
    #print("fps : " +str(clock.get_fps()))

    for event in pygame.event.get(): #check event for loop
        if event.type == pygame.QUIT: #check close screen event
            running = False #game is not running
        if event.type == pygame.KEYDOWN: #check status KEYDOWN
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key ==pygame.K_RIGHT:
                to_x += character_speed
            elif event.key ==pygame.K_UP:
                to_y -= character_speed
            elif event.key ==pygame.K_DOWN:
                to_y += character_speed
            #elif event.key == pygame.K_1:
            #    print('this work!!')
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos +=  to_x *dt
    character_y_pos +=  to_y *dt

    #set max position (prevent out of screen)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width:
        character_x_pos = screen_width - character_width
    if character_y_pos <0 :
        character_y_pos = 0
    elif character_y_pos > screen_height:
        character_y_pos = screen_height - character_height
    



    screen.blit(background, (0,0)) #run background image
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #update run background image

# exit pygame
pygame.quit()
