import pygame
import sys
import random
from pygame.locals import *

#Variables du jeu
maintain=True #Maintiens le jeu ouvert
scrolling=0 #A quel point le jeu défile, définit le score
speed=1

print("\nCeci est une version de developpement et ne dois \nen aucun cas etre consideree comme le produit final.\n")

#Affichage de la fenetre
window=pygame.display.set_mode((400,550))
info=pygame.display.Info()

#Chargements
#   Variables dans lesquelles on stock les images
background=[]
player=[]
obstacle=[]
   
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
#       Obstacles
for i in range(0,1):
    try:
        print("Chargement de data/Obstacle_"+str(i)+".png")
        obstacle.append(pygame.image.load("data/Obstacle_"+str(i)+".png"))
    except:
        print("Une erreur est survenue\nFermeture du programme...")
        sys.exit()

print("\nEn cours...\n")
print("Détails:")
print("Facteur vitesse: "+str(speed))

pos_obstacle=[]
offset_obstacle=[]
generated=False #La postition initiale des obstacle a elle ete generee?
player_pos=180 #Position du joueur sur l'axe x
#Boucle du jeu
while maintain:

    scrolling=scrolling+speed #Fait défiler le fond
    window.blit(background[0],(0,scrolling-9450)) #Fait afficher le fond

    if generated==False:    #Genere la position initiale des obstacles
        for i in range(0,5):
            pos_obstacle.append(random.randrange(130, 231, 50))
            offset_obstacle.append(random.randrange(scrolling-40,scrolling-1000,-40))
        generated=True
    for i in range(0,5): #Regarde si des obstacles sont hors du champs de vision
        if scrolling+offset_obstacle[i]>550:
            offset_obstacle[i]=offset_obstacle[i]+random.randrange(-600,-2000,-40)  #Affiche les obstacles supplémentaires
            pos_obstacle[i]=random.randrange(130, 231, 50)
    for i in range(0,5): #Affiche les obstacles
        window.blit(obstacle[0],(pos_obstacle[i],scrolling+offset_obstacle[i]))

    window.blit(player[0],(player_pos,500)) #Affiche le joueur

    pygame.display.flip() #Met à jour la vue

    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key==K_RIGHT: #Traite la flèche DROITE
            if player_pos==230: #Restriction des mouvements
                print("Deplacement a droite impossible.")
            else:
                player_pos=player_pos+50
        if event.type==KEYDOWN and event.key==K_LEFT: #Traite la flèche GAUCHE
            if player_pos==130: #Restriction des moucements
                print("Deplacement a gauche impossible.")
            else:
                player_pos=player_pos-50
        if event.type==QUIT: #Traite la fin du programme
            maintain=False

print("\nNiveau completé à "+str(int(scrolling/100)) +"%")

print("\nArret...")
sys.exit() 

