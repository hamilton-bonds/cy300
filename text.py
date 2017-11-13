import pygame, sys, random, time
from pygame.locals import *

#Pre-defined Colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#Terminate Application
def terminate():
    pygame.quit()
    sys.ext()
    
#Write Text on the Screen
def drawText(text, font, screen, x, y, pos):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    if pos == 'c':
        textrect.center = (x,y)
    elif loc == "l":
        textrect.topleft = (x,y)
    elif loc == "r":
        textrect.topright = (x,y)        
    screen.blit(textobj, textrect)
    
#Main Menu
def main_menu(screen):
    screen.fill(GREEN)
    font = pygame.font.SysFont(None, 50)
    drawText('Total War!', font, screen, 400, 50, 'c')
    font = pygame.font.SysFont(None, 25)
    drawText('Hit ENTER to play', font, screen, 400, 460, 'c')
    drawText('Hit ESC to quit', font, screen, 400, 480, 'c')

#Map of main game
def game_map(screen):
    screen.fill(GREEN)
    
#Move Troops
def move_troops(troopx,troopy,mousex,mousey):
    troopx = mousex
    troopy = mousey
    return troopx, troopy
    
#Start the Game
def playGame():
    pygame.init()
    gameState = 'starting'

    #Screen for the game
    screen = pygame.display.set_mode([800,600])
    pygame.display.set_caption('Game Test')
    
    #Load Images
    castle = pygame.image.load('Castle.png')
    troop = pygame.image.load('cavalry.png')
    
    #Image Rectangles
    castleRect = castle.get_rect()
    troopRect = troop.get_rect()
    
    #Troop Starting Position
    troopx = 250
    troopy = 50
    
    #main loop
    while True:
        if gameState == 'starting':
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminate()
                    elif event.key == K_RETURN:
                        gameState = 'game'
                        
            #open the main menu
            main_menu(screen)
            
        #main game
        elif gameState == 'game':
            game_map(screen)
            troop_pos = [troopx, troopy]
            screen.blit(castle, [200,50])
            screen.blit(troop, troop_pos)
            (mousex, mousey) = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminate()
                elif event.type == MOUSEBUTTONDOWN:
                    troopx, troopy = move_troops(troopx,troopy,mousex,mousey)
                        
            
            
        #update display
        pygame.display.update()
            
    
    
    
