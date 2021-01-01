import pygame

program_run = True

#SCREEN OPTION
def set_window(title,width,height):

    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((width,height))

def get_event(event):

    global program_run

    for i in event:

        if i.type == pygame.QUIT:

            program_run = False



