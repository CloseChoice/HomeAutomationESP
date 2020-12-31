#!/bin/bash

sudo /home/tobias/anaconda3/envs/micropython/bin/ampy --port /dev/ttyUSB0 put esp_files/main.py
sudo /home/tobias/anaconda3/envs/micropython/bin/ampy --port /dev/ttyUSB0 put esp_files/config.json