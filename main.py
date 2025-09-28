import pygame as pg
import random as rd

# Initialisation
pg.init()

# Definition des constantes
perso_x = 200
perso_y = 300
Taille = w, h = 500, 500
vitesse = 0.25
frame = 0

# on ajoute la taille du monde en géneral
world_width = 1000
world_height = 1000

# Creation de la fenetre
screen = pg.display.set_mode(Taille)


# creation des arbres
trees = pg.image.load('aalfa/tree_29.png')
tree = pg.transform.scale(trees, (50, 50))
# Creation du personnage
perso = [pg.image.load('sprite_perso-principal/alain0.png'),
         pg.image.load('sprite_perso-principal/alain1.png'),
         pg.image.load('sprite_perso-principal/alain2.png'),
         pg.image.load('sprite_perso-principal/alain3.png'),
         pg.image.load('sprite_perso-principal/alain4.png'),
         pg.image.load('sprite_perso-principal/alain5.png'),
         pg.image.load('sprite_perso-principal/alain6.png'),
         pg.image.load('sprite_perso-principal/alain7.png'),
         pg.image.load('sprite_perso-principal/alain8.png'),
         pg.image.load('sprite_perso-principal/alain9.png'),
         pg.image.load('sprite_perso-principal/alain10.png'),
         pg.image.load('sprite_perso-principal/alain11.png')
         ]
current_perso = perso[1]

# on crée une liste qui va contenir tous les arbres
forrest = []
tree_nbr = rd.randint(30, 50)

for i in range(tree_nbr):
    # On choisit la position de chaque arbre au hasard.
    pos = [rd.randint(0, 950), rd.randint(0, 950)]
    forrest.append(pos)

# Boucle principal
running = True
while running:

    # On calcuse l'offset du camera (au moitié de l'écran)
    camera_x = perso_x - 250
    camera_y = perso_y - 250

    # On limite le camera pour qu'il n'aille pas en dehors du monde
    camera_x = max(0, min(camera_x, world_width - 500))
    camera_y = max(0, min(camera_y, world_height - 500))

    # Pour que le joueur atteint le bord du monde
    player_screen_x = perso_x - camera_x
    player_screen_y = perso_y - camera_y
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Deplacement
    touch = pg.key.get_pressed()
    if touch[pg.K_LEFT]:
        current_perso = perso[3 + frame % 3]
        if player_screen_x >= 0:
            perso_x -= vitesse
            frame += 1
    if touch[pg.K_RIGHT]:
        current_perso = perso[6 + frame % 3]
        if player_screen_x <= 500 - 32:  # Car le point a traiter est le point
            # plus haut à gauche de l'image
            perso_x += vitesse
            frame += 1
    if touch[pg.K_DOWN]:
        current_perso = perso[0 + frame % 3]
        if player_screen_y <= 500 - 32:  # Car le point a traiter est le point
            # plus haut à gauche de l'image
            perso_y += vitesse
            frame += 1
    if touch[pg.K_UP]:
        current_perso = perso[9 + frame % 3]
        if player_screen_y >= 0:
            perso_y -= vitesse
            frame += 1

    screen.fill((110, 55, 0))
    for i in range(tree_nbr):
        screen.blit(tree, (forrest[i][0] - camera_x, forrest[i][1] - camera_y))
    screen.blit(current_perso, (player_screen_x, player_screen_y))

    pg.display.update()
    pg.display.flip()


pg.quit()
