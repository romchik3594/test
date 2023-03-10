from django.shortcuts import render
from main.models import IoT
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from paho.mqtt import client as mqtt_client
import random
from var_dump import var_dump

#mqtt response
#
#
def connect_mqtt():
    broker = "broker.hivemq.com"
    client_id = f'python-mqtt-{random.randint(0, 100)}'
    port = 1883
    username = ""
    password = ""
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


def publish(client, value, topic):
    msg = value
    result = client.publish(topic, value)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{value}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    client.loop_stop()
    client.disconnect()


def run(value, topic):
    client = connect_mqtt()
    client.loop_start()
    publish(client, value, topic)
# end mqtt block
#
#
def index(request):
    db = IoT.objects.get(id=1)
    return render(request,'main/index.html',{'db':db})
def somepage(request):
    return render(request,'main/somepage.html')
@csrf_exempt
def update1(request):
    db = IoT.objects.get(id=1)
    return HttpResponse(db.gas)
@csrf_exempt
def update2(request):
    db = IoT.objects.get(id=1)
    return HttpResponse(db.liq)
@csrf_exempt
def update3(request):
    db = IoT.objects.get(id=1)
    return HttpResponse(db.punch)
@csrf_exempt
def update4(request):
    db = IoT.objects.get(id=1)
    return HttpResponse(db.tempre)
    
