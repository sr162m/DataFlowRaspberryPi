msg.sensor = msg.payload;

data={};
if (msg.sensor.hasOwnProperty("deviceID")){
    data["deviceID"] = parseFloat(msg.sensor.deviceID);
}
if (msg.sensor.hasOwnProperty("name")){
    data["deviceName"] = msg.sensor.name;
}
if (msg.sensor.hasOwnProperty("tempF")){
    data["tempF"] = parseFloat(msg.sensor.tempF);
}
if (msg.sensor.hasOwnProperty("humidity")){
    data["humidity"] = parseFloat(msg.sensor.humidity);
}
if (msg.sensor.hasOwnProperty("windspeed")){
    data["windspeed"] = parseFloat(msg.sensor.windspeed);
}

timestamp = new Date().toISOString();

msg.payload = {
    "object": msg.sensor.name,
    "class": context.global.properties._class,
    "data": data,
    "timestamp": timestamp
    
}
return msg;
