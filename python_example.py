import requests
import time

dataFlowObject={}

url = 'YOUR ENDPOINT HERE'

while True:
	dataFlowObject["deviceID"] = "909456"
	dataFlowObject["name"] = "Raspberry_Pi"
	dataFlowObject["tempF"] = "98.6"
	dataFlowObject["humidity"] = "56"
	dataFlowObject["windspeed"] = "55"
	requests.post(url, json=dataFlowObject)
	time.sleep(10)


