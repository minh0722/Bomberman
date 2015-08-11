import os
import pygame
from pygame.sprite import Sprite
from pygame import Surface

# get path where current .py file is in
main_dir = os.path.split(os.path.abspath(__file__))[0]


def load_image(file):
    file = os.path.join(main_dir, 'resources', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s"' % (file))
    return surface


def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def encode(data):
    return data.encode('utf-8')

def decode(data):
    return data.decode('utf-8')

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
