### MQTT SUBSCRIBER SERIAL 1, BROKER CLOUD

#---------------------------------------------------------------------------# 
import paho.mqtt.client as mqtt
#import requests
import json
import pymysql
from datetime import datetime
'''
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    '''
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.toPic+" "+str(msg.payload))
    payloads = json.loads(msg.payload)
    timemili = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print timemili
    con = pymysql.connect(host = 'localhost',user = **********,passwd = ********,db = ********)
    cursor = con.cursor()
    cursor.execute("INSERT INTO `smartgrid_tf`.`SPB_cell_datapengukuran_mqtt` ( `datetime`, `SPB_Lm_id`, `SPB_Lm_ver`, `Imod`, `Tmod`, `SPB_Cell_id`, `SPB_Cell_ver`, `Vcell`, `Tcell`, `IntRcell`, `SOCcell`, `SOHcell`, `timestamp_milisecond`)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", ( payloads['tanggal'],payloads['SPB_Lm_id'],payloads['SPB_Lm_ver'],payloads['Imod'],payloads['Tmod'],payloads['SPB_Cell_id'],payloads['SPB_Cell_ver'],payloads['Vcell'],payloads['Tcell'],payloads['IntRcell'],payloads['SOCcell'],payloads['SOHcell'], timemili))
    con.commit()
    con.close()

mqtts = mqtt.Client()
#mqtts.on_connect = on_connect
mqtts.on_message = on_message
mqtts.connect("eng-cloud.com", 1883, 60)
mqtts.subscribe("SPB", qos=0)
mqtts.loop_forever()
 