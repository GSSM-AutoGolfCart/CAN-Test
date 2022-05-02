# This installs the required dependencies without pip
# Arose from a lack of working ssl on the Jetson

cd /tmp

# PySerial 3.3
git clone https://github.com/pyserial/pyserial/
cd pyserial
git checkout 1c4bc81 # Release 3.3
sudo python3.7 setup.py install
cd ..

# PyFiglet
git clone https://github.com/pwaller/pyfiglet
cd pyfiglet
git checkout d7079e9 # Working version
sudo python3.7 setup.py install