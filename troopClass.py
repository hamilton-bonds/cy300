
class Troops(object):
    def __init__(self,name,category,number,rank,armor,weapon,king,prince,x,y):
        self.nam = name
        self.cat = category
        self.num = number
        self.rnk = rank
        self.arm = armor
        self.weap = weapon
        self.king = king
        self.prince = prince
        self._x = x
        self._y = y
        
    def __repr__(self):
        return "Troops({},{},{},{},{},{},{},{})".format(self.nam,self.cat,self.num,self.rnk,self.arm,self.weap,self.king,self.prince)
        
    def stats(self):
        return "TROOP STATS | Name: {} | Type: {} | Number: {} | Rank: {} | Armor: {} | Weapon: {} | King: {} | Prince: {} | Location: ({},{})".format(self.nam,self.cat,self.num,self.rnk,self.arm,self.weap,self.king,self.prince,self._x,self._y)

    def category(self):
        return self.cat
        
    def rank(self):
        return self.rnk
        
    def weapon(self):
        return self.weap
        
    def armor(self):
        return self.arm
        
    def upgrade_weapon(self):
        self.weap += 1
        return self.weap
        
    def upgrade_armor(self):
        self.arm += 1
        return self.arm
        
    def rank_up(self):
        self.rnk += 1
        return self.rnk
        
    def train(self):
        return "Training" #In progress
        
    def die(self):
        return "Removing" #In progress
        
    def disband(self):
        return "Disbanding" #In progress

    def location(self):
        return "({},{})".format(self._x,self._y)

    def getImage(self):
        troop_image_name = "{}.png".format(self.cat)
        return troop_image_name
        
    def update_right(self,change):
        troopx = self._x
        troopx += change
        return troopx
    
    def update_left(self,change):
        troopx = self._x
        troopx -= change
        return troopx
        
    def update_up(self,change):
        troopy = self._y
        troopy += change
        return troopy
        
    def update_down(self,change):
        troopy = self._y
        troopy -= change
        return troopy
    
