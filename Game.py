import pygame
import sys
from pygame.locals import *

print("\nCeci est une version de developpement et ne dois \nen aucun cas être considéré comme le produit final.\n")

#Affichage de la fenêtre
window=pygame.display.set_mode((400,550))
info=pygame.display.Info()

#Chargements
background=[]
for i in range(0,1):
    try:
        print("Chargement de data/Back_"+str(i)+".png")
        background.append(pygame.image.load("data/Back_"+str(i)+".png"))
    except:
        print("Une erreur est survenue lors de la tentative de chargement de la ressource")
        print("Fermeture du programme...")
        sys.exit()

#%
maintain=True
scrolling=0
scroll_speed=3
while maintain:
    scrolling=scrolling+1*scroll_speed
    window.blit(background[0],(0,scrolling))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==QUIT or event.type==KEYDOWN:
            maintain=False
