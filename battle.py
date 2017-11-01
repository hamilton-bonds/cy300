# Program for processing battle outcomes

# Inputs:  general_rank, unit_rank(s), troop_number(s), troop_type(s)
# Later, add armor, weapons, and allied/enemy ally units
# Can add this to CSV for convenience

# Processes whether or not the user wants to automatically resolve the battle.
def process_trigger_input(trigger_one,enemy_attacker,final_enemy_tot,final_your_tot,enemy_attacks_game):
    process_trigger_input_one = 5
    enemy_attacker = int(enemy_attacker)
    if trigger_one in 'Yy':
        attack_turn(final_enemy_tot,final_your_tot,enemy_attacker,enemy_attacks_game)
    else:
        print('Battle Exited')

#Cavalry first, infantry second, artillery third
#Suppose that enemy is attacking you.  This means that they move first.

# Gets battle numbers based off of the trigger processing.

# Takes battle inputs and uses mathematics to automatically resolve the battle and output final numbers
# Test is just based on final numbers
def process_battle_results(final_enemy_tot,final_your_tot,enemy_attacks_game):

    if final_your_tot == 0:
        print("DEFEAT!")
        print("ALLIES REMAINING: ",final_your_tot)
        print("ENEMIES REMAINING: ",final_enemy_tot)

    elif final_enemy_tot == 0:
        print("VICTORY!")
        print("ALLIES REMAINING: ",final_your_tot)
        print("ENEMIES REMAINING: ",final_enemy_tot)

    elif final_your_tot < final_enemy_tot:
        print("DEFEAT!")
        print("ALLIES REMAINING: ",final_your_tot)
        print("ENEMIES REMAINING: ",final_enemy_tot)

    elif final_enemy_tot < final_your_tot:
        print("VICTORY!")
        print("ALLIES REMAINING: ",final_your_tot)
        print("ENEMIES REMAINING: ",final_enemy_tot)

    elif final_your_tot == final_enemy_tot:
        if enemy_attacks_game == 1:
            print("VICTORY!")
            print("ALLIES REMAINING: ",final_your_tot)
            print("ENEMIES REMAINING: ",final_enemy_tot)
            result = "VICTORY!"
            return result
        else:
            print("DEFEAT!")
            print("ALLIES REMAINING: ",final_your_tot)
            print("ENEMIES REMAINING: ",final_enemy_tot)
            result = "DEFEAT!"
            return result
    else:
        print("ERROR!")

