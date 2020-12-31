from umqtt.simple import MQTTClient
from machine import Pin
import machine
import ubinascii
import micropython

# Setup a GPIO Pin for output
led = Pin(12, Pin.OUT)
pin = machine.Pin(2, machine.Pin.OUT)
# Modify below section as required
CONFIG = {
# Configuration details of the MQTT broker
"MQTT_BROKER": "iot.eclipse.org",
"USER": "",
"PASSWORD": "",
"PORT": 1883,
"TOPIC": b"micro/python",
# unique identifier of the chip
"CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())
}

# Method to act based on message received
def onMessage(topic, msg):
    print("Topic: %s, Message: %s" % (topic, msg))

    if msg == b"on":
    pin.off()
    led.on()
    elif msg == b"off":
    pin.on()
    led.off()

def listen():
    #Create an instance of MQTTClient
    client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
    # Attach call back handler to be called on receiving messages
    client.set_callback(onMessage)
    client.connect()
    #client.publish("test", "ESP8266 is Connected")
    client.subscribe(CONFIG['TOPIC'])
    print("ESP8266 is Connected to %s and subscribed to %s topic" % (CONFIG['MQTT_BROKER'], CONFIG['TOPIC']))

try:
    while True:
    client.wait_msg()
    #msg = (client.check_msg())
finally:
#client.disconnect()
    client.publish("test", "ESP8266 is Connected")

listen()

    def __init__(self, client_id, server, port=0, user=None, password=None, keepalive=0,
                 ssl=False, ssl_params={}):

MQTTClient()


ssid = 'Rumpelkiste'
password = 'MiedS9876!'
mqtt_server = '172.18.0.1'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'hello'

mqtt_client_id = 

# connect to Adafruit IO MQTT broker using unsecure TCP (port 1883)
# 
# To use a secure connection (encrypted) with TLS: 
#   set MQTTClient initializer parameter to "ssl=True"
#   Caveat: a secure connection uses about 9k bytes of the heap
#         (about 1/4 of the micropython heap on the ESP8266 platform)
ADAFRUIT_IO_URL = b'io.adafruit.com' 
ADAFRUIT_USERNAME = b'<ENTER_ADAFRUIT_USERNAME>'
ADAFRUIT_IO_KEY = b'<ENTER_ADAFRUIT_IO_KEY>'
ADAFRUIT_IO_FEEDNAME = b'freeHeap'

  ```mosquitto_sub -h localhost -p 1883 -t test -u mqtt_broker_local -P hhuh9CS26Lr4yJc4```


client = MQTTClient(client_id=bytes('client_'+str(99), 'utf-8'), 
                    server=b'192.168.0.109', 
                    user=b'mqtt_broker_local', 
                    password=b'hhuh9CS26Lr4yJc4',
                    ssl=False)
