# Hardware Module Tester
# Serial Monitor
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

# Serial Port
$tty_port = "/dev/ttyACM0"

# Print STD Program Header
python3.7 HardwareTester/src/util.py

# Print serial output
stty -F $tty_port raw 115200
cat $tty_port