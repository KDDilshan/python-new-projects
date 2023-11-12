import pygame
from pygame.locals import *

pygame.init()
SCREEN_WIDTH=400
SCREEN_HEIGHT=400
window=pygame.display.set_mode([SCREEN_HEIGHT,SCREEN_WIDTH])
running=True
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
           running=False
        # #    did user hit a key
        # if event.type==pygame.KEYDOWN:
        #     # was it right key of enter
        #     if event.key== K_KP_ENTER:
        #         running=False
            
    window.fill((0,255,255))
    pygame.draw.circle(window,(255,255,0),(200,200),50)
    surface=pygame.Surface((50,50))
    surface.fill((0,0,0))
    rect=surface.get_rect()
    # position correction to center
    surface_center=((SCREEN_WIDTH-surface.get_width())/2,(SCREEN_HEIGHT-surface.get_height())/2)
    window.blit(surface,surface_center)
    # for displaing all the things
    pygame.display.flip()

pygame.quit()

        
        
