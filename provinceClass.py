import math, string
from unitClass import *
from cityClass import *

# This class applies to units in provinces, not in cities.
# This class is in progress.

class Province(object):
    def __init__(self,name,owner,unit_list=[],city,x,y):
        self.name = name
        self.owner = owner
        self.ul = unit_list if unit_list else []
        self.city = city if city else City()
        self._x = x
        self._y = y
        
    def __repr__(self):
        return "Province({},{},{})".format(self.ul,self._x,self._y)
    
    def stats(self):
        return "PROVINCE STATS: COMING SOON!"
        
    def comp(self):
        return self
        
    def __add__(self,units): #Merges what you select (units) with the stationary unit (self)
        ttot = self.tot()
        if (ttot + units.number()) > 750:
            return "Merge Armies, cannot add more troops"
        else:
            return self.ul.append(units)
        
    def remove(self,units): #Pops and returns what you select (unitsp) from the stationary unit (self)
        theunit = self.ul
        return self.ul.pop(theunit.index(units))
        
    def die(self):
        totcomp = self.tot()
        print("Will simply remove from list based off of total")

    def tot(self):
        total = 0
        for troop in self.tl:
            add = troop.number()
            total += add
        return total
        
    def getImage(self):
        sub = self.tot
        while sub > 0:
            gar_temp -= 10
        sub_add = math.fabs(sub)
        rounded = int(self.tot + sub_add)
        unit_image_name = "Unit{}.png".format(rounded)
        return unit_image_name

    def update_right(self,change):
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