# Homebridge Hardware Control service

## Purpose

A Raspberry Pi Homebridge server is incredibly flexible and easy to setup for controlling any home appliances from the Apple Home APP.

By installing plugins like [HTTP-Switch](https://www.npmjs.com/package/homebridge-http-switch) in Homebridge, HTTP requests can be used as the intermediate way of connecting "Hardware" and "Software".

For the hardware side, [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) library in Python allows accessing GPIO pins conveniently. By pairing with [Flask](https://flask.palletsprojects.com/en/1.1.x/), building an HTTP server takes only several lines of code.

If the functionality of the device is very simple (ex. just a light switch), there's definitelly no need to separate them into parts. But once there are needs for more functionalities or logic, codes will get harder to maintain or modify if they are not organized.

The purpose of this project is to properly layout Python scripts that interact with hardware, so they are modular and can be easily modified when needed. All parts are controlled and initialized by the daemon, therefore it can be packed as a service to a Unit file, and start automatically by OS during boot.

## Hardware

I choose a Raspberry Pi Zero W as the "Controller", it can conenct to anything that works with the GPIO pins. Devices I connected are:

1. Relay (a 5V relay which controls a lamp)
2. Buttons (3 buttons)
3. Display (128*64 single-color OLED I2C display)
4. RGB LED Strip (1 meter of WS2812B, 60 LEDs/m)



# To Be Continued...