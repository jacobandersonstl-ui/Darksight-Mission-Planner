#Rocket Mission Planner
import os
import math

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

earth_radius = 6371
def calculate_orbital_geometry(entry):
    r_a = entry["apoapsis"] + earth_radius
    r_p = entry["periapsis"] + earth_radius

    a = (r_a + r_p) / 2
    b = math.sqrt(r_a * r_p)
    scale = 39 / a
    return a, b, scale

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
    a1, b1, scale = calculate_orbital_geometry(entry_1)
    os.system('cls')
    print(f"\nWelcome, Engineer, to the Darksight Aerospace Mission Planner.")
    def boot_select():
        option_boot_select = input(f"\nPlease select what you would like to do: 1: Mission Planner 2: Active Missions Viewer 3: Quit; Choice: ")
        if option_boot_select == "1":
            mission_planner()
        elif option_boot_select == "2":
            mission_map_select()
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

def mission_map_select():
    os.system('cls')
    print(f"\nSatellite Orbital Map Viewer")
    print(f"\n"* 5)
    map_select = input(f"""Please select the orbit you would like a map of:
          1: {entry_1['name']}
          2: {entry_2['name']}
          3: Reboot (back)
          
          Choice: """)
    if map_select == "1":
        entry_1_map()
    elif map_select == "2":
        pass
    elif map_select == "3":
        main()

def entry_1_map():
    print(f"""
    ==================================================
           DARKSIGHT AEROSPACE MISSION PLANNER
    ==================================================

                    Orbit View

                 .-------------.
              .-'               '-.
            .'                     '.
           /           0             \\
           \\                         /
            '.                     .'
              '-.______*________.-'

    0 = Earth
    * = {entry_1['name']}
    """)
    entry_1_orbit_menu = input(f"""Menu:
          1: Change Orbit
          2: Quit""")
    if entry_1_orbit_menu == "1":
        orbital_selection_one()
    elif entry_1_orbit_menu == "2":
        main()

main()
