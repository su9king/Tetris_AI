import pygame
import block_image

#SCREEN OPTION
def set_screen(title,width,height):

    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((width,height))

    pygame.image.load(block_image)