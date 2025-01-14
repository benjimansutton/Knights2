import random

# Call for this when you want to create a new knight
def create_knight(knights):
    print("Let's create a knight!")
    knight_name = input("What is the knight's name: ")
    knights_data = [knight_name]
    knights.append(knights_data)

# Call for this when you want to create a new weapon
def create_weapon(weapons):
    print("Let's create a weapon!")
    weapon_name = input("What is the weapon: ")
    weapons_data = [weapon_name]
    weapons.append(weapons_data)

# Call a knight and change their data
def change_knight_data(knights):
    print("--- What would you like to update? ---")
    print(f"1: Knight's name: {knights[0][0]}")
    selection = input("Select your option: ")
    try:
        selection = int(selection)
        if selection == 1:
            new_name = input("What is their new name: ")
            knights[0][0] = new_name
            print(f"Your knight's new name is: {new_name}")
        else:
            print("--- Please select a valid option ---")
    except:
        print("--- Try Again! ---")
        change_knight_data(knights)

# Call a weapon and change its data
def change_weapon_data(weapons):
    print("--- What would you like to update? ---")
    print(f"1: Weapon's name: {weapons[0][0]}")
    selection = input("Select your option: ")
    try:
        selection = int(selection)
        if selection == 1:
            new_name = input("What is the new weapon name: ")
            weapons[0][0] = new_name
            print(f"Your weapon's new name is: {new_name}")
        else:
            print("--- Please select a valid option ---")
    except:
        print("--- Try Again! ---")
        change_weapon_data(weapons)

# Show the current knights and select one
def select_knight(knights):
    if len(knights) == 0:
        print("You need to create a knight first!! \n")
    else:
        print("What knight would you like to update?\n")
        for index, knight in enumerate(knights):
            print(f"{index + 1} - Knight's name: {knight[0]}")
        selection = input("\nSelect the knight's number: ")
        try:
            selection = int(selection) - 1
            change_knight_data(knights[selection])
        except:
            print("--- Try Again! ---")
            select_knight(knights)

# Show the current weapon and update it
def select_weapon(weapons):
    if len(weapons) == 0:
        print("You need to create a weapon first!! \n")
    else:
        change_weapon_data(weapons)

# This is the menu and we make our selections here
def menu(knights, weapons):
    while True:
        # Print the display options
        print("What do you want to do?")
        print("1: Create a new knight")
        print("2: Update your knight")
        print("3: Create a new weapon")
