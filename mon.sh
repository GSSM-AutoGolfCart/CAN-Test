# Hardware Module Tester
# Serial Monitor
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

# Print STD Program Header
python3.7 HardwareTester/src/util.py

# Print serial output
stty -F "/dev/ttyACM0" raw 115200
cat "/dev/ttyACM0"