def attack_turn(final_enemy_tot,final_your_tot,enemy_attacker,enemy_attacks_game):
    time = 0
    while time < 600 or final_enemy_tot !=0 or final_your_tot != 0 or enemy_attacker == 3:
        time += 1
        if enemy_attacker == 1:
            #Allied troops calculation
            final_your_inf = your_inf - (enemy_art / art_v_inf)
            if final_your_inf < 0: #Protects against negative troop numbers
                final_your_inf = 0
            else:
                final_your_inf = final_your_inf

            final_your_cav = your_cav - (enemy_inf / inf_v_cav)
            if final_your_cav < 0: #Protects against negative troop numbers
                final_your_cav = 0
            else:
                final_your_cav = final_your_cav

            final_your_art = your_art - (enemy_cav / cav_v_art)
            if final_your_art < 0: #Protects against negative troop numbers
                final_your_art = 0
            else:
                final_your_art = final_your_art

            final_your_tot = final_your_inf + final_your_cav + final_your_art
            if final_your_tot < 0: #Protects against negative troop numbers
                final_your_tot = 0
            else:
                final_your_tot = int(final_your_tot)

            print("\n\tYOUR INFANTRY: ",your_inf,"\n\tYOUR CAVALRY: ",your_cav,"\n\tYOUR ARTILLERY: ",your_art,"\n\tYOUR TOTAL: ",final_your_tot)
            if final_your_tot != 0:
                enemy_attacker = 0
            else:
                enemy_attacker = 2

        elif enemy_attacker == 0:
            #Enemy troops calculation
            final_enemy_inf = enemy_inf - (your_art / art_v_inf)
            if final_enemy_inf < 0: #Protects against negative troop numbers
                final_enemy_inf = 0
            else:
                final_enemy_inf = final_enemy_inf

            final_enemy_cav = enemy_cav - (your_inf / inf_v_cav)
            if final_enemy_cav < 0: #Protects against negative troop numbers
                final_enemy_cav = 0
            else:
                final_enemy_cav = final_enemy_cav

            final_enemy_art = enemy_art - (your_cav / cav_v_art)
            if final_enemy_art < 0: #Protects against negative troop numbers
                final_enemy_art = 0
            else:
                final_enemy_art = final_enemy_art

            final_enemy_tot = final_enemy_inf + final_enemy_cav + final_enemy_art
            if final_enemy_tot < 0: #Protects against negative troop numbers
                final_enemy_tot = 0
            else:
                final_enemy_tot = int(final_enemy_tot)

            print("\n\tENEMY INFANTRY: ",enemy_inf,"\n\tENEMY CAVALRY: ",enemy_cav,"\n\tENEMY ARTILLERY: ",enemy_art,"\n\tENEMY TOTAL: ",final_enemy_tot)
            if final_enemy_tot != 0:
                enemy_attacker = 1
            else:
                enemy_attacker = 2

        elif enemy_attacker == 2:
            process_battle_results(final_enemy_tot,final_your_tot,enemy_attacks_game)
            enemy_attacker = 3


if __name__ == '__main__':

    # An attack has been triggered!  What would you like to do?
    trigger_one = input("Would you like to autmoatically resolve the battle [Y/N]? ")  #Simulates the game calling the function
    enemy_attacker = 1
#input("If the enemy is attacking, type '1': ")                    #Simulates if the enemy triggered the event
    enemy_attacks_game = int(enemy_attacker)

    # Battle Constants (constants without modifiers)
    cav_v_art = 3 #Every 1 cavalry can kill 3 artillery per second
    inf_v_cav = 2 #Every 1 infantry can kill 2 cavalry per second
    art_v_inf = 4 #Every 1 artillery can kill 4 infantry per second

    # Prompts user for allied inputs
    print("\n+--------------------##### ALLIED UNITS #####--------------------+\n|\t\t\t\t\t\t\t\t |")
    your_inf = input("|\tHow many infantry troops do you have? ")
    your_inf = int(your_inf)
    your_cav = input("|\tHow many cavalry troops do you have? ")
    your_cav = int(your_cav)
    your_art = input("|\tHow many artillery troops do you have? ")
    your_art = int(your_art)
    print("|\t\t\t\t\t\t\t\t |")
    print("+----------------------------------------------------------------+")
#    your_gen = input("What unit is your general? ")  #This would be where we include the rank and unit type of the general

    # Prompts user for enemy inputs
    print("\n+--------------------##### ENEMY  UNITS #####--------------------+\n|\t\t\t\t\t\t\t\t |")
    enemy_inf = input("|\tHow many infantry troops does your enemy have? ")
    enemy_inf = int(enemy_inf)
    enemy_cav = input("|\tHow many cavalry troops does your enemy have? ")
    enemy_cav = int(enemy_cav)
    enemy_art = input("|\tHow many artillery troops does your enemy have? ")
    enemy_art = int(enemy_art)
    print("|\t\t\t\t\t\t\t\t |")
    print("+----------------------------------------------------------------+")
#    enemy_gen = input("What unit is your enemy general? ")

    # Gets the starting final numbers for calculation during battle
    final_enemy_tot = enemy_inf + enemy_cav + enemy_art
    final_your_tot = your_inf + your_cav + your_art

    process_trigger_input(trigger_one,enemy_attacker,final_enemy_tot,final_your_tot,enemy_attacks_game)
