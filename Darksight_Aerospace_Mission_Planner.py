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
        orbital_selection_two()

def main():
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
            main()
    
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
    orbital_selection_one_operation()

def orbital_selection_one_operation():
    orbital_change_one = input("\nPlease make a selection based on what you want to do:\n1: Edit Apoapsis\n2: Edit Periapsis\n3: Go to Map View\n4: Reboot (Back)\nChoice: ")
    if orbital_change_one == "1":
        os.system('cls')
        apoapsis_change = input(f"\nCurrent Apoapsis: {entry_1['apoapsis']:,}km; New Apoapsis: ")
        try:
            entry_1["apoapsis"] = int(apoapsis_change)
        except ValueError:
            input(f"Invalid Apoapsis Value. Press Enter")
            orbital_selection_one()
            return
        orbital_selection_one()
    elif orbital_change_one == "2":
        os.system('cls')
        periapsis_change = input(f"\nCurrent Periapsis: {entry_1['periapsis']:,}km; New Periapsis: ")
        try:
            entry_1["periapsis"] = int(periapsis_change)
        except ValueError:
            input(f"Invalid Periapsis Value. Press Enter")
            orbital_selection_one()
            return
        orbital_selection_one()
    elif orbital_change_one == "3":
        entry_1_map()
    elif orbital_change_one == "4":
        print("\nRebooting...")
        main()
    else:
        input(f"Invalid Input '{orbital_change_one}'")
        orbital_selection_one()

def orbital_selection_two():
    os.system('cls')
    print(f"\nEditing orbit of {entry_2['name']}. Please wait...")
    input("\nPress Enter")
    os.system('cls')
    print("==================================================")
    print("        DARKSIGHT AEROSPACE MISSION PLANNER")
    print("==================================================\n")

    print(f"Satellite:        {entry_2['name']}")
    print(f"Organization:     {entry_2['organization']}\n")

    print(f"Apoapsis:         {entry_2['apoapsis']:,}km")
    print(f"Periapsis:        {entry_2['periapsis']:,}km")
    print(f"Delta-V:          {entry_2['ΔV']:,}m/s\n")

    print("==================================================")
    orbital_selection_two_operation()

def orbital_selection_two_operation():
    orbital_change_two = input("\nPlease make a selection based on what you want to do:\n1: Edit Apoapsis\n2: Edit Periapsis\n3: Reboot (Back)\nChoice: ")
    if orbital_change_two == "1":
        os.system('cls')
        apoapsis_change = input(f"\nCurrent Apoapsis: {entry_2['apoapsis']:,}km; New Apoapsis: ")
        try:
            entry_2["apoapsis"] = int(apoapsis_change)
        except ValueError:
            input(f"Invalid Apoapsis Value. Press Enter")
            orbital_selection_two()
            return
        orbital_selection_two()
    elif orbital_change_two == "2":
        os.system('cls')
        periapsis_change = input(f"\nCurrent Periapsis: {entry_2['periapsis']:,}km; New Periapsis: ")
        try:
            entry_2["periapsis"] = int(periapsis_change)
        except ValueError:
            input(f"Invalid Periapsis Value. Press Enter")
            orbital_selection_two()
            return
        orbital_selection_two()
    elif orbital_change_two == "3":
        entry_2_map()
    elif orbital_change_two == "4":
        print("\nRebooting...")
        main()
    else:
        input(f"Invalid Input '{orbital_change_two}'")
        orbital_selection_two()


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
        entry_2_map()
    elif map_select == "3":
        main()
    else:
        input(f"Invalid Input '{map_select}'. Press Enter")
        mission_map_select()

def entry_1_map():
    os.system('cls')
    print(f"""
    ==================================================
           DARKSIGHT AEROSPACE MISSION PLANNER
    ==================================================

                    Orbit View""")
    draw_map(entry_1)
    print(f"""\n
    0 = Earth
    * = {entry_1['name']}
    """)
    entry_1_orbit_menu = input(f"""Menu:
          1: Change Orbit
          2: Quit
                               
          Choice: """)
    if entry_1_orbit_menu == "1":
        orbital_selection_one()
    elif entry_1_orbit_menu == "2":
        main()
    else:
        input(f"\nInvalid Input '{entry_1_orbit_menu}'. Press Enter")
        entry_1_map()

def entry_2_map():
    os.system('cls')
    print(f"""
    ==================================================
           DARKSIGHT AEROSPACE MISSION PLANNER
    ==================================================

                    Orbit View""")
    draw_map(entry_2)
    print(f"""\n
    0 = Earth
    * = {entry_2['name']}
    """)
    entry_2_orbit_menu = input(f"""Menu:
          1: Change Orbit
          2: Quit
                               
          Choice: """)
    if entry_2_orbit_menu == "1":
        orbital_selection_two()
    elif entry_2_orbit_menu == "2":
        main()
    else:
        input(f"\nInvalid Input '{entry_2_orbit_menu}'. Press Enter")
        entry_2_map()

def draw_map(entry):
    a, b, scale = calculate_orbital_geometry(entry)
    width, height = 79, 39
    a, b, scale = calculate_orbital_geometry(entry)
    a_s = a * scale
    b_s = b * scale * 0.5  # 0.5 because terminal chars are taller than wide
    
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    cx, cy = width // 2, height // 2
    grid[cy][cx] = '0'  # Earth
    
    for y in range(height):
        for x in range(width):
            dx = x - cx
            dy = y - cy
            val = (dx/a_s)**2 + (dy/b_s)**2
            if abs(val - 1) < 0.15:
                grid[y][x] = '*'
    
    for row in grid:
        print(''.join(row))

main()
