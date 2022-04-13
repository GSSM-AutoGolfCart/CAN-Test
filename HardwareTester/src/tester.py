import os
import src.util as util

def run():
    main_menu()

def clear():
    # Clear Screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Banner and Info Block
    print(util.to_color(util.title, "cyan"))
    print(util.info_block)

def main_menu():
    clear()
    print("Main Menu: ")

    print("""
        1) Steering
        2) Brakes
        3) Acceleration
        4) Accessories
        5) Misc
        6) Run in Manual Mode
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        steering()
    elif option == 2:
        brakes()
    elif option == 3:
        acclerator()
    elif option == 4:
        accessories()
    elif option == 5:
        misc()
    elif option == 6:
        manual()
    else:
        main_menu()

def steering():
    clear()
    print("Steering Menu: ")

    print("""
        1) Turn Right
        2) Turn Left
        3) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        pass
    elif option == 2:
        pass
    else:
        main_menu()

def brakes():
    clear()
    print("Brakes Menu: ")

    print("""
        1) Enagage
        2) Disengage
        3) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        pass
    elif option == 2:
        pass
    else:
        main_menu()

def acclerator():
    clear()
    print("Accelerator Menu: ")

    print("""
        1) Increment
        2) Decrement
        3) Stop
        4) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    else:
        main_menu()

def accessories():
    clear()
    print("Accessory Menu: ")

    print("""
        1) Head Lights On
        2) Head Lights Off
        3) Tail Lights On
        4) Tail Lights Off
        5) Left Signal On
        6) Left Signal Off
        7) Right Signal On
        8) Right Signal Off
        9) Rear Buzzer On
        10) Rear Buzzer Off
        11) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    else:
        main_menu()

def misc():
    clear()
    print("Misc Menu: ")

    print("""
        1) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    else:
        main_menu()

def manual():
    pass

if __name__ == "__main__":
    main_menu()