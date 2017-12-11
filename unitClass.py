import math, string
from troopClass import *

# This class applies to units in provinces, not in cities.
# The cityClass.py will address units in cities.
# This class gives you a few things about a unit:
# 1) What it's made of (just type 'unit')
# 2) Add and remove troops from the unit
# 3) Displays when you've added too many (removing to 0 just triggers removal from total list of troops)
# 4) Total troops
# 5) The unit's image
# 6) Positional updates
# If you need any more functionality, please notify Bonds

class Unit(object):
    def __init__(self,troop_list,garded,x,y):
        self.tl = troop_list if troop_list else []
        self.gard = garded if garded else 0
        self._x = x
        self._y = y
        
    def __repr__(self):
        return "Unit({},{},{})".format(self.tl,self._x,self._y)
    
    def stats(self):
        for uns in self.ul:
            print(uns) #Will change later to enumerate inf,cav,art and numbers
        
    def comp(self):
        return self
        
    def __add__(self,troop): #Merges what you select (troop) with the stationary unit (self)
        ttot = self.tot()
        if (ttot + troop.number()) > 750:
            return "Merge Armies, cannot add more troops"
        else:
            return self.tl.append(troop)
        
    def remove(self,troop): #Pops and returns what you select (troop) from the stationary unit (self)
        thetroop = self.tl
        return self.tl.pop(thetroop.index(troop))
        
#    def die(self):
#        totcomp = self.tot()
#        print("Will simply remove from list based off of total")

    def addToGarrison(self):
        self.gard = 1
        return self.gard
    def remFromGarrison(self):
        self.gard = 0
        return self.gard
        
    def isGarrisoned(self):
        return gard == 1
        
    def tot(self):
        total = 0
        for troop in self.tl:
            add = troop.number()
            total += add
        return total
        
    def getUnitImage(self):
        sub = self.tot
        while sub > 0:
            gar_temp -= 10
        sub_add = math.fabs(sub)
        rounded = int(self.tot + sub_add)
        unit_image_name = "Unit{}.png".format(rounded)
        return unit_image_name

    def updateLocation(newx,newy):
        self._x = newx
        self._y = newy
        return self._x,self._y
        
    def update_right(self,change): #Updates based on the scroll.
        self._x += change
        return self._x
    
    def update_left(self,change):
        self._x -= change
        return self._x
        
    def update_up(self,change):
        self._y += change
        return self._y
        
    def update_down(self,change):
        self._y -= change
        return self._y