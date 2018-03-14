import pygame
import sys
from pygame.locals import *

#Affichage de la fenêtre
window=pygame.display.set_mode((400,800))
global_info=pygame.display.Info()


#Chargements
layer=[]
try:
    for i in range(0,2):
        layer.append(pygame.image.load("assets/menu/Layer"+str(i)+".png"))
    print("Layers Chargées avec succès")
except:
    print("Fichiers de layer.s manquant.s");sys.exit()
#Fonction de super-résolution
def SuperResolution(PoX=0,PoY=0):
    info=pygame.display.Info()
    PoY=PoY/-1
    PoX=int(info.current_w/2+PoX)
    PoY=int(info.current_h/2+PoY)
    return (PoX,PoY)

#menu_layer_0=pygame.transform.scale(menu_layer_0, (global_info.current_w, global_info.current_h))
#menu_layer_1=pygame.transform.scale(menu_layer_1, (global_info.current_w, global_info.current_h))
#menu_layer_2=pygame.transform.scale(menu_layer_2, (global_info.current_w, global_info.current_h))

#Affichage du menu
maintain=True
while maintain:
    w##ndow.blit(lmenu_layer_0SuperResolution(-global_info.current_w/2,global_info.current_h/2))
    #w#ndow.blit(menu_layer_1,SuperResolution(-global_info.current_w/2,global_info.current_h/2))
    #w#ndow.blit(menu_layer_2,SuperResolution(-global_info.current_w/2,global_info.current_h/2))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==QUIT or event.type==KEYDOWN:
            maintain=False
