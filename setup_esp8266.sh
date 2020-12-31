#!/bin/bash

# take care to use the correct esptool
sudo esptool.py --port /dev/ttyUSB0 erase_flash

# deploy firmware
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20200911-v1.13.bin

