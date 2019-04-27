# charge3dglasses
A script to trigger IoT hardware based on data from Facebook events.

Author  : Brandon Tanner <theletterpi@gmail.com>\
Version : 1.0 (April 18, 2019)\
Project : https://github.com/pyrite357/charge3dglasses

## Project Description:
This is a script to analyze the Facebook events for a certain
group that has movie parties, and look for 3D in the event name.
If found, this script will trigger a Sonoff Basic module to power
on the charging station for the 3D Glasses, doing so 1 hour before the
event starts and then power it off after the event starts.

This helps the owner of the home theatre who would sometimes in the
past forget to charge all of the 3D Glasses prior to having a movie party.
This is an example of true home automation using IoT hardware. Another purpose for this project was to build a display case to keep the glasses off the floor and out of reach from children and pets, as some of the glasses were $40/ea. This case keeps them protected, and they can be charged all at once.

Although the author has been programming since the mid 90's, this was
his very first Python script ever written from scratch. Please forgive
any unsightly code ;)

## Credits:
Thanks to Joshua Wilfong for the idea to charge the glasses based on Facebook data.\
Thanks to Andrew Blankenship for coaching on setting up the Sonoff Basic, and flashing the firmware.\
Thanks to Victoria Kelley for helping to build the 3D Glasses charging station.

## Installation (written for Python 2.7):
   1). pip install python-dateutil requests\
   2). copy this script to your home directory in Linux\
   3). Add the IP Address of your Sonoff Basic to the ip_of_sonoff var below\
   4). Add the username and password of your Sonoff that was flashed with [Tasmota Firmware](https://github.com/arendst/Sonoff-Tasmota)\
   5). Make this script executable by running: chmod +x ~/charge3dglasses.py\
   5). Add the following line to your crontab so that it runs every 5 min
```
        */5 * * * * /home/yourusername/charge3dglasses.py
```
   6). sudo gem install [facebook-cli](https://github.com/specious/facebook-cli)\
   7). facebook-cli config --appid=<your_app_id> --appsecret=<your_app_secret>\
   7). facebook-cli login\
   8). Add the following line to your crontab to fetch Facebook events every 15 min
```
        */15 * * * * /path/to/facebook-cli api "/<group_id>/events" > /tmp/facebook_events.json
```

## TODO:
  * If manually turning on the charging station by the push button on the Sonoff, need to figure out a way for this script to not turn it off automatically.
  * Verify power is on/off after sending commands to turn the Sonoff on/off.
  * Perhaps just use the Facebook Graph API directly from the Python script.

## Feedback
I woud love any and all feedback! Especially on making this safer and more secure. The thought that electrical devices in my home are automatically controlled based on data from the Internet is scary, and even insane to some. However, I think with the right safe guards in place, this can be done right.

## Pictures:

Here is the glasses case I bought on ebay for $19.99 (USD)\
<img src="/../images/glassescase.jpg" width="300" height="300" />

I bought 2 of these A/C powered 6-port USB hubs for about $6.50 (USD) ea
<img src="/../images/usbhub.jpg" />

The Sonoff Basic R2 was bought on Amazon for $6.99 (USD)\
<img src="/../images/sonoff.jpg" width="300" height="300" />

Soldered these 4 male header pins on\
<img src="/../images/sonoff1.jpg" />

Bought this USB to TTL Adapter on Amazon for $12.49 (USD)\
<img src="/../images/sonoff2.jpg" />

Hooked the TTL adapter up to the Sonoff's header pins\
<img src="/../images/sonoff3.jpg" />

Flashing the Sonoff with [Tasmota Firmware](https://github.com/arendst/Sonoff-Tasmota) using [esptool.py](https://github.com/espressif/esptoolesptool)\
<img src="/../images/sonoff4.png" />

Sonoff is ready to go\
<img src="/../images/sonoff5.jpg" />

My home theatre room prior to starting this project\
<img src="/../images/livroombeforeshelf.jpg" />

I built and painted a shelf (apparently to Lowes, black means brown, oh well)\
<img src="/../images/paintshelf.jpg" />

Construction begins\
<img src="/../images/shelf1.jpg" />

Construction continues\
<img src="/../images/shelf2.jpg" />

Side view with USB hubs powered on\
<img src="/../images/shelf3.jpg" />

Built a side piece using the case backing\
<img src="/../images/shelf4.jpg" />

Test powering on the glasses\
<img src="/../images/shelf5.jpg" />

What it all looks like when finished\
<img src="/../images/shelf6.jpg" />

## Video:

[![Video Preview of Charging Station in action](https://img.youtube.com/vi/3aGKrcRz-d0/0.jpg)](https://www.youtube.com/watch?v=3aGKrcRz-d0)
