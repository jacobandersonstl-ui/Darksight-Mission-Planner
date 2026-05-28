#Rocket Mission Planner
import os

entry_1 = {
    "name" : "Forge II Satellite",
    "organization" : "Darksight Aerospace",
    "apoapsis" : 401578,
    "periapsis" : 393285,
    "ΔV" : 435,
}

entry_2 = {
    "name" : "Forgiven II Satellite (Darksight Aerospace)",
    "organization" : "Darksight Aerospace",
    "apoapsis" : 401578,
    "periapsis" : 393285,
    "ΔV" : 435,
}

entry_3 = {
    "name" : "None",
    "apoapsis" : "?",
    "periapsis" : "?",
}

def mission_planner():
    os.system('cls')
    print("\nBooting Mission Planner")
    os.system('cls')
    print(f"-" * 38)
    print(" Darksight Aerospace Mission Planing Software")
    print(f"-" * 38)
    orbital_entry = input(f"What orbit would you like to edit? 1: {entry_1['name']} ({entry_1['organization']}); 2: {entry_2['name']}; 3: None; Choice: ")
    if orbital_entry == "1":
        orbital_selection_one()
    else:
        pass

def main():
    os.system('cls')
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
    os.system('cls')
    print(f"\nEditing orbit of {entry_1['name']}. Please wait...")
    input("\nPress Enter")
    os.system('cls')
    print("==================================================")
    print("        DARKSIGHT AEROSPACE MISSION PLANNER")
    print("==================================================\n")

    print(f"Satellite:        {entry_1['name']}")
    print(f"Organization:     {entry_1['organization']}\n")

    print(f"Apoapsis:         {entry_1['apoapsis']:,}km")
    print(f"Periapsis:        {entry_1['periapsis']:,}km")
    print(f"Delta-V:          {entry_1['ΔV']:,}m/s\n")

    print("==================================================")
    input("\nPress Enter")
    orbital_selection_one_operation()

def orbital_selection_one_operation():
    orbital_change_one = input("\nPlease make a selection based on what you want to do:\n1: Edit Apoapsis\n2: Edit Periapsis\n3: Quit\nChoice: ")
    if orbital_change_one == "1":
        os.system('cls')
        apoapsis_change = input(f"\nCurrent Apoapsis: {entry_1['apoapsis']:,}km; New Apoapsis: ")
        entry_1["apoapsis"] = int(apoapsis_change)
        orbital_selection_one()
    elif orbital_change_one == "2":
        os.system('cls')
        periapsis_change = input(f"\nCurrent Periapsis: {entry_1['periapsis']:,}km; New Periapsis: ")
        entry_1["periapsis"] = int(periapsis_change)
        orbital_selection_one()
    elif orbital_change_one == "3":
        print("\nRebooting...")
        main()

main()