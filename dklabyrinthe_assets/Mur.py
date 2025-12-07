"""Mettre les murs, le départ, et la banane"""
import pygame
from Model import Constantes
from Model.Donkey_kong import DonkeyKong

class Mur:
    def __init__(self):
        self.player = DonkeyKong()
        self.carte = Constantes.lst
        self.image = pygame.image.load(Constantes.mur)
        self.image_banane = pygame.image.load(Constantes.banane)
        self.image_depart = pygame.image.load(Constantes.depart)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.indices_rect = [i for i in self.rect]



    def construire(self, screen):
        for ligne in self.carte:
            x = ligne # dans cette variable on récupere chaque ligne ( 1ere iteration on recupere la 1ere ligne,
            # 2eme iteration on récupere la 2ème ligne ...)

            indices = [i for i, ele in enumerate(x) if ele == "m"]  # alors on récupere tous les l'indices de "m"

            for i in indices: # on parcours les indices
                self.rect.x = i * 30 # on fait l'indice de "m" * la taille du sprite pour la pos en x
                self.rect.y = self.carte.index(x) * 30 # on fait l'indice de la ligne * la taille du sprite pour la pos en y
                screen.blit(self.image, (self.rect.x, self.rect.y))

            if "a" in x: # si ya un "a" dans la ligne x = indice du "a" et y = indice de la ligne où est le "a"
                pos_x = x.index("a") * 30
                pos_y = self.carte.index(x) * 30
                screen.blit(self.image_banane, (pos_x, pos_y))

            if "d" in x: # si ya un "d" dans la ligne x = indice du "d" et y = indice de la ligne où est le "d"
                pos_x = x.index("d") * 30
                pos_y = self.carte.index(x) * 30
                screen.blit(self.image_depart, (pos_x, pos_y))
