import pygame
import sys
from pygame.locals import *
nombre_assets=3
print("\nCeci est une version de developpement et ne dois \nen aucun cas etre consideree comme le produit final.\n")

#Affichage de la fenetre
window=pygame.display.set_mode((400,550))
info=pygame.display.Info()

#Chargements
background=[]
for i in range(0,nombre_assets):
    try:
        print("Chargement de data/Back_"+str(i)+".png")
        background.append(pygame.image.load("data/Back_"+str(i)+".png"))
    except:
        print("Une erreur est survenue lors de la tentative de chargement de la ressource")
        print("Fermeture du programme...")
        sys.exit()

#Fait defiler le fond
def Background(scroll_speed,scrolling):
    scrolling=scrolling+1*scroll_speed
    window.blit(background[0],(0,scrolling))
    window.blit(background[0],(0,scrolling-400))
    if scrolling>400:
        scrolling=0
    return scrolling

print("\nEn cours...")

#%
maintain=True
scrolling=0
window.blit(background[1],(0,scrolling+400)) #tile pre scroll
while maintain:
    scrolling=Background(3,scrolling)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==QUIT or event.type==KEYDOWN:
            maintain=False

print("\nArret...")
sys.exit()
