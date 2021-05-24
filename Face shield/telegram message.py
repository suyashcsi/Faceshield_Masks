import requests                
import json                     
import time                     
from boltiot import Bolt        
import conf                     
mybolt = Bolt(conf.bolt_api_key, conf.device_id)
response = mybolt.serialBegin('9600')
def get_sensor_value_from_pin(pin):
    """Returns the sensor value. Returns -999 if requefist fails"""
    try:
        response = mybolt.serialRead('10')
        data = json.loads(response)
        if data["success"] != 1:
            print("Request not successfull")
            print("This is the response->", data)
            return -999
        sensor_value = int(data["value"])
        return sensor_value
    except Exception as e:
        print("Something went wrong when returning the sensor value")
        print(e)
        return -999
def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "GET",
            url,
            params=data
        )
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False
while True:
    # Step 1
    sensor_value = get_sensor_value_from_pin("10")    
    print("The current sensor value is:", sensor_value)
    if sensor_value == -999:
        print("Request was unsuccessfull. Skipping.")
        time.sleep(1)
        continue
    if sensor_value <= conf.threshold:
        print("Sensor value has decreased threshold")
        message = "Alert! intruder " 
        ". The current sensor value is " + str(sensor_value)
        telegram_status = send_telegram_message(message)
        print("This is the Telegram status:", telegram_status)
    time.sleep(1)