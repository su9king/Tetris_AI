import pygame

def set_screen(title,width,height):

    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((width,height))