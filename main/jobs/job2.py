from django.conf import settings
from paho.mqtt import client as mqtt_client
from main.models import IoT
import random
import time
import sys
import gc
import random
import time

from paho.mqtt import client as mqtt_client


broker = "broker.hivemq.com"
topic1 = "test35941/data"
topics = ["test35941/data","test35942/data","test35943/data","test35944/data"]
client_id = f'python-mqtt-{random.randint(0, 100)}'
port = 1883
username = ""
password = ""

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = random.randint(0, 1000)
    for el in topics:
        time.sleep(1)
        if msg_count % 2 == 0:
            msg = 1
        else:
            msg = 0
        result = client.publish(el, msg_count)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg_count}` to topic `{el}`")
        else:
            print(f"Failed to send message to topic {el}")
    client.loop_stop()
    client.disconnect()
    sys.exit()


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

def scheduler_api2():
    global cut
    cut = 0
    run()
    