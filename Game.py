import pygame
import random
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init() 

#Variables du jeu
maintain=True #Maintiens le jeu ouvert
scrolling=0 #A quel point le jeu défile, définit le score
speed=1

print("\nCeci est une version de developpement et ne dois \nen aucun cas etre consideree comme le produit final.\n")

#Affichage de la fenetre
window=pygame.display.set_mode((400,550))
info=pygame.display.Info()
pygame.display.set_caption("Corridor Jumper")

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
for i in range(0,2):
    try:
        print("Chargement de data/Player_"+str(i)+".png")
        player.append(pygame.image.load("data/Player_"+str(i)+".png"))
    except:
        print("Une erreur est survenue\nFermeture du programme...")
        sys.exit()
#       Obstacles
for i in range(0,3):
    try:
        print("Chargement de data/Obstacle_"+str(i)+".png")
        obstacle.append(pygame.image.load("data/Obstacle_"+str(i)+".png"))
    except:
        print("Une erreur est survenue\nFermeture du programme...")
        sys.exit()
try:
    pygame.mixer.music.load("data/Music.mp3")
    print("Chargement de data/Music.mp3")
except:
    print("Une erreur est survenue\nFermeture du programme...")
    sys.exit()

print("\nEn cours...\n")
print("Détails:")
print("Facteur vitesse: "+str(speed))

sprite_state=0
type_obstacle=[]
pos_obstacle=[]
offset_obstacle=[]
generated=False #La postition initiale des obstacle a elle ete generee?
player_pos=180 #Position du joueur sur l'axe x

pygame.mixer.music.play(-1,0.0) 

#Boucle du jeu
while maintain:
    
    scrolling=1*speed+scrolling #Fait défiler le fond
    speed=speed+0.001
    window.blit(background[0],(0,scrolling-9450)) #Fait afficher le fond

    if generated==False: #Genere la position initiale des obstacles
        for i in range(0,5):
            type_obstacle.append(random.randrange(0,3,1)) #Le type des obstacles (chaise? extincteur?)
            pos_obstacle.append(random.randrange(130,231,50)) #La position des obstacles (dans quelles colonnes sont ils?)
            offset_obstacle.append(random.randrange(scrolling-40,scrolling-1000,-40)) #Difficultés avec randrange, ne prend en charge que des ints
        generated=True
    for i in range(0,5): #Regarde si des obstacles sont hors du champs de vision
        if scrolling+offset_obstacle[i]>550:
            offset_obstacle[i]=offset_obstacle[i]+random.randrange(-600,-2000,-40)  #Affiche les obstacles supplémentaires
            pos_obstacle[i]=random.randrange(130,231,50)
    for i in range(0,5): #Affiche les obstacles
        window.blit(obstacle[type_obstacle[i]],(pos_obstacle[i],scrolling+offset_obstacle[i]))

    if sprite_state<50: #Joue l'animation du joueur (2 images)
        window.blit(player[0],(player_pos,500))
    else:
        window.blit(player[1],(player_pos,500))
    
    sprite_state=sprite_state+1

    if sprite_state>100:
        sprite_state=0
    
    for i in range(0,5): #Vérifie si le joueur marche sur un obstacle et arrette l'app si c'est le cas
        if player_pos==pos_obstacle[i] and scrolling+offset_obstacle[i]<=462 and scrolling+offset_obstacle[i]>=459:
            maintain=False
    
    if scrolling/100>100: #Vérifie qu'on est pas à la fin du niveau
        print("Gagne!")
        maintain=False
    
    pygame.display.flip() #Met à jour la vue

    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key==K_RIGHT: #Traite la flèche DROITE
            if player_pos==230: #Restriction des mouvements
                print("Deplacement a droite impossible.")
            else:
                player_pos=player_pos+50
        if event.type==KEYDOWN and event.key==K_LEFT: #Traite la flèche GAUCHE
            if player_pos==130: #Restriction des mouvements
                print("Deplacement a gauche impossible.")
            else:
                player_pos=player_pos-50
        if event.type==QUIT: #Traite la fin du programme
            maintain=False
    
    pygame.display.set_caption("Corridor Jumper - "+str(int(scrolling/100))+"%")

print("\nNiveau completé à "+str(int(scrolling/100)) +"%")

print("\nArret...")
sys.exit() 
