# Smartcouch
This is a small project called smartcouch. With this project I'm tracking my development of a small REST based API running on a Raspberry Pi including the wiring with additional hardware like LED stripes. Beside the code I'm also including instructions and manuals on building the couch itself.

The software is AS IS 

The following hardware is needed to build the couch:
- Raspberry Pi (incl. Power supply, SD card, Wifi dongle, ...)
- LED stripes WS2801
- 5V 12A Power Supply (for LEDs)
- 3 Euro Pallets

## Setup


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
 

