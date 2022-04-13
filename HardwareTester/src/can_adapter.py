import serial

# Drive Computer Core Library
#
# Class to access the drive computer's CAN adapter
# Accepts and receives messages
#
# Part of the GSSM Autonomous Golf Cart
# Written by Joseph Telaak, class of 2022

class CAN_Adapter:

    # Constructor
    #
    # serial_port: Serial port where the Arduino CAN Adapter is located
    # baud: Arduino serial baud rate

    def __init__(self, serial_port = '/dev/ttyUSB0', baud = 11520):
        try:
            self.arduino = serial.Serial(port = serial_port, baudrate = baud, timeout = .1)

        except:
            print("FATAL: Cannot connect to the drive computer's CAN adapter")
            quit()
            

    # Return a reference to the device
    #
    # return: arduino

    def get_device(self):
        return self.arduino


    # Manually send a message to the CAN Adapter
    #
    # message: Message to send

    def send_string_to_adapter(self, message):
        self.arduino.write(message)

    # Send CAN message
    #
    # id: 32-bit CAN Bus ID
    # data: 8x 8-bit CAN Message

    def write(self, id, data):
        # Check Message Size
        if len(data) != 8:
            return

        # Format Message
        formatted_data = ""
        for dat in data:
            formatted_data += f"{dat} "

        # Send message as String
        output = f"({id}) {formatted_data}"
        self.arduino.write(f"CMD-Send: {output}")

    # Send CAN message
    def write(self, message):
        self.arduino.write(f"CMD-Send: {message}")
