import pygame

pygame.init() #Refresh (required)

#set screen size

screen_width = 480 #width
screen_height = 640 #height
screen = pygame.display.set_mode((screen_width, screen_height))

#set screen title

pygame.display.set_caption("Sample Game") #game title

#set background image
backgorund = pygame.image.load("C:\\Users\\wshhw\\Documents\\VisualStudio Project\\Python\\Game Project\\PythonGame1\\PythonGame1\\pygame_basic\\background.png")

#check event

running = True
while running: 
    for event in pygame.event.get(): #check event for loop
        if event.type == pygame.QUIT: #check close screen event
            running = False #game is not running


    screen.blit(backgorund, (0,0)) #run background image

    pygame.display.update() #update run background image
# exit pygame
pygame.quit()
