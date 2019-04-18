#!/usr/bin/env python

"""Charge 3D Glasses based on Facebook Events

Author  : Brandon Tanner <theletterpi@gmail.com>
Version : 1.0 (April 18, 2019)

This is a script to analyze the Facebook events for a certain
group that has movie parties, and look for 3D in the event name.
If found, this script will trigger a Sonoff Basic module to power
on the charging station for the 3D Glasses, doing so 1 hour before the
event starts and then power it off after the event starts.

This helps the owner of the home theatre who would sometimes in the
past forget to charge all of the 3D Glasses prior to having a movie party.
This is an example of true home automation using IoT hardware.

Although the author has been programming since the mid 90's, this was
his very first Python script ever written from scratch. Please forgive
any unsightly code ;)

Credits:
Thanks to Joshua Wilfong for the idea to charge the glasses based on Facebook data.
Thanks to Andrew Blankenship for coaching on setting up the Sonoff Basic, and flashing the firmware.
Thanks to Victoria Kelley for helping to build the 3D Glasses charging station

Pictures of the hardware setup:
    TBD


Feedback welcome! Especially on making this safer and more secure.


Installation (written for Python 2.7):
   1). pip install python-dateutil requests
   2). copy this script to your home directory in Linux
   3). Add the IP Address of your Sonoff Basic to the ip_of_sonoff var below
   4). Add the username and password of your Sonoff that was flashed with Tasmota firmware
   5). Make this script executable by running: chmod +x ~/charge3dglasses.py
   5). Add the following line to your crontab so that it runs every 5 min
       */5 * * * * /home/yourusername/charge3dglasses.py
   6). sudo gem install facebook-cli
   7). facebook-cli config --appid=<your_app_id> --appsecret=<your_app_secret>
   7). facebook-cli login
   8). Add the following line to your crontab to fetch Facebook events every 15 min
       */15 * * * * /path/to/facebook-cli api "/<group_id>/events" > /tmp/facebook_events.json

"""

import sys
import json
import requests
from datetime import datetime
from datetime import timedelta
from dateutil import parser

# Begin user customizable variables:
ip_of_sonoff = "192.168.1.100"
events_file  = "/tmp/facebook_events.json"
username     = "admin"
password     = ""

# Begin calculated variables:
url = "http://" + ip_of_sonoff + "/cm?user=" + username + "&password=" + password + "&cmnd="
sonoff_cmd_sts = url + "Power"
sonoff_cmd_power_on = url + "Power%20On"
sonoff_cmd_power_off = url + "Power%20Off"

# Ensure Facebook Events file exists
try:
    json_file = open(events_file, 'rb')
except IOError:
    print("Could not read {}".format(events_file))
    sys.exit()

# Ensure that:
#       1). We can connect to the Sonoff
#       2). That we got a valid 200 response code
#       3). That we got valid JSON response data
#       4). That the JSON response contains a POWER key
# And exit if any of the above fail.
try:
    r = requests.get(sonoff_cmd_sts)
    if (r.status_code != 200):
        print("Fatal Error: Invalid status code from Sonoff")
        print(r.status_code)
        print(r.raise_for_status())
        sys.exit()
    else:
        sonoff_cur_status = r.json()
        if ("POWER" not in sonoff_cur_status):
            print("Fatal Error: Missing POWER key from Sonoff JSON Response")
            sys.exit()
        else:
            sonoff_cur_status = sonoff_cur_status['POWER']
except ValueError, e:
    print("Fatal Error: Invalid response from Sonoff")
    sys.exit()
except requests.ConnectionError:
    print("Fatal Error: Could not connect to Sonoff")
    sys.exit()

# Begin logic to determine if we should be charging right now
should_be_charging = False
with json_file:
    data = json.load(json_file)
    for i in data:
        # if the event name containts "3d " or " 3d"
        if ("3d " in i['name'].lower() or " 3d" in i['name'].lower()):
            # create a date obj from start_time
            dt = parser.parse(i['start_time'])
            # create a datetime object in the timezone of the dt obj
            now = datetime.now(dt.tzinfo)
            # check if dt is in the future
            if (dt > now):
                # check if current time is within 1 hour of the party starting
                onehourbeforeparty = dt - timedelta(hours=1)
                if (now >= onehourbeforeparty and now < dt):
                    should_be_charging = True
                    break

# Begin logic to Power On/Off the Sonoff
if (sonoff_cur_status == "OFF" and should_be_charging):
    # turn it on
    print('sending command to power on')
    results = requests.get(sonoff_cmd_power_on).json()
    print(results)
    # todo: verify it is on now
elif (sonoff_cur_status == "ON" and not should_be_charging):
    # turn it off
    print("Sending command to power off")
    results = requests.get(sonoff_cmd_power_off).json()
    print(results)
    # todo verify it is off now
else:
    print("Everything is the way it should be. POWER={}, shouldBeCharging={}.".format(sonoff_cur_status, should_be_charging))
