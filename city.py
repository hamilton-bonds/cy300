# This program is designed to allow the user to interface with a city in
# PYTHON TOTAL WAR

import string

######## VARIABLES ########
your_name = "Hamilton"
spacename = " " * (16 - len(your_name))

# Economic Variables
exports = 250
troop_cost = 100
building_cost = 100
tax_display = "Normal"
tax_setting = 3

# Military Variables
gar = 100
inprov = 0
troop_tot = gar + inprov

# Social Variables
loy_mod = 3
loyalty = (100 + ((gar/200) * 100)) * (loy_mod/3)
if loyalty > 200:
    loyalty = 200
elif loyalty < 0:
    loyalty = 0

# Economic Calculations
upkeep_cost = troop_tot / 10
upkeep_cost = int(troop_tot)
taxes = (tax_setting / 10) * exports
taxes = int(taxes)
income = taxes + exports
expenses = troop_cost + building_cost + upkeep_cost
net = income - expenses
net_str = str(net)

if net < 0:
    sign = "-"
else:
    sign = "+"
spacenet = " " * (8 - len(net_str))

export_one = "copper"
export_two = "rum"
export_three = ""
export_list = export_one + ", " + export_two + ", " + export_three + "."
spacex = " " * (24 - len(export_list))
econ_vars = (tax_display,tax_setting,exports,taxes,net,expenses,sign,spacenet)

# Military Calculations

# Social Calculations



######## FUNCTIONS ########

# City Panel
def your_city(your_city_select,give_close):
    give_next = ""
    while give_next == "" and give_close == "":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("+[O]--[E]conomic--|--[M]ilitary--|--[S]ocial--[B]+")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|                                                |")
        print("| + Please select a tab [E]/[M]/[S]              |")
        print("| + Owner: ",your_name,spacename,"                   |")
        print("| + Press [O] for the Overview                   |")
        print("| + Press [B] for the Building Menu              |")
        print("|                                                |")
        print("+----------------------------------------[C]lose-+\n")
        tab_select = input("")

        if tab_select in "Ee":
            give_next = "N"
            economic(econ_vars) #Add variables
        elif tab_select in "Mm":
            give_next = "N"
            military() #Add variables
        elif tab_select in "Ss":
            give_next = "N"
            social() #Add variables
        elif tab_select in "Cc":
            give_next = "N"
            give_close = "C"
        elif tab_select in "Oo":
            give_next = "N"
            overview() #Add variables
        elif tab_select in "Bb":
            give_next = "N"
            building() #Add variables
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+[O]--[E]conomic--|--[M]ilitary--|--[S]ocial--[B]+")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|                                                |")
            print("| + Please select a tab [E]/[M]/[S]              |")
            print("| + Owner: ",your_name,spacename,"                   |")
            print("| + Press [O] for the Overview                   |")
            print("| + Press [B] for the Building Menu              |")
            print("|                                                |")
            print("+----------------------------------------[C]lose-+")
            tab_select = input("")

    if give_close == "C":
        exit()


# Overview
def overview():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("+--------------------OVERVIEW--------------------+")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|                                                |")
    print("| + NET INCOME: ",sign,"$",net,spacenet,"                  |")
    print("| + GARRISON  : ",gar,"                            |")
    print("| + LOYALTY   : ",loyalty,"                            |")
    print("| + EXPORTS   : ",export_list,spacex,"      |")
    print("|                                                |")
    print("+-----------------------------------------[B]ack-+")
    next_over = input("")
    if next_over in "Bb":
        give_close = ""
        your_city(your_city_select,give_close)

