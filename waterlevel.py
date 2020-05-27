import time
import sys
import ibmiotf.application
import ibmiotf.device
import requests
import random#node-red apitoken R0!0YdZ90ot8hEc7g6
#Provide your IBM Watson Device Credentials
organization = "qd0meg" #azu7j9
deviceType = "raspberrypi"#raspberrypi
deviceId = "123456"#123456
authMethod = "token"
authToken = "!s6_I2IB1Gf1h3e6qB"#12345678

# Initialize GPIO

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        

        waterLevel = random.randrange(0,101,2)
        #Send Water Level to IBM Watson
        data = { 'WaterLevel' : waterLevel}
        #print (data)
        if waterLevel==100:
                r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=AR1aQKTJsqO6SmuohbfgW0CLBEeUYF4HlZrDzk35ywNd9tvcPiVs921OGhymwLRJtuFarYNcb8eBQZdk&sender_id=FSTSMS&message=Tank%20Full%20and%20Tank%20OverFlow&language=english&route=p&numbers=9494354282')
                print(r.status_code)
        def myOnPublishCallback():
            print ("Published WaterLevel = %d ltrs" % waterLevel,"to IBM Watson")

        success = deviceCli.publishEvent("Water level", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback #subscription

# Disconnect the device and application from the cloud
deviceCli.disconnect()
