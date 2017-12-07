import random, math

# This class applies to cities and the troops within them.
# The cityClass.py will address units in cities.
# This class gives you a few things about a city:
# 1) Province
# 2) Garrison
# 3) Stockpile (how long it can hold out under seige in amount of turns)
# 4) Tax Level (Very Low, Low, Normal, High, Very High)
# 5) Raise and Lower Taxes (Changes tax level and associated tax income as well as loyalty)
# 6) Displays taxes
# 7) Displays loyalty
# 8) 
# If you need any more functionality, please notify Bonds

# Make a player class...

class City(object):
    def __init__(self,province,citytype,garrison,taxlvl,resources,income,pbuilds,cbuilds,troop_list,x,y):
        self.province = province
        self.citytype = citytype if citytype else "City"
        self.garrison = garrison if garrison else 0
#        self.stockpile = stockpile if stockpile else 2
        self.taxlvl = taxlvl if taxlvl else "Normal"
#        self.taxes = taxes
        self.resources = resources
        self.income = income
#        self.expenses = expenses
#        self.loyalty = loyalty
        self.pbuilds = pbuilds if pbuilds else [] #Possible builds
        self.cbuilds = cbuilds if cbuilds else [] #Complete builds
        self.tl = troop_list
        self._x = x
        self._y = y

    def __repr__(self):
        return "City({},{},{},{},{},{},{},{},{},{},{})".format(self.province,self.citytype,self.garrison,self.taxlvl,self.resources,self.income,self.pbuilds,self.cbuilds,self.tl,self._x,self._y)
        
    def stats(self): #Good
        return "CITY STATS: | Province: {} | Garrison: {} | Taxes: {} | Income: {}".format(self.province,self.garrison,self.taxlvl,self.income)

    def province(self): #'str' object is not callable
        return self.province

    def garrison(self): #'int' object is not callable
        return self.garrison

    def stockpile(self): #Good
        if self.citytype == "None":
            stockpile = 0
        elif self.citytype == "City":
            stockpile = 2
        elif self.citytype == "Castle":
            stockpile = 4
        return stockpile

    def taxlvl(self): #'str' object is not callable
        return self.taxlvl

    def raisetaxes(self): #Good
        if self.taxlvl == "Very Low":
            self.taxlvl = "Low"
            return self.taxlvl
        elif self.taxlvl == "Low":
            self.taxlvl = "Normal"
            return self.taxlvl
        elif self.taxlvl == "Normal":
            self.taxlvl = "High"
            return self.taxlvl
        elif self.taxlvl == "High":
            self.taxlvl = "Very High"
            return self.taxlvl
        elif self.taxlvl == "Very High":
            self.taxlvl = "Very High"
            return self.taxlvl

    def lowertaxes(self): #Good
        if self.taxlvl == "Very Low":
            self.taxlvl = "Very Low"
            return self.taxlvl
        elif self.taxlvl == "Low":
            self.taxlvl = "Very Low"
            return self.taxlvl
        elif self.taxlvl == "Normal":
            self.taxlvl = "Low"
            return self.taxlvl
        elif self.taxlvl == "High":
            self.taxlvl = "Normal"
            return self.taxlvl
        elif self.taxlvl == "Very High":
            self.taxlvl = "High"
            return self.taxlvl

    def taxes(self): #Good
        if self.taxlvl == "Very Low":
            tax = int(0.10 * self.income)
            return tax
        elif self.taxlvl == "Low":
            tax = int(0.20 * self.income)
            return tax
        elif self.taxlvl == "Normal":
            tax = int(0.30 * self.income)
            return tax
        elif self.taxlvl == "High":
            tax = int(0.40 * self.income)
            return tax
        elif self.taxlvl == "Very High":
            tax = int(0.50 * self.income)
            return tax

    def loyalty(self): #'tax' is not defined
        if self.taxlvl == "Very Low":
            tax = int(0.10 * self.income)
        elif self.taxlvl == "Low":
            tax = int(0.20 * self.income)
        elif self.taxlvl == "Normal":
            tax = int(0.30 * self.income)
        elif self.taxlvl == "High":
            tax = int(0.40 * self.income)
        elif self.taxlvl == "Very High":
            tax = int(0.50 * self.income)
        troop_pct = self.garrison * 2 #Represents percentage out of 200 (self.garrison/100)*200 = self.garrison * 2
        troop_pct = troop_pct + ((tax / self.income) * 100)
        if troop_pct > 200:
            troop_pct = 200
        elif troop_pct < 0:
            troop_pct = 0
        if troop_pct < 100:
            loyalty = int(100 - troop_pct)
            return loyalty #There is a loyalty % chance of a rebellion
        else:
            return 0

    def rebellion(self): #'tax' is not defined
        if self.taxlvl == "Very Low":
            tax = int(0.10 * self.income)
        elif self.taxlvl == "Low":
            tax = int(0.20 * self.income)
        elif self.taxlvl == "Normal":
            tax = int(0.30 * self.income)
        elif self.taxlvl == "High":
            tax = int(0.40 * self.income)
        elif self.taxlvl == "Very High":
            tax = int(0.50 * self.income)
        troop_pct = self.garrison * 2 #Represents percentage out of 200 (self.garrison/100)*200 = self.garrison * 2
        troop_pct = troop_pct + ((tax / self.income) * 100)
        if troop_pct > 200:
            troop_pct = 200
        elif troop_pct < 0:
            troop_pct = 0
        if troop_pct < 100:
            loyalty = int(100 - troop_pct)
        else:
            return 0
        if loyalty > 0:
            reb = random.randint(0,100)
            randorange = self.loyalty
            if reb in range(0,self.loyalty):
                return "REBELLION"
            else:
                return "PEACEFUL"

    def upgrade_to_city(self): #Good
        if self.citytype == "None":
            stockpile = 2
            self.citytype = "City"
        elif self.citytype == "City":
            stockpile = 2
            self.citytype = "City"
        return self.citytype,stockpile
                
    def upgrade_to_castle(self): #Good
        if self.citytype == "City":
            stockpile = 4
            self.citytype = "Castle"
        elif self.citytype == "Castle":
            stockpile = 4
            self.citytype = "Castle"
        return self.citytype,stockpile

    def expenses(self): #Good
        expenses = int(self.garrison * 0.25)
        return expenses

    def __add__(self,troops): #Merges what you select (troop) with the stationary unit (self)
        ttot = self.tot()
        if (ttot + troops.number()) > 1000:
            return "Merge Armies, cannot add more troops"
        else:
            return self.tl.append(troops)
        
    def remove(self,troop): #Pops and returns what you select (troop) from the stationary unit (self)
        thetroop = self.tl
        if troop in self.tl:
            return self.tl.pop(thetroop.index(troop))
        else:
            return "Nothing to do."

    def tot(self): #Good
        total = 0
        for troop in self.tl:
            add = troop.number()
            total += add
        return total
    
    def buildings(self): #Good
        return self.cbuilds
    
    def building_options(self): #Good
        province_builds = []
        citybuilds = ["Port","Barracks","Stable"] #Represent attributes of these buildings later.
        castlebuilds = ["Foundry","University"] #Additional buildings that can only be built with a castle.
        if self.citytype == "None":
            return self.pbuilds
        elif self.citytype == "City":
            for cybuild in citybuilds:
                self.pbuilds.append(cybuild)
            return self.pbuilds
        elif self.citytype == "Castle":
            for cabuild in castlebuilds:
                self.pbuilds.append(cabuild)
            return self.pbuilds
            
    def build_something(self,building): #Good
        province_builds = []
        citybuilds = ["Port","Barracks","Stable"] #Represent attributes of these buildings later.
        castlebuilds = ["Foundry","University"] #Additional buildings that can only be built with a castle.
        self.pbuilds.remove(building)
        self.cbuilds.append(building)
        return self.pbuilds,self.cbuilds
        
    def destroy_something(self,building): #Good
        self.pbuilds.append(building)
        self.cbuilds.remove(building)
        return self.pbuilds,self.cbuilds
        
#    def __add__(self,item,itemtype): #Adds item based off of either the type "Building" or "Troop"
#        ttot = self.tot()
#        if itemtype == "Troop":
#            if (ttot + item.number()) > 750:
#                return "Merge Armies, cannot add more troops"
#            else:
#                return self.tl.append(item)
#        elif itemtype == "Building":
#            return self.pbuilds.append(item) #Adds the building to the possible build items

#    def build(self):
#        return "Building itself"
        
#    def destroy(self):
#        return "Destroying"

    def location(self): #Good
        return "({},{})".format(self._x,self._y)

    def getImage(self): #Good
        gar_temp = self.garrison
        while gar_temp > 0:
            gar_temp -= 20
        gar_add = math.fabs(gar_temp)
        garrison_round = int(self.garrison + gar_add)
        city_image_name = "{}{}.png".format(self.citytype,garrison_round)
        return city_image_name

    def update_right(self,change): #All good.
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