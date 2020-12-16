import threading
import paho.mqtt.client as mqtt
import json


class ClientTV:
    def __init__(self):
        self.client = mqtt.Client("tv")
        self.client.connect(host="dojot.atlantico.com.br", port=1883)
        self.client.on_message = self.callback
        self.status = False

    def publish_to_dojot(self, data):
        data["from"] = "tv"
        data["to"] = "smp"
        self.client.publish("/gesad/434339/attrs", payload=json.dumps(data))

    def subscribe(self):
        self.client.subscribe("/gesad/f0bf6d/attrs")

    def callback(self, msg):
        body = json.loads(msg.payload)
        data = {'msg': ''}
        if self.status = 'unlocked': 
            data['msg'] = 'TV is unlocked'
        
        elif self.status = 'locked': 
            data['msg'] = 'TV is locked'

        self.publish_to_dojot(data)
