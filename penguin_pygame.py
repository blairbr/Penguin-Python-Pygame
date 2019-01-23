import pygame

pygame.init()    #intialize pygame - must do this for the program to start properly

#declare the width and height of the screen
width = 1500
height = 1500
 
#make the pygame window
screen = pygame.display.set_mode((width, height))

#here you can import an image - make sure it's in the same folder as this .py file or it won't work
penguinImage = pygame.image.load("penguin.png").convert()

# the coordinates on the screen (x and y)
x = 250
y = 250
screen.blit(penguinImage, ( x,y)) # paint to screen
pygame.display.update() #updates the screen (you need to do this for your image to show up)
game_running = True

#initialize the change in x coordinates for when your image moves
x_change = 0

while game_running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    print("Image should move right")
            #reset the x_change to zero if the user releases the left or right key (so the image doesn't move continuously)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    print("resetting x_change to zero")
                    x_change = 0
            #makes it so the program closes when the user clicks the X in the top right corner of the screen
            if event.type == pygame.QUIT:
                game_running = False
        
        #here x is reset to a new value, which updates the coordinates and causes it the image to move left and right
        x = x_change + x

        screen.blit(penguinImage, ( x,y)) #update the screen with the new coordinates of the image

        pygame.display.update()  #update the display
