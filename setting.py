import pygame

program_run = True

# SETTING WINDOW NAME AND SIZE
def set_window(title,width,height):

    global screen

    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((width,height))

# WHEN USER GENERATE THE EVENT
def get_event(event):

    global program_run,mouse_click

    for e in event:

        if e.type == pygame.QUIT:

            program_run = False



# DRAWING OBJECT
def draw_screen(board):

    screen.blit(pygame.image.load("background.png"),(0,0))

    x = 0
    y = 0
    image = pygame.transform.scale(pygame.image.load("blue.png"),(32,32))

    for i in range(20):

        for j in range(10):

            if board[i][j] == 1:

                screen.blit(image,(x,y))

            x += 32


        x = 0

        y += 32

    pygame.display.update()



