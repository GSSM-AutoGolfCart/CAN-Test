import os
import sys

import src.util as util
import src.can.can_messages as msg
from src.can_adapter import CAN_Adapter

# Hardware Module Tester
# Main
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

# CAN Adapter
can = CAN_Adapter(serial_port=str(sys.argv[1]), baud=11520)

# Run
def run():
    main_menu()

# Clear screen
def clear():
    # Clear Screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Banner and Info Block
    print(util.to_color(util.title, "cyan"))
    print(util.info_block)

# Main menu
def main_menu():
    clear()
    print("Main Menu: ")

    print("""
        1) Direction
        2) Steering
        3) Brakes
        4) Acceleration
        5) Accessories
        6) Misc
        7) Run in Manual Mode
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        direction()
    elif option == 2:
        steering()
    elif option == 3:
        brakes()
    elif option == 4:
        acclerator()
    elif option == 5:
        accessories()
    elif option == 6:
        misc()
    elif option == 7:
        manual()
    else:
        main_menu()

# Steering menu
def steering():
    clear()
    print("Steering Menu: ")

    print("""
        1) Turn Right
        2) Turn Left
        3) Stop Turn
        4) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        can.write(msg.turn_right)
    elif option == 2:
        can.write(msg.turn_left)
    elif option == 3:
        can.write(msg.stop_turn)
    else:
        main_menu()

# Direction Menu
def direction():
    clear()
    print("Direction Menu: ")

    print("""
        1) Forward
        2) Reverse
        3) Enable
        4) Disable
        5) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        can.write(msg.forward)
    elif option == 2:
        can.write(msg.reverse)
    elif option == 3:
        can.write(msg.enable)
    elif option == 4:
        can.write(msg.disable)
    else:
        main_menu()

# Brakes menu
def brakes():
    clear()
    print("Brakes Menu: ")

    print("""
        1) Pull
        2) Release
        3) Disable
        4) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        can.write(msg.pull_brakes)
    elif option == 2:
        can.write(msg.release_brakes)
    elif option == 3:
        can.write(msg.disable_brakes)
    else:
        main_menu()

# Accelerator menu
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
        can.write(msg.accelerate)
    elif option == 2:
        can.write(msg.deccelerate)
    elif option == 3:
        can.write(msg.stop_accel)
    else:
        main_menu()

# Accessory menu
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
        11) Honk
        12) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        can.write(msg.head_on)
    elif option == 2:
        can.write(msg.head_off)
    elif option == 3:
        can.write(msg.tail_on)
    elif option == 4:
        can.write(msg.tail_off)
    elif option == 5:
        can.write(msg.left_signal_on)
    elif option == 6:
        can.write(msg.left_signal_off)
    elif option == 7:
        can.write(msg.right_signal_on)
    elif option == 8:
        can.write(msg.right_signal_off)
    elif option == 9:
        can.write(msg.rear_buzz_on)
    elif option == 10:
        can.write(msg.rear_buzz_off)
    elif option == 11:
        can.write(msg.honk)
    else:
        main_menu()

# Misc menu
def misc():
    clear()
    print("Misc Menu: ")

    print("""
        1) Back
    
    """)

    option = int(input("Enter Choice: "))

    if option == 1:
        pass
    else:
        main_menu()

# Manual mode operation
def manual():
    pass