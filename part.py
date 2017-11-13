# This is the simple logic for our game
# PYTHON TOTAL WAR
# 
# by CDTs Bonds, Ferguson, and Loe
# Dr. Cook's H5 Section for CY300
# 
# This game will function much like
# Microsoft Games' Medieval Total War
# 
# Player info:  [players,player_name,faction,difficulty,time_period]

def main_menu():
    menu_select = ""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("+________________________+")
    print("|    PYTHON TOTAL WAR    |")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|   +[S]ingle Player     |")
    print("|                        |")
    print("|   +[G]ames Saved       |")
    print("|                        |")
    print("|   +[E]xit Game         |")
    print("|________________________|")
    print("+                        +")
    menu_select = input("")
    if menu_select in "Ss":
        single_player()
    elif menu_select in "Gg":
        saved_games()
    elif menu_select in "Ee":
        print("EXITING GAME...")
    else:
        main_menu()

def single_player():
    players = 1
    name_loop = 1
    player_name = ""
    while name_loop == 1:
        if len(player_name) == 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+________________________+")
            print("|     Single  Player     |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|   +Name [<9 chars]     |")
            print("|                        |")
            print("|     [_       ]         |")
            print("|                        |")
            print("|    [`]=Clear [#]=Done  |")
            print("|________________________|")
            print("+                        +")
            player_add = input("")
            if player_add in "`":
                player_name = ""
                player_add = ""
            elif player_add == "#":
                print("Are you sure you want to be named ",player_name,"[Enter]?")
                confirm = input("")
                if confirm == "":
                    player_name = player_name
                    name_loop = 0
                elif confirm != "":
                    player_name = ""
                    player_add = ""
            player_name = player_name + player_add
        elif len(player_name) == 1:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+________________________+")
            print("|     Single  Player     |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|   +Name [<9 chars]     |")
            print("|                        |")
            print("|     [",player_name,"_      ]       |")
            print("|                        |")
            print("|    [`]=Clear [#]=Done  |")
            print("|________________________|")
            print("+                        +")
            player_add = input("")
            if player_add in "`":
                player_name = ""
                player_add = ""
            elif player_add == "#":
                print("Are you sure you want to be named ",player_name,"[Enter]?")
                confirm = input("")
                if confirm == "":
                    player_name = player_name
                    name_loop = 0
                elif confirm != "":
                    player_name = ""
                    player_add = ""
            player_name = player_name + player_add
        elif len(player_name) == 2:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+________________________+")
            print("|     Single  Player     |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|   +Name [<9 chars]     |")
            print("|                        |")
            print("|     [",player_name,"_     ]       |")
            print("|                        |")
            print("|    [`]=Clear [#]=Done  |")
            print("|________________________|")
            print("+                        +")
            player_add = input("")
            if player_add in "`":
                player_name = ""
                player_add = ""
            elif player_add == "#":
                print("Are you sure you want to be named ",player_name,"[Enter]?")
                confirm = input("")
                if confirm == "":
                    player_name = player_name
                    name_loop = 0
                elif confirm != "":
                    player_name = ""
                    player_add = ""
            player_name = player_name + player_add
        elif len(player_name) == 3:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+________________________+")
            print("|     Single  Player     |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|   +Name [<9 chars]     |")
            print("|                        |")
            print("|     [",player_name,"_    ]       |")
            print("|                        |")
            print("|    [`]=Clear [#]=Done  |")
            print("|________________________|")
            print("+                        +")
            player_add = input("")
            if player_add in "`":
                player_name = ""
                player_add = ""
            elif player_add == "#":
                print("Are you sure you want to be named ",player_name,"[Enter]?")
                confirm = input("")
                if confirm == "":
                    player_name = player_name
                    name_loop = 0
                elif confirm != "":
                    player_name = ""
                    player_add = ""
            player_name = player_name + player_add
        elif len(player_name) == 4:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+________________________+")
            print("|     Single  Player     |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|   +Name [<9 chars]     |")
            print("|                        |")
            print("|     [",player_name,"_   ]       |")
            print("|                        |")
            print("|    [`]=Clear [#]=Done  |")
            print("|________________________|")
            print("+                        +")
            player_add = input("")
            if player_add in "`":
                player_name = ""
                player_add = ""
            elif player_add == "#":
                print("Are you sure you want to be named ",player_name,"[Enter]?")
                confirm = input("")
                if confirm == "":
                    player_name = player_name
                    name_loop = 0
                elif confirm != "":
                    player_name = ""
                    player_add = ""
            player_name = player_name + player_add
        elif len(player_name) == 5:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+________________________+")
            print("|     Single  Player     |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|   +Name [<9 chars]     |")
            print("|                        |")
            print("|     [",player_name,"_  ]       |")
            print("|                        |")
            print("|    [`]=Clear [#]=Done  |")
            print("|________________________|")
            print("+                        +")
            player_add = input("")
            if player_add in "`":
                player_name = ""
                player_add = ""
            elif player_add == "#":
                print("Are you sure you want to be named ",player_name,"[Enter]?")
                confirm = input("")
                if confirm == "":
                    player_name = player_name
                    name_loop = 0
                elif confirm != "":
                    player_name = ""
                    player_add = ""
            player_name = player_name + player_add
        elif len(player_name) == 6:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+________________________+")
            print("|     Single  Player     |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|   +Name [<9 chars]     |")
            print("|                        |")
            print("|     [",player_name,"_ ]       |")
            print("|                        |")
            print("|    [`]=Clear [#]=Done  |")
            print("|________________________|")
            print("+                        +")
            player_add = input("")
            if player_add in "`":
                player_name = ""
                player_add = ""
            elif player_add == "#":
                print("Are you sure you want to be named ",player_name,"[Enter]?")
                confirm = input("")
                if confirm == "":
                    player_name = player_name
                    name_loop = 0
                elif confirm != "":
                    player_name = ""
                    player_add = ""
            player_name = player_name + player_add
        elif len(player_name) == 7:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+________________________+")
            print("|     Single  Player     |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|   +Name [<9 chars]     |")
            print("|                        |")
            print("|     [",player_name,"_]       |")
            print("|                        |")
            print("|    [`]=Clear [#]=Done  |")
            print("|________________________|")
            print("+                        +")
            player_add = input("")
            if player_add in "`":
                player_name = ""
                player_add = ""
            elif player_add == "#":
                print("Are you sure you want to be named ",player_name,"[Enter]?")
                confirm = input("")
                if confirm == "":
                    player_name = player_name
                    name_loop = 0
                elif confirm != "":
                    player_name = ""
                    player_add = ""
            player_name = player_name + player_add
        elif len(player_name) == 8:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+________________________+")
            print("|     Single  Player     |")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|   +Name [<9 chars]     |")
            print("|                        |")
            print("|     [",player_name,"]       |")
            print("|                        |")
            print("|    [`]=Clear [#]=Done  |")
            print("|________________________|")
            print("+                        +")
            player_add = input("")
            if player_add in "`":
                player_name = ""
                player_add = ""
            elif player_add == "#":
                print("Are you sure you want to be named ",player_name,"[Enter]?")
                confirm = input("")
                if confirm == "":
                    player_name = player_name
                    name_loop = 0
                elif confirm != "":
                    player_name = ""
                    player_add = ""
            player_name = player_name + player_add

    player_str = ""
    for char in player_name:
        if char == "#":
            char = ""
        elif char != "#":
            player_str = player_str + char

    game_options = [players,player_str]
    faction_select(game_options)

