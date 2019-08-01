import requests
import time
import random

dataFlowObject={}

url = 'YOUR ENDPOINT HERE'

while True:
    dataFlowObject["deviceID"] = "909456"
    dataFlowObject["name"] = "Raspberry_Pi"
    dataFlowObject["tempF"] = str(random.randint(55,120))
    dataFlowObject["humidity"] = str(random.randint(30,100))
    dataFlowObject["windspeed"] = str(random.randint(0,200))
    requests.post(url, verify=False, json=dataFlowObject)
    #time.sleep(10)

