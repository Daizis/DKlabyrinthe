"""Code de base"""
import pygame
from Model import Constantes
from Model.Donkey_kong import DonkeyKong
from Model.Mur import Mur

# Initialisation
pygame.init()

# Creation fenetre
screen = pygame.display.set_mode(Constantes.taille_screen)

# Creation de la page du choix de niveau
lvl = pygame.image.load(Constantes.lvl)

pygame.display.set_caption("DKlabyrinthe")
# Charger le fond
background = pygame.image.load(Constantes.fond)

winner = pygame.image.load(Constantes.winner).convert_alpha()

# On charge les classe joueur et mur (FAIRE UNE CLASSE GAME)
player = DonkeyKong()
mur = Mur()

# Boucle du jeu
marche = True
choice = True
running = True
carte = ""

while marche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            marche = False
            pygame.quit()

    while choice:
        screen.blit(lvl, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                marche = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    carte = "dklabyrinthe_assets/DK_niveau1.txt"
                    Constantes.func(carte)
                    choice = False

                elif event.key == pygame.K_2:
                    carte = "dklabyrinthe_assets/DK_niveau2.txt"
                    choice = False

    while running:

        # Afficihage du fonds dans la fentre
        screen.blit(background, (0, 0))

        # Affichage des murs, du départ et de la banane (arrivée)
        mur.construire(screen)

        # Affichage du joueur
        screen.blit(player.image, player.rect)

        # Rafraichissement du jeu
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                marche = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and [player.rect[0] + player.speed, player.rect[1]] not in Constantes.liste:
                    # on transforme player.rect en liste en ajoutant ou en enlevant le speed à x ou y et on regarde si notre liste est contenu dans Constantes.liste
                    player.move_right()

                    if player.rect[:2] == Constantes.indice_banana:
                        screen.blit(background, (0, 0))
                        screen.blit(winner, (112, 112))
                        pygame.display.flip()
                        running = False


                elif event.key == pygame.K_LEFT and [player.rect[0] - player.speed, player.rect[1]] not in Constantes.liste:
                    player.move_left()

                elif event.key == pygame.K_UP and [player.rect[0], player.rect[1] - player.speed] not in Constantes.liste:
                    player.move_up()

                elif event.key == pygame.K_DOWN and [player.rect[0], player.rect[1] + player.speed] not in Constantes.liste:
                    player.move_down()



