#Rocket Mission Planner

entry_1 = {
    "name" : "Forge II Satellite (Darksight Aerospace)",
    "apoapsis" : 401578,
    "periapsis" : 393285,
}

entry_2 = {
    "name" : "Forgiven II Satellite (Darksight Aerospace)",
    "apoapsis" : 401578,
    "periapsis" : 393285,
}

entry_3 = {
    "name" : "None",
    "apoapsis" : "?",
    "periapsis" : "?",
}

def mission_planner():
    print(f"\n" * 50)
    print("\nBooting Mission Planner")
    print(f"\n" * 50)
    print(f"-" * 38)
    print(" Darksight Aerospace Mission Planing Software")
    print(f"-" * 38)
    orbital_entry = input(f"What orbit would you like to edit? 1: {entry_1['name']}; 2: {entry_2['name']}; 3: None; Choice: ")
    if orbital_entry == "1":
        orbital_selection_one()
    else:
        pass

def main():
    print(f"\nWelcome, Engineer, to the Darksight Aerospace Mission Planner.")
    def boot_select():
        option_boot_select = input(f"\nPlease select what you would like to do: 1: Mission Planner 2: Active Missions Viewer 3: Quit; Choice: ")
        if option_boot_select == "1":
            mission_planner()
        elif option_boot_select == "2":
            pass
        elif option_boot_select == "3":
            input(f"\nExiting Darksight Aerospace Mission Planner")
            quit()
        else:
            input(f"\nInvalid Input: '{option_boot_select}'")
    
    boot_select()

def orbital_selection_one():
    print(f"\n" * 50)
    print(f"\nEditing orbit of {entry_1['name']}. Please wait...")
    input("\nPress Enter")

main()