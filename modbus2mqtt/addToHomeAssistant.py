from .mqtt_ad import MQTT_AD_Helper
from .helpers import *

class HassConnector:
    def __init__(self,mqc,globaltopic,verbosity):
        self.mqc=mqc
        self.globaltopic=globaltopic
        self.verbosity=verbosity
        self.broker_discovery_prefix = "homeassistant"
 
    def addAll(self,referenceList):
        try:
            if(self.verbosity):
                print("Adding all references to Home Assistant")
            for r in referenceList:
                if r.unit is not None:
                    object_type = "sensor"
                    unique_id = r.device.name + "_" + str(r.reference)
                    if r.unique_id is not None:
                        unique_id = r.unique_id
                    unique_id = unique_id + "_modbus2mqtt"
                    unique_id.replace(" ", "_")
                    varname = r.topic
                    jobj = MQTT_AD_Helper.createSensorObject(self.globaltopic[0:-1] + "/" + r.device.name, varname, unique_id, r.unit)
                    if jobj != None:
                        dtopic = self.broker_discovery_prefix + "/" + object_type + "/" + r.device.name + "/" + varname + "/config"
                        #print(f"publishing config ->: {dtopic}")
                        self.mqc.publish(dtopic, serialize_dict(jobj), 0, True)
                else:
                    if "r" in r.rw and not "w" in r.rw:
                        if r.poller.dataType == "bool":
                            self.addBinarySensor(r)
                        if r.poller.dataType == "int16":
                            self.addSensor(r)
                    if "w" in r.rw and "r" in r.rw:
                        if r.poller.dataType == "bool":
                            self.addSwitch(r)
                        if r.poller.dataType == "int16": #currently I have no idea what entity type to use here..
                            self.addSensor(r)
        except Exception as e:
            print("AA")
            if (self.verbosity):
                print("Error:", str(e))
            
    def addBinarySensor(self,ref):
        if(self.verbosity):
            print("Adding binary sensor "+ref.topic+" to HASS")
        #self.mqc.publish("homeassistant/binary_sensor/"+self.globaltopic[0:-1]+"_"+ref.device.name+"_"+ref.topic+"/config","{\"name\": \""+ref.device.name+"_"+ref.topic+"\", \"state_topic\": \""+self.globaltopic+ref.device.name+"/state/"+ref.topic+"\", \"payload_on\": \"True\", \"payload_off\": \"False\"}",qos=0,retain=True)

    def addSensor(self,ref):
        if(self.verbosity):
            print("Adding sensor "+ref.topic+" to HASS")
        #self.mqc.publish("homeassistant/sensor/"+self.globaltopic[0:-1]+"_"+ref.device.name+"_"+ref.topic+"/config","{\"name\": \""+ref.device.name+"_"+ref.topic+"\", \"state_topic\": \""+self.globaltopic+ref.device.name+"/state/"+ref.topic+"\"}",qos=0,retain=True)

    def addSwitch(self,ref):
        if(self.verbosity):
            print("Adding switch "+ref.topic+" to HASS")
        #self.mqc.publish("homeassistant/switch/"+self.globaltopic[0:-1]+"_"+ref.device.name+"_"+ref.topic+"/config","{\"name\": \""+ref.device.name+"_"+ref.topic+"\", \"state_topic\": \""+self.globaltopic+ref.device.name+"/state/"+ref.topic+"\", \"state_on\": \"True\", \"state_off\": \"False\", \"command_topic\": \""+self.globaltopic+ref.device.name+"/set/"+ref.topic+"\", \"payload_on\": \"True\", \"payload_off\": \"False\"}",qos=0,retain=True)

#    def removeAll(self,referenceList):
#        for ref in referenceList:
#            print("blah")
#            self.mqc.publish(self.globaltopic+ref.device.name+"/"+ref.topic,"",qos=0)

