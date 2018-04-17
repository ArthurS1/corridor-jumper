import pygame
import sys
from pygame.locals import *

#Variables du jeu
maintain=True #Maintiens le jeu ouvert
scrolling=0 #A quel point le jeu défile, définit le score
speed_cte=0.1
score=0

print("\nCeci est une version de developpement et ne dois \nen aucun cas etre consideree comme le produit final.\n")

#Affichage de la fenetre
window=pygame.display.set_mode((400,550))
info=pygame.display.Info()

#Chargements
#   Variables dans lesquelles on stock les images
background=[]
player=[]

#   Boucles ou on stock les images dans les variables précédentes
#       Backgrounds
for i in range(0,1):
    try:
        print("Chargement de data/Back_"+str(i)+".png")
        background.append(pygame.image.load("data/Back_"+str(i)+".png"))
    except:
        print("Une erreur est survenue\nFermeture du programme...")
        sys.exit()
#       Player
for i in range(0,1):
    try:
        print("Chargement de data/Player_"+str(i)+".png")
        player.append(pygame.image.load("data/Player_"+str(i)+".png"))
    except:
        print("Une erreur est survenue\nFermeture du programme...")
        sys.exit()

#Fait defiler une tile
def Background(tile_scroll,back_number,reset_pos):
    window.blit(background[back_number],(0,tile_scroll))
    if tile_scroll>550:
        return True

print("\nEn cours...")

tile_scroll_1=150
tile_scroll_2=-250
tile_scroll_3=-650

#Boucle du jeu
while maintain:
    scrolling=scrolling+speed_cte #Changer la vitesse de défilement ici
    tile_scroll_1=tile_scroll_1+speed_cte
    tile_scroll_2=tile_scroll_2+speed_cte
    tile_scroll_3=tile_scroll_3+speed_cte
    if Background(tile_scroll_1,0)==True:# Si il arrive en bas et est devenu invisible
        tile_scroll_1=-250
    if Background(tile_scroll_2,0)==True:# Si il arrive en bas et est devenu invisible
        tile_scroll_2=-250
    if Background(tile_scroll_3,0)==True:# Si il arrive en bas et est devenu invisible
        tile_scroll_2=-250
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT: #Traite la fin du programme
            maintain=False

print("\nArret...")
sys.exit()
