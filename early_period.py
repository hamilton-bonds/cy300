#This file is designed to create starting values for Python Total War Early Period.

import string


# Troop Locations in a Province
English_Military = [
                    [{"Mercia":[[[0,0],[[300,1,1,1,1],[150,1,1,1,0],[450,1,1,1,0],[900],[1,1]]]]},
                    {"Wales":[[[100,100],[[300,1,1,1,1],[150,1,1,1,0],[250,1,1,1,0],[700],[0,0]]]]}]
                    ]

#French_Military = [
#                   [{"Ile-de-France":[[[200,200],[[300,1,1,1,1],[150,1,1,1,0],[450,1,1,1,0],[900],[1,1]]]]},
#                   {"Normandy":[[[300,300],[[300,1,1,1,1],[150,1,1,1,0],[250,1,1,1,0],[700],[0,0]]]]}]
#                   ]

#German_Military = [
#                   [{"Bavaria":[[[400,400],[[300,1,1,1,1],[150,1,1,1,0],[450,1,1,1,0],[900],[1,1]]]]},
#                   {"Silesia":[[[500,500],[[300,1,1,1,1],[150,1,1,1,0],[250,1,1,1,0],[700],[0,0]]]]}],
#                   [{"Bohemia":[[[600,600],[[300,1,1,1,1],[150,1,1,1,0],[450,1,1,1,0],[900],[1,1]]]]},
#                   {"Munchen":[[[700,700],[[300,1,1,1,1],[150,1,1,1,0],[250,1,1,1,0],[700],[0,0]]]]}],
#                   ]

#City Owners
#What do I want to know about a city?
# 1. Income
# 2. Loyalty
# 3. Resources
# 4. Taxation

factions = [["English",English_Military]]
#,["French",French_Military],["German",German_Military]]

military_dict = {}

for faction in factions:
    military_dict[faction[0]] = faction[1]
    print(military_dict[faction[0]])
