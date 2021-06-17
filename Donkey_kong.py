import pygame
from Model import Constantes


class DonkeyKong:
    """Classe qui represente notre personnage"""

    def __init__(self):
        self.speed = 30
        self.image = pygame.image.load(Constantes.dk_droite)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def move_right(self):
        self.rect.x += self.speed
        self.image = pygame.image.load(Constantes.dk_droite)


    def move_left(self):
        self.rect = self.rect.move(-self.speed, 0)
        self.image = pygame.image.load(Constantes.dk_gauche)

    def move_up(self):
        self.rect = self.rect.move(0, -self.speed)
        self.image = pygame.image.load(Constantes.dk_haut)

    def move_down(self):
        self.rect = self.rect.move(0, self.speed)
        self.image = pygame.image.load(Constantes.dk_bas)

