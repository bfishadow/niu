#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json

strSerialNumber = "" # Check it in the app
strAppToken = "" # Dump the app request with Mitm

objNiuReq = urllib.request.Request("https://app-api.niu.com/v3/motor_data/index_info?sn=" + strSerialNumber)
objNiuReq.add_header("token", strAppToken)

with urllib.request.urlopen(objNiuReq) as objNiuResponse:
   objNiuAPIResult = objNiuResponse.read()
objNiuData = json.loads(objNiuAPIResult)

intNiuBatteryLevel = objNiuData["data"]["batteries"]["compartmentA"]["batteryCharging"]
intNiuEstMileage   = objNiuData["data"]["estimatedMileage"]
strNiuLocLat       = objNiuData["data"]["postion"]["lat"]
strNiuLocLng       = objNiuData["data"]["postion"]["lng"]
blnNiuCharging     = objNiuData["data"]["isCharging"]

strNiuChargingStatus = ""
if blnNiuCharging == 0 :
    strNiuChargingStatus = "(Not Charging)"
elif blnNiuCharging == 1 :
    strNiuChargingStatus = "(Charging)"

strNiuLocLat = int(strNiuLocLat*100000)/100000
strNiuLocLng = int(strNiuLocLng*100000)/100000

strNiuGoogleMapsLink = "https://www.google.com/maps/search/" + str(strNiuLocLat) + ",+" + str(strNiuLocLng)

print ("Battery Level:", intNiuBatteryLevel, "%", strNiuChargingStatus)
print ("Estimated Mileage:", intNiuEstMileage, "KM")
print ("Location:", strNiuGoogleMapsLink)
