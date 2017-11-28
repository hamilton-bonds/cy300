import string

# Initial variables [[inf,ivalour,iarmor,iweapon,igeneral],[cav,cvalour,carmor,cweapon,cgeneral],[art,avalour,aarmor,aweapon,ageneral],[king,prince]]
your_troops = [[300,8,3,4,1],[120,1,3,1,0],[450,2,1,1,0],[870],[0,0]]
enemy_troops = [[450,3,5,5,0],[300,6,3,3,1],[120,3,3,1,0],[870],[0,0]]

inf_v_cav = 2
cav_v_art = 3
art_v_inf = 4
enemy_attacks_first = 1 #Enemy attacks first if 1

battle_constants = [inf_v_cav,cav_v_art,art_v_inf,enemy_attacks_first]

print("~~~~~~STARTING VALUES~~~~~~")
print("YOUR INFANTRY  : ",your_troops[0][0])
print("YOUR CAVALRY   : ",your_troops[1][0])
print("YOUR ARTILLERY : ",your_troops[2][0])
print("                 ------")
print("         TOTAL : ",your_troops[3][0],"\n\n")

print("ENEMY INFANTRY : ",enemy_troops[0][0])
print("ENEMY CAVALRY  : ",enemy_troops[1][0])
print("ENEMY ARTILLERY: ",enemy_troops[2][0])
print("                 ------")
print("         TOTAL : ",enemy_troops[3][0],"\n\n")

def attack_turn(your_troops,enemy_troops,battle_constants):
    your_total = your_troops[3][0]
    enemy_total = enemy_troops[3][0]
    enemy_attacks_first = battle_constants[3]

    while not ((your_total == 0) or (enemy_total == 0)):
        if enemy_attacks_first == 1:
            enemy_attack(your_troops,enemy_troops,battle_constants)
            enemy_attacks_first = 0
            your_total = your_troops[3][0]
#            show_iteration(your_troops,enemy_troops)  #Uncomment to show iterations
        else:
            friendly_attack(enemy_troops,your_troops,battle_constants)
            enemy_attacks_first = 1
            enemy_total = enemy_troops[3][0]
#            show_iteration(your_troops,enemy_troops)  #Uncomment to show iterations

    end_battle(your_troops,enemy_troops)
    

def show_iteration(your_troops,enemy_troops):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("~~~~~ITERATING  VALUES~~~~~")
    print("YOUR INFANTRY  : ",your_troops[0][0])
    print("YOUR CAVALRY   : ",your_troops[1][0])
    print("YOUR ARTILLERY : ",your_troops[2][0])
    print("                 ------")
    print("         TOTAL : ",your_troops[3][0],"\n\n")

    print("ENEMY INFANTRY : ",enemy_troops[0][0])
    print("ENEMY CAVALRY  : ",enemy_troops[1][0])
    print("ENEMY ARTILLERY: ",enemy_troops[2][0])
    print("                 ------")
    print("         TOTAL : ",enemy_troops[3][0],"\n\n")
    stub_input = input("Press any key to continue...")

def enemy_attack(your_troops,enemy_troops,battle_constants):
    your_inf = your_troops[0][0]
    your_cav = your_troops[1][0]
    your_art = your_troops[2][0]
    inf_v_cav = battle_constants[0]
    cav_v_art = battle_constants[1]
    art_v_inf = battle_constants[2]
    ivalor = enemy_troops[0][1]
    iarmor = your_troops[0][2] #your troops' armor defends
    iweapon = enemy_troops[0][3]
    igeneral = enemy_troops[0][4]
    cvalor = enemy_troops[0][1]
    carmor = your_troops[0][2] #your troops' armor defends
    cweapon = enemy_troops[0][3]
    cgeneral = enemy_troops[0][4]
    avalor = enemy_troops[0][1]
    aarmor = your_troops[0][2] #your troops' armor defends
    aweapon = enemy_troops[0][3]
    ageneral = enemy_troops[0][4]

    your_inf = (your_inf + iarmor) - art_v_inf*((1+igeneral)*ivalor*iweapon) #Use the plus armor operator
    your_cav = (your_cav + carmor) - inf_v_cav*((1+cgeneral)*cvalor*cweapon) #That prevents increasing troops
    your_art = (your_art + aarmor) - cav_v_art*((1+ageneral)*avalor*aweapon) #Try division...

    #Protects against fractions and negative numbers
    if your_inf < 1:
        your_inf = 0
    if your_cav < 1:
        your_cav = 0
    if your_art < 1:
        your_art = 0

    #Since battle always produces nice round number in this case, see below
    your_tot = your_inf + your_cav + your_art

    your_troops[0][0] = your_inf
    your_troops[1][0] = your_cav
    your_troops[2][0] = your_art
    your_troops[3][0] = your_tot

    return your_troops

def friendly_attack(enemy_troops,your_troops,battle_constants):
    enemy_inf = enemy_troops[0][0]
    enemy_cav = enemy_troops[1][0]
    enemy_art = enemy_troops[2][0]
    inf_v_cav = battle_constants[0]
    cav_v_art = battle_constants[1]
    art_v_inf = battle_constants[2]
    ivalor = your_troops[0][1]
    iarmor = enemy_troops[0][2] #enemy troops' armor defends
    iweapon = your_troops[0][3]
    igeneral = your_troops[0][4]
    cvalor = your_troops[0][1]
    carmor = enemy_troops[0][2] #enemy troops' armor defends
    cweapon = your_troops[0][3]
    cgeneral = your_troops[0][4]
    avalor = your_troops[0][1]
    aarmor = enemy_troops[0][2] #enemy troops' armor defends
    aweapon = your_troops[0][3]
    ageneral = your_troops[0][4]

    enemy_inf = (enemy_inf + iarmor) - art_v_inf*((1+igeneral)*ivalor*iweapon)
    enemy_cav = (enemy_cav + carmor) - inf_v_cav*((1+cgeneral)*cvalor*cweapon)
    enemy_art = (enemy_art + aarmor) - cav_v_art*((1+ageneral)*avalor*aweapon)

    #Protects against fractions and negative numbers
    if enemy_inf < 1:
        enemy_inf = 0
    if enemy_cav < 1:
        enemy_cav = 0
    if enemy_art < 1:
        enemy_art = 0

    #Since battle always produces nice round number in this case, see below
    enemy_tot = enemy_inf + enemy_cav + enemy_art

    enemy_troops[0][0] = enemy_inf
    enemy_troops[1][0] = enemy_cav
    enemy_troops[2][0] = enemy_art
    enemy_troops[3][0] = enemy_tot

    return enemy_troops

def end_battle(your_troops,enemy_troops):
    your_tot = your_troops[3][0]
    enemy_tot = enemy_troops[3][0]
    if (your_tot > enemy_tot) or (enemy_tot == 0):
        print("\n\nVICTORY!\n\n")
    elif (your_tot < enemy_tot) or (your_tot == 0):
        print("\n\nDEFEAT!\n\n")

    print("~~~~~~~ENDING VALUES~~~~~~~")
    print("YOUR INFANTRY  : ",your_troops[0][0])
    print("YOUR CAVALRY   : ",your_troops[1][0])
    print("YOUR ARTILLERY : ",your_troops[2][0])
    print("                 ----------")
    print("         TOTAL : ",your_troops[3][0],"\n\n")

    print("ENEMY INFANTRY : ",enemy_troops[0][0])
    print("ENEMY CAVALRY  : ",enemy_troops[1][0])
    print("ENEMY ARTILLERY: ",enemy_troops[2][0])
    print("                 ----------")
    print("         TOTAL : ",enemy_troops[3][0],"\n\n")

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
