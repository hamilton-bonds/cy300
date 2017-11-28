import string

# Initial variables [inf,cav,art]
your_troops = [450,300,120,870]
enemy_troops = [700,120,50,870]

inf_v_cav = 2
cav_v_art = 3
art_v_inf = 4
enemy_attacks_first = 1 #Enemy attacks first if 1

battle_constants = [inf_v_cav,cav_v_art,art_v_inf,enemy_attacks_first]

print("~~~~~~STARTING VALUES~~~~~~")
print("YOUR INFANTRY  : ",your_troops[0])
print("YOUR CAVALRY   : ",your_troops[1])
print("YOUR ARTILLERY : ",your_troops[2])
print("                 ------")
print("         TOTAL : ",your_troops[3],"\n\n")

print("ENEMY INFANTRY : ",enemy_troops[0])
print("ENEMY CAVALRY  : ",enemy_troops[1])
print("ENEMY ARTILLERY: ",enemy_troops[2])
print("                 ------")
print("         TOTAL : ",enemy_troops[3],"\n\n")

def attack_turn(your_troops,enemy_troops,battle_constants):
    your_total = your_troops[3]
    enemy_total = enemy_troops[3]
    enemy_attacks_first = battle_constants[3]

    while not ((your_total == 0) or (enemy_total == 0)):
        if enemy_attacks_first == 1:
            enemy_attack(your_troops,battle_constants)
            enemy_attacks_first = 0
            your_total = your_troops[3]
        else:
            friendly_attack(enemy_troops,battle_constants)
            enemy_attacks_first = 1
            enemy_total = enemy_troops[3]

    end_battle(your_troops,enemy_troops)
    

def enemy_attack(your_troops,battle_constants):
    your_inf = your_troops[0]
    your_cav = your_troops[1]
    your_art = your_troops[2]
    inf_v_cav = battle_constants[0]
    cav_v_art = battle_constants[1]
    art_v_inf = battle_constants[2]

    your_inf = your_inf - art_v_inf
    your_cav = your_cav - inf_v_cav
    your_art = your_art - cav_v_art

    #Protects against fractions and negative numbers
    if your_inf < 1:
        your_inf = 0
    if your_cav < 1:
        your_cav = 0
    if your_art < 1:
        your_art = 0

    #Since battle always produces nice round number in this case, see below
    your_tot = your_inf + your_cav + your_art

    your_troops[0] = your_inf
    your_troops[1] = your_cav
    your_troops[2] = your_art
    your_troops[3] = your_tot

    return your_troops

def friendly_attack(enemy_troops,battle_constants):
    enemy_inf = enemy_troops[0]
    enemy_cav = enemy_troops[1]
    enemy_art = enemy_troops[2]
    inf_v_cav = battle_constants[0]
    cav_v_art = battle_constants[1]
    art_v_inf = battle_constants[2]

    enemy_inf = enemy_inf - art_v_inf
    enemy_cav = enemy_cav - inf_v_cav
    enemy_art = enemy_art - cav_v_art

    #Protects against fractions and negative numbers
    if enemy_inf < 1:
        enemy_inf = 0
    if enemy_cav < 1:
        enemy_cav = 0
    if enemy_art < 1:
        enemy_art = 0

    #Since battle always produces nice round number in this case, see below
    enemy_tot = enemy_inf + enemy_cav + enemy_art

    enemy_troops[0] = enemy_inf
    enemy_troops[1] = enemy_cav
    enemy_troops[2] = enemy_art
    enemy_troops[3] = enemy_tot

    return enemy_troops

def end_battle(your_troops,enemy_troops):
    your_tot = your_troops[3]
    enemy_tot = enemy_troops[3]
    if (your_tot > enemy_tot) or (enemy_tot == 0):
        print("\n\nVICTORY!\n\n")
    elif (your_tot < enemy_tot) or (your_tot == 0):
        print("\n\nDEFEAT!\n\n")

    print("~~~~~~~ENDING VALUES~~~~~~~")
    print("YOUR INFANTRY  : ",your_troops[0])
    print("YOUR CAVALRY   : ",your_troops[1])
    print("YOUR ARTILLERY : ",your_troops[2])
    print("                 ----------")
    print("         TOTAL : ",your_troops[3],"\n\n")

    print("ENEMY INFANTRY : ",enemy_troops[0])
    print("ENEMY CAVALRY  : ",enemy_troops[1])
    print("ENEMY ARTILLERY: ",enemy_troops[2])
    print("                 ----------")
    print("         TOTAL : ",enemy_troops[3],"\n\n")

if __name__ == '__main__':
    question = input("Would you like to automatically resolve the battle? ")
    qmod = question.lower()
    pos = ("yes","y")
    neg = ("no","n")

    if qmod in pos:
        attack_turn(your_troops,enemy_troops,battle_constants) #battle
    elif qmod in neg:
        print("EXITING...")
    else:
        print("ERROR")
