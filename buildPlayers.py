#Builds Players
from playerClass import *

#USE:  run this set of programs using buildPlayers() to start a game.  To load it, simply use the loadValues program. (Coming soon)

#You can replace this later with menus that display and modify the same information.  This is just the logic.
faction_list = [
                ["English","Open"],
                ["French","Open"],
                ["Germans","Open"],
                ["Spanish","Open"],
                ["Italians","Open"],
                ["Russians","Open"],
                ["Polish","Open"],
                ["Turkish","Open"]]

taken = []
available = []
gameValues = []
player_list = []
turn_order = []

#THE FOLLOWING ITEMS ARE INDEPENDENT OF THE PLAYERCLASS MODULE.  THEY ARE IN ORDER OF USE.
def modeSelect(): #Represents main menu.
    print("\n\nSELECT A MODE")
    modeSelect = input("\n\n[S]ingle Player | [M]ultiplayer : ")
    if modeSelect in "Ss":
        singlePlayer()
    elif modeSelect in "Mm":
        multiPlayer()
    else:
        modeSelect()

def difficultySelect():
    print("\n\nSELECT A DIFFICULTY")
    difficulty = input("\n\n[E]asy | [M]edium | [H]ard : ")
    if difficulty in "Ee":
        difficulty = "Easy"
    elif difficulty in "Mm":
        difficulty = "Medium"
    elif difficulty in "Hh":
        difficulty = "Hard"
    else:
        difficultySelect()
    gameValues.append(difficulty)
    return gameValues

def periodSelect():
    print("\n\nSELECT A PERIOD")
    period = input("\n\n[E]arly | [M]iddle | [L]ate : ")
    if period in "Ee":
        period = "Early"
    elif period in "Mm":
        period = "Middle"
    elif period in "Ll":
        period = "Late"
    else:
        periodSelect()
    gameValues.append(period)
    return gameValues

def factionSelect(faction_list,player_list,taken,available):
    updateAvailableFactions()
    for player in player_list:
        print("\n\nSELECT A FACTION (#), ",player,": ")
        print("")
        for num,faction in enumerate(faction_list):
            print(" ",(num+1),". \t",faction[0],"\t | ",faction[1],"\t |")
        print("")
        fSelect = input("\n\nTYPE FACTION NUMBER: ")
        fSelect = int(fSelect) - 1 #To account for the fact that the list starts at 0
        for num,faction in enumerate(faction_list):
            if num in taken:
                print("\n\nFACTION TAKEN")
                factionSelect(faction_list)
            else:
                faction_list[fSelect][1] = player
    for num,faction in enumerate(faction_list): #Generate AI
        if faction[1] == "Open":
            faction[1] = "AI"
    for player in player_list:
        for faction in faction_list:
            p = player
            f = faction[0]
            if faction[1] == player:
                turn_order.append([f,p])
    for faction in faction_list:
        f = faction[0]
        if faction[1] not in player_list:
            turn_order.append([f,"AI"])
    return faction_list,turn_order
        
def updateAvailableFactions():
    for i in range(0,len(faction_list)): #Determine a list of available numbers
        taken = []
        available = []
        if faction_list[i][1] == "Open":
            available.append(i)
        else:
            taken.append(i)
    return taken,available
        
def singlePlayer():
    print("\n\nSINGLE PLAYER")
    aplayer = input("Who will be playing? ")
    player_list.append(aplayer)
    return player_list
    
def multiPlayer():
    print("\n\nMULTIPLAYER")
    pSelector = "A"
    while pSelector not in "Dd":
        if player_list:
            i = 0
            for i in range(0,len(player_list)):
                print("\n\nPLAYERS:")
                print("")
                print(" ",i+1,". \t",player_list[i],"\t |")
                print("")
        pSelector = input("\n\n[A]dd | [R]emove | [D]one : ")
        if pSelector in "Aa":
            new_player = input("\n\nPlayer Name: ")
            player_list.append(new_player)
        elif pSelector in "Rr": #Reminder: don't allow this if NOT player_list.
            remove_player = int(input("\n\nSelect Player Number to Remove: "))
            player_list.remove(player_list[remove_player-1])
    return player_list

def buildPlayers(faction_list,turn_order):
    modeSelect()
    difficultySelect()
    periodSelect()
    factionSelect(faction_list,player_list,taken,available)

def runBuildPlayers():
    buildPlayers(faction_list,turn_order)
    return turn_order
    
#if __name__ == '__main__': #Comment this in order to make it importable.
#    buildPlayers(faction_list)
#    print("\n\nFaction List: ",faction_list)
#    print("\n\nTurn Order  : ",turn_order)
#    print("\n\nGame Values : ",gameValues)