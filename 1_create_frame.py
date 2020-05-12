import pygame

pygame.init() #Refresh (required)

#set screen size

screen_width = 480 #width
screen_height = 640 #height
pygame.display.set_mode((screen_width, screen_height))

#set screen title

pygame.display.set_caption("Sample Game") #game title

#check event

running = True
while running: 
    for event in pygame.event.get(): #check event for loop
        if event.type == pygame.QUIT: #check close screen event
            running = False #game is not running

# exit pygame

pygame.quit()
