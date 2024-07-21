import random
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topics = {
    "shift_length": "oee/shift_length",
    "breaks": "oee/breaks",
    "downtime": "oee/downtime",
    "ideal_cycle_time": "oee/ideal_cycle_time",
    "total_count": "oee/total_count",
    "reject_count": "oee/reject_count"
}
client_id = f'publish-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc, properties=None):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}\n")

    client = mqtt_client.Client(client_id=client_id, protocol=mqtt_client.MQTTv5)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def simulate_data():
    shift_length = 480  # Shift length in minutes
    breaks = 60  # Breaks in minutes
    downtime = random.randint(40, 50)  # Downtime in minutes
    ideal_cycle_time = 1.0  # Ideal cycle time in seconds
    total_count = random.randint(18800, 19500)  # Total count of widgets
    reject_count = random.randint(400, 450)  # Reject count of widgets
    return shift_length, breaks, downtime, ideal_cycle_time, total_count, reject_count

def publish(client):
    while True:
        shift_length, breaks, downtime, ideal_cycle_time, total_count, reject_count = simulate_data()
        client.publish(topics["shift_length"], shift_length)
        client.publish(topics["breaks"], breaks)
        client.publish(topics["downtime"], downtime)
        client.publish(topics["ideal_cycle_time"], ideal_cycle_time)
        client.publish(topics["total_count"], total_count)
        client.publish(topics["reject_count"], reject_count)
        print(f"Published Shift Length: {shift_length}, Breaks: {breaks}, Downtime: {downtime}, Ideal Cycle Time: {ideal_cycle_time}, Total Count: {total_count}, Reject Count: {reject_count}")
        time.sleep(10)

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
