from unitClass import *
from cityClass import *

class Troops(object):
    def __init__(self,name,category,number=100,rank=1,armor=1,weapon=1,king=0,prince=0):
        self.nam = name
        self.cat = category
        self.num = number if number else 100
        self.rnk = rank if rank else 1
        self.arm = armor if armor else 1
        self.weap = weapon if weapon else 1
        self.king = king if king else 0
        self.prince = prince if prince else 0
        
    def __repr__(self):
        return "Troops({},{},{},{},{},{},{},{})".format(self.nam,self.cat,self.num,self.rnk,self.arm,self.weap,self.king,self.prince)
        
    def stats(self):
        return "TROOP STATS | Name: {} | Type: {} | Number: {} | Rank: {} | Armor: {} | Weapon: {} | King: {} | Prince: {}".format(self.nam,self.cat,self.num,self.rnk,self.arm,self.weap,self.king,self.prince)

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

    def getTroopImage(self):
        troop_image_name = "{}.png".format(self.cat)
        return troop_image_name
        
    #Object needs no update or location since the unit holds that information.