from umqtt.simple import MQTTClient
import ujson
import time
import machine
import dht

with open('config.json', 'r') as f:
    config = ujson.load(f)

client = MQTTClient(client_id=bytes(str(config['client_id']), 'utf-8'), 
                    server=bytes(config['server'], 'utf-8'), 
                    user=bytes(config['user'], 'utf-8'), 
                    password=bytes(config['password'], 'utf-8'),
                    ssl=False)
client.connect()
d = dht.DHT11(machine.Pin(2))

topic = config['topic']

while True:
    d.measure()
    client.publish(topic + '/temperature', str(d.temperature()))
    client.publish(topic + '/humidity', str(d.humidity()))
    time.sleep(3)





