import pygame
pygame.init()
ecran = pygame.display.set_mode((10, 10))

background = pygame.image.load("background.png").convert()
background_rect=background.get_rect()
largeur_fond = background_rect.width
hauteur_fond = background_rect.height
ecran = pygame.display.set_mode((largeur_fond, hauteur_fond))
pygame.display.set_caption("jeu fisik")
image = pygame.image.load("image_DOWN.png").convert_alpha()
hauteur_perso = image.get_rect().height
largeur_perso = image.get_rect().width

y,x=0,0
left,right,up,down=0,0,0,0
compteur=20
clock= pygame.time.Clock()

continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    mouvement = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and x>=0:
        x-=3
        mouvement = True
        if compteur%20==0:
            if left==0:
                image = pygame.image.load("image_LEFT_0.png").convert_alpha()
                left=1
            elif left==1:
                image = pygame.image.load("image_LEFT.png").convert_alpha()
                left=2
            elif left==2:
                image = pygame.image.load("image_LEFT_1.png").convert_alpha()
                left=3
            elif left==3:
                image = pygame.image.load("image_LEFT.png").convert_alpha()
                left=0
        compteur+=1
    if pressed[pygame.K_RIGHT] and x<= (largeur_fond - largeur_perso):
        x+=3
        mouvement = True
        if compteur%20==0:
            if right==0:
                image = pygame.image.load("image_RIGHT_0.png").convert_alpha()
                right=1
            elif right==1:
                image = pygame.image.load("image_RIGHT.png").convert_alpha()
                right=2
            elif right==2:
                image = pygame.image.load("image_RIGHT_1.png").convert_alpha()
                right=3
            elif right==3:
                image = pygame.image.load("image_RIGHT.png").convert_alpha()
                right=0
        compteur+=1
    if pressed[pygame.K_UP]and y>=0:
        y-=3
        mouvement = True
        if compteur%20==0:
            if up==0:
                image = pygame.image.load("image_UP_0.png").convert_alpha()
                up=1
            elif up==1:
                image = pygame.image.load("image_UP_1.png").convert_alpha()
                up=0
        compteur+=1
    if pressed[pygame.K_DOWN] and x<= (hauteur_fond - hauteur_perso):
        y+=3
        mouvement = True
        if compteur%20==0:
            if down==0:
                image = pygame.image.load("image_DOWN_0.png").convert_alpha()
                down=1
            elif down==1:
                image = pygame.image.load("image_DOWN_1.png").convert_alpha()
                down=0
        compteur+=1
    if event.type == pygame.KEYUP and mouvement == False:
        if event.key == pygame.K_LEFT:
            image = pygame.image.load("image_LEFT.png").convert_alpha()
        if event.key == pygame.K_RIGHT:
            image = pygame.image.load("image_RIGHT.png").convert_alpha()
        if event.key == pygame.K_UP:
            image = pygame.image.load("image_UP.png").convert_alpha()
        if event.key == pygame.K_DOWN:
            image = pygame.image.load("image_DOWN.png").convert_alpha()

    ecran.fill((255,255,255))
    ecran.blit(background, (0,0))
    ecran.blit(image, (x,y))
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