def faction_select(game_options):
    menu_select = ""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("+________________________+")
    print("|   Faction  Selection   |")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|   +[E]nglish           |")
    print("|                        |")
    print("|   +[F]rench            |")
    print("|                        |")
    print("|   +[G]ermans           |")
    print("|________________________|")
    print("+                        +")
    menu_select = input("")
    if menu_select in "Ee":
        faction = "English"
        game_options.append(faction)
        game_settings(game_options)
    elif menu_select in "Ff":
        faction = "French"
        game_options.append(faction)
        game_settings(game_options)
    elif menu_select in "Gg":
        faction = "Germans"
        game_options.append(faction)
        game_settings(game_options)
    else:
        faction_select(game_options)

def game_settings(game_options):
    menu_select = ""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("+________________________+")
    print("|     Game  Settings     |")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|   +[E]asy              |")
    print("|                        |")
    print("|   +[M]edium            |")
    print("|                        |")
    print("|   +[H]ard              |")
    print("|________________________|")
    print("+                        +")
    menu_select = input("")
    if menu_select in "Ee":
        difficulty = "Easy"
        game_options.append(difficulty)
        time_period(game_options)
    elif menu_select in "Mm":
        difficulty = "Medium"
        game_options.append(difficulty)
        time_period(game_options)
    elif menu_select in "Hh":
        difficulty = "Hard"
        game_options.append(difficulty)
        time_period(game_options)
    else:
        game_settings(game_options)

