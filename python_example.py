import serial
import json
import requests
import time
import os

dataFlowObject={}

url = 'https://runm-east.dataflow.iot.att.com/63b6a21dd8794/478e18f956a6/d821567aefc0ccc/in/flow/rpimain'

while True:
	dataFlowObject["deviceID"] = "909456"
	dataFlowObject["name"] = "Raspberry_Pi"
	dataFlowObject["tempF"] = "98.6"
	dataFlowObject["humidity"] = "56"
	dataFlowObject["windspeed"] = "55"
	requests.post(url, verify=False, json=dataFlowObject)
	time.sleep(10)


