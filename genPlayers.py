from playerClass import *

master_list = []
factions_available = ["English","French","German"]

#Player goes to a screen with all factions listed, uses drop-down menu to assign himself to that class.

def gameSettings():
    period = input("Period : ")

def createGameAccount: #Can do game stats later for funzies.
    username = input("Username: ")
    master_list.append(username) #Username's position in the list counts as its user ID

def humanCreator(username,factions):
    fact_sel = input("Select a faction: ")
    factions_available.remove(fact_sel)

def aiCreator():

def factionAssign():
    for faction in factions:
        for player in master_list:
            if player.factionDisplay() == faction:
                