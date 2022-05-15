import pygame
from support import import_folder

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        self.frame_index = 0
        self.animation_speed = 0.5
