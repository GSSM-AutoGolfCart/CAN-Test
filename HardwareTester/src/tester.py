import os
import sys

import src.util as util

from src.ControlLib.ControlLib.src.can_adapter import CAN_Adapter
import src.ControlLib.ControlLib.src.raw.can_messages as msg

# Hardware Module Tester
# Main
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022


class Tester:

    # Constructor
    def __init__(self, adapter = CAN_Adapter(serial_port=sys.argv[1])) -> None:
        self.can = adapter

    # Run
    def run(self):
        self.main_menu()

    # Clear screen
    def clear(self):
        # Clear Screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Banner and Info Block
        print(util.to_color(util.title, "cyan"))
        print(util.info_block)

    # Main menu
    def main_menu(self):
        self.clear()
        print("Main Menu: ")

        print("""
            1) Direction
            2) Steering
            3) Brakes
            4) Acceleration
            5) Accessories
            6) Misc
            7) Run in Manual Mode (In-Progess)
            8) Exit
        
        """)

        try:
            option = int(input("Enter Choice: "))
        except:
            self.main_menu()

        if option == 1:
            self.direction()
        elif option == 2:
            self.steering()
        elif option == 3:
            self.brakes()
        elif option == 4:
            self.acclerator()
        elif option == 5:
            self.accessories()
        elif option == 6:
            self.misc()
        elif option == 7:
            self.manual()
        elif option == 8:
            exit(0)
        
        self.main_menu()

    # Steering menu
    def steering(self):
        self.clear()
        print("Steering Menu: ")

        print("""
            1) Turn Right
            2) Turn Left
            3) Stop Turn
            4) Start Turn
            5) Back
        
        """)

        try:
            option = int(input("Enter Choice: "))
        except:
            self.main_menu()

        if option == 1:
            self.can.write(msg.turn_right)
            self.steering()
        elif option == 2:
            self.can.write(msg.turn_left)
            self.steering()
        elif option == 3:
            self.can.write(msg.stop_turn)
            self.steering()
        elif option == 4:
            self.can.write(msg.en_turn)
            self.steering()
        
        self.main_menu()

    # Direction Menu
    def direction(self):
        self.clear()
        print("Direction Menu: ")

        print("""
            1) Forward
            2) Reverse
            3) Enable
            4) Disable
            5) Back
        
        """)

        try:
            option = int(input("Enter Choice: "))
        except:
            self.main_menu()

        if option == 1:
            self.can.write(msg.forward)
            self.direction()
        elif option == 2:
            self.can.write(msg.reverse)
            self.direction()
        elif option == 3:
            self.can.write(msg.enable)
            self.direction()
        elif option == 4:
            self.can.write(msg.disable)
            self.direction()
        
        self.main_menu()

    # Brakes menu
    def brakes(self):
        self.clear()
        print("Brakes Menu: ")

        print("""
            1) Pull
            2) Release
            3) Disable
            4) Enable
            5) Back
        
        """)

        try:
            option = int(input("Enter Choice: "))
        except:
            self.main_menu()

        if option == 1:
            self.can.write(msg.pull_brakes)
            self.brakes()
        elif option == 2:
            self.can.write(msg.release_brakes)
            self.brakes()
        elif option == 3:
            self.can.write(msg.disable_brakes)
            self.brakes()
        elif option == 4:
            self.can.write(msg.enable_brakes)
            self.brakes()
        
        self.main_menu()

    # Accelerator menu
    def acclerator(self):
        self.clear()
        print("Accelerator Menu: ")

        print("""
            1) Increment
            2) Decrement
            3) Stop
            4) Back
        
        """)

        try:
            option = int(input("Enter Choice: "))
        except:
            self.main_menu()

        if option == 1:
            self.can.write(msg.accelerate)
            self.acclerator()
        elif option == 2:
            self.can.write(msg.deccelerate)
            self.acclerator()
        elif option == 3:
            self.can.write(msg.stop_accel)
            self.acclerator()
        
        self.main_menu()

    # Accessory menu
    def accessories(self):
        self.clear()
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

        try:
            option = int(input("Enter Choice: "))
        except:
            self.main_menu()

        if option == 1:
            self.can.write(msg.head_on)
            self.accessories()
        elif option == 2:
            self.can.write(msg.head_off)
            self.accessories()
        elif option == 3:
            self.can.write(msg.tail_on)
            self.accessories()
        elif option == 4:
            self.can.write(msg.tail_off)
            self.accessories()
        elif option == 5:
            self.can.write(msg.left_signal_on)
            self.accessories()
        elif option == 6:
            self.can.write(msg.left_signal_off)
            self.accessories()
        elif option == 7:
            self.can.write(msg.right_signal_on)
            self.accessories()
        elif option == 8:
            self.can.write(msg.right_signal_off)
            self.accessories()
        elif option == 9:
            self.can.write(msg.rear_buzz_on)
            self.accessories()
        elif option == 10:
            self.can.write(msg.rear_buzz_off)
            self.accessories()
        elif option == 11:
            self.can.write(msg.honk)
            self.accessories()
        
        self.main_menu()

    # Misc menu
    def misc(self):
        self.clear()
        print("Misc Menu: ")

        print("""
            1) Back
        
        """)

        try:
            option = int(input("Enter Choice: "))
        except:
            self.main_menu()

        if option == 1:
            pass
        
        self.main_menu()

    # Manual mode operation
    def manual(self):
        self.main_menu()