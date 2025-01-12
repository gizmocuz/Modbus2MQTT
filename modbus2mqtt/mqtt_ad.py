# MQTT-AD Helper
#(c) 2023 GizMoCuz
# V1.01

import json

class MQTT_AD_Helper():
    @staticmethod
    def createBinaryObject(root, name, varname, unique_id, payload_on = "ON", payload_off = "OFF"):
        device_identifier = unique_id
        if device_identifier.find("_") != -1:
            device_identifier = unique_id.split("_")[0]
        vjson = {
            "stat_t": "~/state",
            "dev": {
                "manufacturer": "PA1DVB"
            }
        }
        vjson["dev"]["ids"].append(device_identifier)
        vjson["~"] = root
        vjson["name"] = name
        vjson["payload_on"] = payload_on
        vjson["payload_off"] = payload_off
        vjson["uniq_id"] = unique_id
        vjson["val_tpl"] = "{{ value_json." + varname + " }}"
        return vjson

    @staticmethod
    def createLightObject(root, name, varname, unique_id, payload_on = "ON", payload_off = "OFF"):
        device_identifier = unique_id
        if device_identifier.find("_") != -1:
            device_identifier = unique_id.split("_")[0]
        vjson = {
            "stat_t": "~/state",
            "dev": {
                "manufacturer": "PA1DVB"
            }
        }
        vjson["dev"]["ids"].append(device_identifier)       
        vjson["~"] = root
        vjson["name"] = name
        vjson["payload_on"] = payload_on
        vjson["payload_off"] = payload_off
        vjson["cmd_t"] = "~/set/" + varname
        vjson["uniq_id"] = unique_id
        vjson["val_tpl"] = "{{ value_json." + varname + " }}"
        return vjson

    @staticmethod
    def createSwitchObject(root, name, varname, unique_id, payload_on = "ON", payload_off = "OFF"):
        device_identifier = unique_id
        if device_identifier.find("_") != -1:
            device_identifier = unique_id.split("_")[0]
        vjson = {
            "stat_t": "~/state",
            "dev": {
                "manufacturer": "PA1DVB"
            }
        }
        vjson["dev"]["ids"].append(device_identifier)
        vjson["~"] = root
        vjson["name"] = name
        vjson["payload_on"] = payload_on
        vjson["payload_off"] = payload_off
        vjson["cmd_t"] = "~/set/" + varname
        vjson["uniq_id"] = unique_id
        vjson["val_tpl"] = "{{ value_json." + varname + " }}"
        return vjson

    @staticmethod
    def createNumberObject(root, name, varname, unique_id, step = 1):
        device_identifier = unique_id
        if device_identifier.find("_") != -1:
            device_identifier = unique_id.split("_")[0]
        vjson = {
            "stat_t": "~/state",
            "dev": {
                "manufacturer": "PA1DVB"
            }
        }
        vjson["dev"]["ids"].append(device_identifier)
        vjson["~"] = root
        vjson["name"] = name
        vjson["step"] = step
        vjson["cmd_t"] = "~/set/" + varname
        vjson["uniq_id"] = unique_id
        vjson["val_tpl"] = "{{ value_json." + varname + " }}"
        return vjson
    
    @staticmethod
    def createSensorObject(root, varname, unique_id, unit_of_measurement):
        device_identifier = unique_id
        if device_identifier.find("_") != -1:
            device_identifier = unique_id.split("_")[0]
        vjson = {
            "stat_t": "~/state/" + varname,
            "dev": {
                "manufacturer": "PA1DVB",
                "ids": []
            }
        }
        vjson["dev"]["ids"].append(device_identifier)
        vjson["~"] = root
        vjson["name"] = varname
        vjson["uniq_id"] = unique_id
        vjson["unit_of_meas"] = unit_of_measurement
        return vjson