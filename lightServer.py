import wiringpi
from flask import Flask

# setup wiringPi
wiringpi.wiringPiSetup()

# Set pin 4 to output
PIN_OUT = 4
wiringpi.pinMode(PIN_OUT, 1)

app = Flask(__name__)


# Status var
lightOn = False

# Update pin to match status
def update():
	global lightOn
	wiringpi.digitalWrite(PIN_OUT, lightOn)

# Turn on
@app.route("/on")
def on():
	global lightOn
	lightOn = True
	update()
	return "on"

# Turn off
@app.route("/off")
def off():
	global lightOn
	lightOn = False
	update()
	return "off"

# Check status, returns str(1) or str(0)
@app.route("/status")
def status():
	global lightOn
	return str(1 if lightOn else 0)

