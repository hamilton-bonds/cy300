import os

print("\t\t+------------------------------+")
print("\t\t|       PYTHON TOTAL WAR    [X]|")
print("\t\t|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("\t\t|                              |")
print("\t\t|    + [L]ow Graphics Test     |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t|                              |")
print("\t\t+------------------------------+")
menu_select = input("")
menu_is = 0

while menu_is == 0:
    if menu_select in "Ll":
        os.write("python3 main_menu.py")
        menu_is = 1
    elif menu_select in "Xx":
        print("Exiting...")
        menu_is = 1
    else:
        menu_select = input("")
        menu_is = 0