# Economy
def economic(econ_vars):
    tax_display = econ_vars[0]
    tax_setting = econ_vars[1]
    tax_setting = int(tax_setting)
    exports = econ_vars[2]
    exports = int(exports)
    taxes = econ_vars[3]
    taxes = int(taxes)
    net = econ_vars[4]
    net = int(net)
    expenses = econ_vars[5]
    expenses = int(expenses)
    sign = econ_vars[6]
    spacenet = econ_vars[7]

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("+[<]--[E]conomic--|--[M]ilitary--|--[S]ocial--[>]+")
    print("|                 +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|+[<]--[T]axes--|--[I]ncome--|--[E]xpenses--[>]+ |")
    print("||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| |")
    print("||                                             | |")
    print("|| + Projected Net Income: ",sign,"$",net,spacenet,"     | |")
    print("|| + Please select a tab [T]/[I]/[E]           | |")
    print("||                                             | |")
    print("||                                             | |")
    print("|+--------------------------------[B]ack-------+ |")
    print("+----------------------------------------[C]lose-+")
    econ_select = input("")
    next_econ = "initial"
    econ_close = 0
    prev_econ = "B"

    while econ_close == 0:
        if (econ_select in "Tt" and (next_econ == "initial")) or (prev_econ == "E" and next_econ in ">.") or (prev_econ == "I" and next_econ in "<,") or (next_econ == "initial" and (econ_select in "<," or econ_select in ">.")) or (next_econ in "Tt"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+[<]--[E]conomic--|--[M]ilitary--|--[S]ocial--[>]+")
            print("|                 +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|+[<]--[T]axes--|--[I]ncome--|--[E]xpenses--[>]+ |")
            print("|+              +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| |")
            print("||  {Taxes}   [ Taxes: ",taxes,"]","\t\t","      | |")
            print("||                                             | |")
            print("||   1) [-]\t",tax_display,"\t","[+]           | |")
            print("||                                             | |")
            print("||                                             | |")
            print("|+--------------------------------[B]ack-------+ |")
            print("+----------------------------------------[C]lose-+")
            prev_econ = "T"
            
            next_econ = input("")
            if next_econ == "-":
                tax_setting -= 1

                if tax_setting == 0:
                    tax_setting = 5
                elif tax_setting == 6:
                    tax_setting = 1

                if tax_setting == 1:
                    tax_display = "Very Low "
                    next_econ = "T"
                elif tax_setting == 2:
                    tax_display = "Low      "
                    next_econ = "T"
                elif tax_setting == 3:
                    tax_display = "Normal   "
                    next_econ = "T"
                elif tax_setting == 4:
                    tax_display = "High     "
                    next_econ = "T"
                elif tax_setting == 5:
                    tax_display = "Very High"
                    next_econ = "T"

            elif next_econ == "+":
                tax_setting += 1

                if tax_setting == 0:
                    tax_setting = 5
                elif tax_setting == 6:
                    tax_setting = 1

                if tax_setting == 1:
                    tax_display = "Very Low "
                    next_econ = "T"
                elif tax_setting == 2:
                    tax_display = "Low      "
                    next_econ = "T"
                elif tax_setting == 3:
                    tax_display = "Normal   "
                    next_econ = "T"
                elif tax_setting == 4:
                    tax_display = "High     "
                    next_econ = "T"
                elif tax_setting == 5:
                    tax_display = "Very High"
                    next_econ = "T"

            taxes = (tax_setting / 10) * exports
            taxes = int(taxes)
            income = taxes + exports
            net = income - expenses
            if net < 0:
                sign = "-"
            else:
                sign = "+"
            spacenet = " " * (8 - len(net_str))
        
        elif (econ_select in "Ii" and (next_econ == "initial")) or (prev_econ == "T" and next_econ in ">.") or (prev_econ == "E" and next_econ in "<,") or (next_econ in "Ii"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+[<]--[E]conomic--|--[M]ilitary--|--[S]ocial--[>]+")
            print("|                 +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|+[<]--[T]axes--|--[I]ncome--|--[E]xpenses--[>]+ |")
            print("||~~~~~~~~~~~~~~+            +~~~~~~~~~~~~~~~~~| |")
            print("||  {Income}                                   | |")
            print("||      - Exports: $",exports,"                      | |")
            print("||      - Taxes  : $",taxes,"                       | |")
            print("||      - Total  : $",net,"                       | |")
            print("||                                             | |")
            print("|+--------------------------------[B]ack-------+ |")
            print("+----------------------------------------[C]lose-+")
            prev_econ = "I"
            next_econ = input("")
        
        elif (econ_select in "Ee" and (next_econ == "initial")) or (prev_econ == "T" and next_econ in "<,") or (prev_econ == "I" and next_econ in ">.") or (next_econ in "Ee"):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+[<]--[E]conomic--|--[M]ilitary--|--[S]ocial--[>]+")
            print("|                 +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|+[<]--[T]axes--|--[I]ncome--|--[E]xpenses--[>]+ |")
            print("||~~~~~~~~~~~~~~~~~~~~~~~~~~~+                 + |")
            print("||  {Expenses}                                 | |")
            print("||                                             | |")
            print("||                                             | |")
            print("||                                             | |")
            print("||                                             | |")
            print("|+--------------------------------[B]ack-------+ |")
            print("+----------------------------------------[C]lose-+")
            prev_econ = "E"
            next_econ = input("")

        elif (econ_select in "Bb") or (next_econ in "Bb"):
            give_close = ""
            your_city(your_city_select,give_close)
            econ_close = 1
            return taxes
            return tax_setting
            return tax_display

        elif (econ_select in "Cc") or (next_econ in "Cc"):
            give_close = "C"
            your_city(your_city_select,give_close)
            econ_close = 1
            return taxes
            return tax_setting
            return tax_display

        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+[<]--[E]conomic--|--[M]ilitary--|--[S]ocial--[>]+")
            print("|                 +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|+[<]--[T]axes--|--[I]ncome--|--[E]xpenses--[>]+ |")
            print("||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| |")
            print("||                                             | |")
            print("|| + Projected Net Income: ",sign,"$",net,spacenet,"     | |")
            print("|| + Please select a tab [T]/[I]/[E]           | |")
            print("||                                             | |")
            print("||                                             | |")
            print("|+--------------------------------[B]ack-------+ |")
            print("+----------------------------------------[C]lose-+")
            econ_select = input("")
            next_econ = ""
            econ_close = 0

# Military
def military():
    a = 1 #Holding variable
    print("military tab")

# Social
def social():
    b = 2 #Holding variable
    print("social tab")

# Building
def building():
    c = 3 #Holding variable
    print("building tab")

# Exit Function
def exit():
    print("Returning to map...")
#    exit = input("")
    


######## MAIN PROGRAM ########
if __name__ == '__main__':
    your_city_select = 1
    give_close = ""
    your_city(your_city_select,give_close)
