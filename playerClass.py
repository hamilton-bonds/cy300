class Player(object):
    def __init__(self,name="",type="",faction="",province_list=[]):
        self.name = name if name else ""
        self.type = "COMPUTER" if name == "AI" else "HUMAN" #Get player to input these values.
        self.fac = faction if faction else ""
#        self.per = period if period else "" #Make this a part of the game object.  Will be valuable for saved games.
#        self.dif = difficulty if difficulty else "" #Make this a part of the game object.  Will be valuable for saved games.
        self.pl = province_list if province_list else []

    def __repr__(self):
        return "Player({},{},{})".format(self.name,self.type,self.fac)
        
    def stats(self):
        return "PLAYER STATS: | Name: {} | Type: {} | Faction: {}".format(self.name,self.type,self.fac)
        
    def nameDisplay(self): #methods to retrieve/display information
        return self.name
        
    def factionDisplay(self):
        return self.fac
        
#    def getPeriod(self): #Make this a part of the game object.  Will be valuable for saved games.
#        return self.per
        
#    def getDifficulty(self): #Make this a part of the game object.  Will be valuable for saved games.
#        return self.dif
        
    def ai(self):
        return self.type == "COMPUTER"
        
    def human(self):
        return self.type == "HUMAN"
        
    def you(self,string): #Where string represents a person's name or user ID.
        return string == self.name
        
    def provinceList(self):
        return self.pl
        
    def __add__(self,prov): #conquering or populating
        return self.pl.append(prov)
        
    def remove(self,prov):
        return self.pl.remove(self.pl.index(prov))