import paho.mqtt.client as mqtt
import sqlite3
import subprocess
import datetime
import time

connection = sqlite3.connect('database/temperature_humidity.db', check_same_thread=False)

# Broker data
broker_port = 1883
timeout_reconnect = 60

def on_connect(client, userdata, flags, rc):
    #print("Connect with result code: " + str(rc))
    if int(str(rc)) == 0:
        print("Connection established")
    else:
        print("Error result code: " + str(rc))

def on_message(client, userdata, msg):
    if str(msg.payload):
        value = int(msg.payload.decode('utf-8'))
        if 'temperature' in msg.topic:
            target_table = 'fct_temperature'
            col_name = 'temperature'
        elif 'humidity' in msg.topic:
            target_table = 'fct_humidity'
            col_name = 'humidity'
        result_dict = {col_name: value, 'topic': msg.topic, 'receive_time': datetime.datetime.now()}
        try:
            connection.execute(f"INSERT INTO {target_table} VALUES (:topic, :receive_time, :{col_name})", result_dict)
            print("Message on: " + str(datetime.datetime.now()) + " - topic: " + msg.topic + ", payload: " + str(msg.payload))
            connection.commit()
            print("committed")
        except Exception as e:
            print(f"couldn't write message {result_dict}, error: {e}")
            

def on_publish(mosq, obj, mid):
    #print("Publish mid: " + str(mid))
    pass

def on_subscribed(mosq, obj, mid, granted_qos):
    print("Subscribed mid: " + str(mid) + ", qos: " + str(granted_qos))

def on_log(mosq, obj, mid, string):
    #print("Log: " + str(string))
    pass

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribed = on_subscribed
client.on_log = on_log
client.username_pw_set("mqtt_broker_local", "hhuh9CS26Lr4yJc4")

client.connect("192.168.0.109", 1883, 60)
client.subscribe('livingroom/computer/humidity', 0)
client.subscribe('livingroom/computer/temperature', 0)

client.loop_start()

while True:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
            break

client.disconnect()