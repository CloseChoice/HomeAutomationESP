Wichtig ist, ein Passwortfile einzurichten, mit Username und PW

#todo: find a solution for the sudo mess!!!!

How to connect to the device getting a Python REPL
```sudo picocom /dev/ttyUSB0 -b115200```
or
```sudo screen /dev/ttyUSB0 115200```

You create this with: 
 - sudo mosquitto_passwd -c /etc/mosquitto/passwd <user_name>


 After doing so, mosquitto runs with:
  - run ```sudo mosquitto -c /etc/mosquitto/mosquitto.conf```

  - Subscribe with
  ```mosquitto_sub -h localhost -p 1883 -t test -u mqtt_broker_local -P <mqtt_broker_pw>```
  - Publish with 
  ```mosquitto_pub -h localhost -p 1883 -t test -u mqtt_broker_local -P <mqtt_broker_pw> -m "Hello again"```

get more information at: http://chrigi.me/wordpress/mqtt-broker-auf-raspberry-installieren/

Run code from computer on ESP8266:
```sudo /home/tobias/anaconda3/envs/micropython/bin/ampy --port /dev/ttyUSB0 run measure_temp.py```

Put code from computer on ESP8266:
```sudo /home/tobias/anaconda3/envs/micropython/bin/ampy --port /dev/ttyUSB0 put main.py```
