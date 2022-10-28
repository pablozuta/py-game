#------------------------import modules------------------------------------

from turtle import pos
import pygame
from sys import exit

#------------------------------Event LooP------------------------------------
pygame.init()

#------------------------------metadatos------------------------------------

pantalla = pygame.display.set_mode((800, 400))
pygame.display.set_caption('High Tech - Low Life')
reloj = pygame.time.Clock()
typography = pygame.font.Font('font/Pixeltype.ttf', 60)


#------------------------------variables------------------------------------

skySurface = pygame.image.load('graphics/Sky.png').convert()
groundSurface = pygame.image.load('graphics/ground.png').convert()

scoreSurface = typography.render('Score', False, 'deeppink')
scoreRectangle = scoreSurface.get_rect(center= (400, 27))

snailSurface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snailRectangle = snailSurface.get_rect(bottomright= (600, 300))

protagonista = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
protagonistaRectangle = protagonista.get_rect(midbottom = (80, 300))
protagonistaGravity = 0

 
while True:

    #codigo para salir del juego si presionamos la x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            if protagonistaRectangle.collidepoint(event.pos):
                protagonistaGravity = -20    

        #funcion if para hacer saltar al protagonista con la tecla espacio
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                protagonistaGravity = -20    
              



    #------------------------background images and text------------------------------
    
    pantalla.blit(skySurface, (0, 0))
    pantalla.blit(groundSurface, (0, 300))

    pygame.draw.rect(pantalla, 'darkslategray', scoreRectangle)
    pygame.draw.rect(pantalla, 'darkslategray', scoreRectangle, 28)
    pantalla.blit(scoreSurface, scoreRectangle)

    #codigo para hacer que el caracol vuelva a aparecer por la derecha
    snailRectangle.right -=4
    if snailRectangle.right < 0:
        snailRectangle.left = 800
    pantalla.blit(snailSurface, snailRectangle)

    #implementacion salto
    protagonistaGravity += 1
    protagonistaRectangle.y += protagonistaGravity
    if protagonistaRectangle.bottom >= 300:protagonistaRectangle.bottom = 300
    pantalla.blit(protagonista, protagonistaRectangle)

    

    mousePos = pygame.mouse.get_pos() #con esto obtenemos la posicion del mouse

     

    pygame.display.update()
    reloj.tick(60)




