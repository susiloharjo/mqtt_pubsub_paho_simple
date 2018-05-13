import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    print ( message.payload )
 
Connected = False   #global variable for the state of the connection
 
broker_address= "app.iot.mkncorp.com"  #Broker address
port = 1883                         #Broker port
user = "lora"                    #Connection username
password = "user.1001"            #Connection password
 
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
   client.publish("Hello","Connected")
   time.sleep(1)
try:
    while True:
        client.publish("Hello","HelloWorld")
        time.sleep(10)
 
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()
