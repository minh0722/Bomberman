import os
import pygame
from pygame.sprite import Sprite
from pygame import Surface

#get path where current .py file is in
main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    file = os.path.join(main_dir, 'resources', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface
  
def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


class Drawable:
    def __init__(self):
        pass

    def draw(self, sprite):
        pass


class dummysound:
    def play(self):
        pass

def load_sound(file):
    if not pygame.mixer: 
    	return dummysound()

    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()