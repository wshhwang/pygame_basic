import pygame

pygame.init() #Refresh (required)

#set screen size

screen_width = 480 #width
screen_height = 640 #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title

pygame.display.set_caption("Sample Game") #game title

#set background image
background = pygame.image.load("C:\\Users\\wshhw\\Documents\\VisualStudio Project\\Python\\Game Project\\PythonGame1\\PythonGame1\\pygame_basic\\background.png")

#set character 
character = pygame.image.load("C:\\Users\\wshhw\\Documents\\VisualStudio Project\\Python\\Game Project\\PythonGame1\\PythonGame1\\pygame_basic\\character.png")
character_size = character.get_rect().size #call image size
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2) #half position of screen
character_y_pos = screen_height-70 #max position of screen (lowest position)

#check event
running = True
while running: 
    for event in pygame.event.get(): #check event for loop
        if event.type == pygame.QUIT: #check close screen event
            running = False #game is not running


    screen.blit(background, (0,0)) #run background image
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() #update run background image

# exit pygame
pygame.quit()
