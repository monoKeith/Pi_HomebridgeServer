from flask import Flask
app = Flask(__name__)

# IO controller, needs to be setup by daemon
IO_CTL = None

def setIO(io):
    global IO_CTL
    IO_CTL = io

"""Flask HTTP Handlers"""
# Turn on
@app.route("/on")
def on():
    global IO_CTL
    IO_CTL.on()
    return "on"

# Turn off
@app.route("/off")
def off():
    global IO_CTL
    IO_CTL.off()
    return "off"
from flask import Flask
# Check status, returns str(1) or str(0)
@app.route("/status")
def status():
    global IO_CTL
    return str(1 if IO_CTL.relay_on else 0)


# run app on port 5001
app.run(host="localhost", port=5001, debug=False)
