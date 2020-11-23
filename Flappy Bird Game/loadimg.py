


import pygame 
import os


def loadimg(image):
    return pygame.transform.scale2x(pygame.image.load(os.path.join("imgs",image)))