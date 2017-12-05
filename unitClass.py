import math

# This class applies to units in provinces, not in cities.
# The cityClass.py will address units in cities.

class Unit(object):
    def __init__(self,troop_list,total,round):
        self.tl = troop_list if troop_list else []
        self.tot = total
        self.rnd = round
        
    def __repr__(self):
        return "Unit[{}]".format(self)
    
    def stats(self):
        return "UNIT STATS: COMING SOON!"
        
    def comp(self):
        return "COMPOSITION:  TBD"
        
    def merge(self,other): #Merges what you select (other) with the stationary unit (self)
        return troop_list.append(other)
        
    def unmerge(self,other): #Pops and returns what you select (other) from the stationary unit (self)
        return troop_list.pop(troop_list.index(other))
        
    def die(self):
        return "DYING"
        
    def create(self):
        return "CREATING"
        
    def rnd(self):
        sub = self.tot
        display = self.tot
        while sub > 0:
            sub -= 10
        display = self.tot + math.fabs(sub)
        return display
        
    def getImage(self):
        unit_image_name = "Unit{}.png".format(self.rnd())
        return unit_image_name