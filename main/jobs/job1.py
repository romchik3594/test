from django.conf import settings
from paho.mqtt import client as mqtt_client
from main.models import IoT
import random
import time
import sys
import gc
broker = "broker.hivemq.com"
topic = "test35941/data"
client_id = f'python-mqtt-{random.randint(0, 100)}'
port = 1883
username = ""
password = ""

def connect_mqtt() -> mqtt_client:
    
    
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            global cut
            cut = cut + 1
            if cut > 1:
                client.loop_stop()
                sys._clear_type_cache()
                gc.enable()
                client.disconnect()
                sys.exit()
                
            
        else:
            print("Failed to connect, return code %d\n", rc)
    global cut
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port, keepalive=5)
    if cut > 1:
        client.loop_stop()
        client.disconnect()
        gc.enable()
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        model_instance = IoT.objects.get(id=1)
        model_instance.gas = msg.payload.decode()
        model_instance.save()
        #sys.exit()
        client.loop_stop()

    client.subscribe(topic)
    client.on_message = on_message
    client.loop_stop()


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    

def scheduler_api():
    global cut
    cut = 0
    run()
    