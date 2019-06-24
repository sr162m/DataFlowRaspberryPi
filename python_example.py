import serial
import json
import requests
import time
import os

dataFlowObject={}

url = 'YOUR ENDPOINT HERE'

while True:
	dataFlowObject["deviceID"] = "909456"
	dataFlowObject["name"] = "Raspberry_Pi"
	dataFlowObject["tempF"] = "98.6"
	dataFlowObject["humidity"] = "56"
	dataFlowObject["windspeed"] = "55"
	requests.post(url, verify=False, json=dataFlowObject)
	time.sleep(10)


