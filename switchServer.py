from flask import Flask

"""Flask HTTP Handlers"""

app = Flask(__name__)

IO_CTL = None

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

# Check status, returns str(1) or str(0)
@app.route("/status")
def status():
    global IO_CTL
    return str(1 if IO_CTL.relay_on else 0)
