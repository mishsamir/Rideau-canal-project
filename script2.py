import time
import random
import json
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message
import os

CONNECTION_STRING = "HostName=finalassignment.azure-devices.net;DeviceId=Sensor2;SharedAccessKey=r6/BpBaPodghThAU8DM37bpBZuimBUWlvBS7NA69Fzs="

def get_telemetry():
    return {
        "temperature": random.uniform(20.0, 40.0),
        "humidity": random.uniform(30.0, 70.0)
    }

def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    locations = ["Dow's Lake", "Fifth Avenue", "NAC"]
    try:
        while True:
            for spot in locations:
                payload = {
                    "location": spot,
                    "iceThickness": random.randint(20, 40),
                    "surfaceTemperature": random.randint(-10, 2),
                    "snowAccumulation": random.randint(0, 15),
                    "externalTemperature": random.randint(-15, 5),
                    "timestamp": datetime.utcnow().isoformat() + "Z"
                }
                msg = Message(json.dumps(payload))
                print(f"Sending message: {payload}")
                try:
                    client.send_message(msg)
                except Exception as e:
                    print(f"Failed to send message: {e}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopped sending messages.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()  