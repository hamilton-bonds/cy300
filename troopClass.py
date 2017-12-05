
class Troops(object):
    def __init__(self,name,category,number,rank,armor,weapon,king,prince):
        self.nam = name
        self.cat = category
        self.num = number
        self.rnk = rank
        self.arm = armor
        self.weap = weapon
        self.king = king
        self.prince = prince
        
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
        return "Training"
        
    def die(self):
        return "Removing"
        
    def disband(self):
        return "Disbanding"
        
    def getImage(self):
        troop_image_name = "{}.png".format(self.cat)
        return troop_image_name