# Smartcouch
This is a small project called smartcouch. With this project I'm tracking my development of a small REST based API running on a Raspberry Pi including the wiring with additional hardware like LED stripes. Beside the code I'm also including instructions and manuals on building the couch itself. The project comes with the django (tastypie) backend which runs on the Rasperry Pi and provides a REST API to controll the LEDs. Additionally there is an Android API which consumes the REST API and allows the user to change the colors of the LEDs.

The following hardware is needed to build the couch:
- Raspberry Pi (incl. Power supply, SD card, Wifi dongle, ...)
- LED stripes WS2801
- 5V 12A Power Supply (for LEDs)
- 3 Euro Pallets

## The couch
The couch I built was inspired by this:
![Alt text](http://www.dekomilch.de/wp-content/uploads/2017/08/paletten-couch-bauen.jpg "Source: http://www.dekomilch.de/diy-do-it-yourself/palettensofa-bauen-visuelle-anleitung/")

I additionaly used indoor gaze to get the color I wanted. After setting it up, I used tape underneeth the seating to have a better surface for the LED stripe.

## Wiring
For the wiring of the LED stripes with the Raspberry Pi and the power supply I used [this](https://tutorials-raspberrypi.de/raspberry-pi-ws2801-rgb-led-streifen-anschliessen-steuern/) tutorial. It's in german, but in one can focus on the image below.

As the LED stripes are supposed to be placed over the edges of the pallets, I cut them and soldered connectors to plug them together.

## Installation
To install the python requirements run the following command: 
```
cd backend 
pip install -r requirements.txt
```

## Execution
To run the REST server navigate to the backend and start the django server
``` 
cd backend
python manage.py runserver 0.0.0.0:8000
```
This will run the djangoserver on port 8000. Alternativly you can simply run the provided run script using ```./run.sh```. Make sure you have execution permissions for the script.
 

