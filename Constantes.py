
# Arriere pan du jeu
fond = "dklabyrinthe_assets/fond.jpg"

# taille de la fenetre
taille_screen = (450, 450)

# icon
icon = "dklabyrinthe_assets/dk_droite.png" # convertir en ico ?

# depart
depart = "dklabyrinthe_assets/depart.png"

# position vers la droite
dk_droite = "dklabyrinthe_assets/dk_droite.png"

# position vers la gauche
dk_gauche = "dklabyrinthe_assets/dk_gauche.png"

# position vers le haut
dk_haut = "dklabyrinthe_assets/dk_haut.png"

# position vers le bas
dk_bas = "dklabyrinthe_assets/dk_bas.png"

# mur
mur = "dklabyrinthe_assets/mur.png"

# banane
banane = "dklabyrinthe_assets/arrivee.png"


# On ouvre la carte du labyrinthe
file = open("dklabyrinthe_assets/DK_niveau1.txt", "r") # on ouvre en lecture
lst = []
liste_carte = file.read().split("\n") # on lit le fichier et on le split au niveau de "\n""
for i in liste_carte:
    # on parcourt la liste en transformant chaque éléments en une liste et on l'ajoute à la liste vide
    lst.append(list(i))


# récupere les indices de chaque murs et de la banane

liste = [] # liste qui contiendra tout les rect de chaque murs
banana = "" # x de l'arrivée
bananaa = "" #  y de l'arrivée
for ligne in lst:
    ligne = ligne # dans cette variable on récupere chaque ligne ( 1ere iteration on recupere la 1ere ligne,

    indices = [i for i, ele in enumerate(ligne) if ele == "m"]  # alors on récupere tous les l'indices de "m"

    for i in indices:  # on parcours les indices
        liste.append([i * 30, lst.index(ligne) * 30]) # On fait une liste qui contient des listes avec le rect de chaque mur (x, y)

    if "a" in ligne:
        bananaa = lst.index(ligne) * 30
        banana = [i* 30 for i, ele in enumerate(ligne) if ele == "a"]


indice_banana = banana
indice_banana.append(bananaa) # rect de la banane
