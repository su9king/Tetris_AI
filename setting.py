import pygame

program_run = True

#SCREEN OPTION
def set_window(title,width,height):

    global screen

    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((width,height))

def get_event(event):

    global program_run

    for i in event:

        if i.type == pygame.QUIT:

            program_run = False

def set_board(board):

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