def time_period(game_options):
    menu_select = ""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("+________________________+")
    print("|      Time  Period      |")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|   +[E]arly             |")
    print("|                        |")
    print("|   +[M]iddle            |")
    print("|                        |")
    print("|   +[L]ate              |")
    print("|________________________|")
    print("+                        +")
    menu_select = input("")
    if menu_select in "Ee":
        time_period = "Early"
        game_options.append(time_period)
        initialization(game_options)
    elif menu_select in "Mm":
        time_period = "Middle"
        game_options.append(time_period)
        initialization(game_options)
    elif menu_select in "Ll":
        time_period = "Late"
        game_options.append(time_period)
        initialization(game_options)
    else:
        time_period(game_options)

def initialization(game_options):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Players     : ",game_options[0])
    print("Player Name : ",game_options[1])
    print("Faction     : ",game_options[2])
    print("Difficulty  : ",game_options[3])
    print("Time Period : ",game_options[4])
    players = str(game_options[0])
    difficulty = str(game_options[3])
    time_period = str(game_options[4])
    game_setting = (players,difficulty,time_period)

    if game_setting[0] == 1 and game_setting[1] == "Easy" and game_setting[2] == "Early":
        print("Initializing a Single Player ",difficulty," Map in the ",time_period," Period.")
    elif game_setting[0] == 1 and game_setting[1] == "Easy" and game_setting[2] == "Middle":
        print("Initializing a Single Player ",difficulty," Map in the ",time_period," Period.")
    elif game_setting[0] == 1 and game_setting[1] == "Easy" and game_setting[2] == "Late":
        print("Initializing a Single Player ",difficulty," Map in the ",time_period," Period.")
    elif game_setting[0] == 1 and game_setting[1] == "Medium" and game_setting[2] == "Early":
        print("Initializing a Single Player ",difficulty," Map in the ",time_period," Period.")
    elif game_setting[0] == 1 and game_setting[1] == "Medium" and game_setting[2] == "Middle":
        print("Initializing a Single Player ",difficulty," Map in the ",time_period," Period.")
    elif game_setting[0] == 1 and game_setting[1] == "Medium" and game_setting[2] == "Late":
        print("Initializing a Single Player ",difficulty," Map in the ",time_period," Period.")
    elif game_setting[0] == 1 and game_setting[1] == "Hard" and game_setting[2] == "Early":
        print("Initializing a Single Player ",difficulty," Map in the ",time_period," Period.")
    elif game_setting[0] == 1 and game_setting[1] == "Hard" and game_setting[2] == "Middle":
        print("Initializing a Single Player ",difficulty," Map in the ",time_period," Period.")
    elif game_setting[0] == 1 and game_setting[1] == "Hard" and game_setting[2] == "Late":
        print("Initializing a Single Player ",difficulty," Map in the ",time_period," Period.")

#INSERT LOAD MAP AND OBJECTS FUNCTION HERE



##################################################################
if __name__ == '__main__':
    main_menu()
