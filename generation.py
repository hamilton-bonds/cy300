#IN PROGRESS
from playerClass import *
from buildPlayers import *
#from unitClass import *
#from cityClass import *
#from provinceClass import *

player_values = []
#city_unit_values = []
#prov_unit_values = []
city_values = []
prov_values = []

def generateAll():
    runBuildPlayers()
    generatePlayers(turn_order)
    generateCities()
    generateProvinces()
    return [player_values,city_unit_values,prov_unit_values,city_values,prov_values]

def generatePlayers(turn_order):
    for part in turn_order:
        fac = part[0]
        name = part[1]
        player_values.append(Player(name,"",fac))
    return player_values

#def generateCityUnits():
#    
#    return city_unit_values
    
#def generateProvUnits():
#    
#    return prov_unit_values

def generateCities():
    
    generateCityUnits()
    return city_values,city_unit_values

def generateProvinces():
    with open("starting_values.txt") as start:
        for line in start:
            line_list = []
            if line[0] != ";":
                a = line.split(":")
                for item in a:
                    line_list.append(item.split("|"))
                    p = line_list[0]
                    t = line_list[1]
                    u = line_list[2]
                    c = line_list[3]
                    prov = Prov(p[0],p[1],p[2],p[3],p[4],p[5])
                    troop = Troops(t[0],t[1],t[2])
                    city = City(p[0],c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9])
                    prov = prov + unit
                    
    generateProvUnits()
    return prov_values,prov_unit_values
