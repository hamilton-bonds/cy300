import pygame, sys, random, time
from pygame.locals import *

##################################################################
##################GAME CONSTANTS AND VALUES#######################
##################################################################
#Pre-defined Colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#USER VALUES
username = "Hamilton"
fselect = "English"
period = "early_period.txt"
difficulty = "easy"
values = [username,fselect,period,difficulty]

#Generate the first map
#Map Starting Position and Values
mapx = -750
mapy = -750

troops = dict()
cities = dict()
#Initialize list of factions, add more later
factions = ["English","French","German"]

#                              LOCATION     DATA         LOCATION     DATA
#    { faction1: [{province1: [[ [x,y] , [troopdata] ] , [ [x,y] , [citydata] ]] }] }
#                             AC COORD   D         D C   T COORD   D        D TA
#
#                     A=all,C=city,COORD=coordinates,D=data,T=troops
#
#OTHER EXAMPLES:
#troopdata = [[300,8,3,4,1],[150,1,3,1,0],[450,2,1,1,0],[900],[1,1]]
#troopexam = [[#inf,val,armour,weapon,general],[#cav,val,armour,weapon,general],[#art,val,armour,weapon,general],[#tot],[king,prince]]
#
#citydata = [["CITY","City.png"],[[300,8,3,4,1],[150,1,3,1,0],[450,2,1,1,0],[900],[0,1]]]
#cityexam = [[type,image],[[garrison troop data]]
#
#Iterate through the period file to get starting values

province_dict_list = []
city_dict_list = []

with open(period,"r") as pfile:
    for faction in factions:
        for line in pfile:
            line.split(',') #It's a CSV
            if line[0] == "STI":  #Starting troop information
                for word in line:  #We want this to iterate only on the line that pertains to its faction
                    province_dict_list.append()
            if line[0] == "SCI":  #Starting city information
                for word in line:  #Again, iterating only on the faction line
                    

    word_list_list = []
    for line in pfile:
        line.split(',')
        word_list = []
        tipa = line[0]
        if tipa == "STI":
            if faction == line[1]:
                for word in line:
                    word_list.append(word)
            word_list_list.append(word_list)
        troops[faction] = word_list_list

        if tipa == "SCI":
            if faction == line[1]:
                for word in line:
                    word_list.append(word)
            word_list_list.append(word_list)
        cities[faction] = word_list_list
print("\nTROOPS\n",troops,"\n\n")
print("\nCITIES\n",cities,"\n\n")

##################################################################
##################END CONSTANTS AND VALUES########################
##################################################################

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
    drawText('Python Total War!', font, screen, 400, 50, 'c')
    font = pygame.font.SysFont(None, 25)
    drawText('Hit ENTER to play', font, screen, 400, 460, 'c')
    drawText('Hit ESC to quit', font, screen, 400, 480, 'c')

#def faction_menu(screen): #If captioned, manually input factions.
#    screen.fill(GREEN)
#    font = pygame.font.SysFont(None, 50)
#    drawText('Select Your Faction!', font, screen, 400, 50, 'c')
#    font = pygame.font.SysFont(None, 25)
#    drawText('Hit ENTER to play', font, screen, 400, 460, 'c')
#    drawText('Hit ESC to quit', font, screen, 400, 480, 'c')

#Map of main game
def game_map(screen,mapx,mapy):
    screen.fill(GREEN)
    europe = pygame.image.load('europe.jpg')
    screen.blit(europe,[mapx,mapy]) #Will later define starting x and y for different factions.
    return screen.blit(europe,[mapx,mapy])
    
#Move Troops
def move_troops(troopx,troopy,mousex,mousey):
    troopx = mousex
    troopy = mousey
    return troopx, troopy

#Render all item positions
def render_positions(positions):
    for pos in positions:
        troop_positions = positions[0]
        city_positions = positions[1]
    for entities in troop_positions:
        entities[0] = troopx
        entities[1] = troopy
    for city in city_positions:
        city[0] = castlex 
        city[1] = castley
    return screen.blit(castle,[castlex,castley]), screen.blit(troop,[troopx,troopy])

#Update all item positions when scrolling
def positions_updates(positions,change):
    for entities in troop_positions:
        entities[0] += change
        entities[1] += change
    for city in cities:
        city[0] += change
        city[1] += change
    mapx += change
    mapy += change
    render_positions(positions)
    return positions

#Render the map's items    
def render_map_items(factions):
    get_troops_and_cities_start()
    
    for faction in troops:
        print(faction)
    for faction in cities:
        print(faction)
    return 0
    #Load Images for each location...
#    castle = pygame.image.load('Castle.png')
#    troop = pygame.image.load('cavalry.png')
    
    #Image Rectangles
#    castleRect = castle.get_rect()
#    troopRect = troop.get_rect()




#//////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#//////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#                      Start the Game
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////////#

def playGame():
    pygame.init()
    gameState = 'starting'

    #Screen for the game
    screen = pygame.display.set_mode([800,600])
    pygame.display.set_caption('Game Test')
    
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
            game_values()
            username = values[0]
            fselect = values[1]
            period = values[2]

            render_map_items()

            game_map(screen,mapx,mapy)

            generate_map(owner)

            troop_pos = [troopx, troopy]
            (mousex, mousey) = pygame.mouse.get_pos()

            gameMap = pygame.image.load('europe.jpg')
            mapWidth = gameMap.get_width()
            mapHeight = gameMap.get_height()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN: #https://www.pygame.org/docs/ref/key.html
                    if event.key == K_ESCAPE:
                        terminate()
                    elif event.key == pygame.K_UP:
                        change = 50
                        positions_updates(positions,change)
                    elif event.key == pygame.K_DOWN:
                        change = -50
                        positions_updates(positions,change)
                    elif event.key == pygame.K_RIGHT:
                        change = -50
                        positions_updates(positions,change)
                    elif event.key == pygame.K_LEFT:
                        change = 50
                        positions_updates(positions,change)
#                    if gameMap.left < 0:
#                        gameMap.left = 0
#                    elif gameMap.right > -WIDTH:
#                        gameMap.right = -WIDTH
#                    elif gameMap.top < 0:
#                        gameMap.top = 0
#                    elif gameMap.bottom > -HEIGHT:
#                        gameMap.bottom = -HEIGHT
#                elif event.type == MOUSEBUTTONDOWN:
#                    troopx, troopy = move_troops(troopx,troopy,mousex,mousey)

#                    mapx, mapy = move_map(mapx,mapy,keyx,keyy)
#   #   #   #   #   #   #   #   #   #   #   #
#s        clock.tick(30)
                    
        pygame.display.update()

if __name__ == '__main__':
    playGame()
