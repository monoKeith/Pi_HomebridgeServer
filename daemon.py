import time
import IO
import UI as UI_CTL
import switchServer as SW_SERVER


# Setup
IO_CTL = IO.IO_class()
SW_SERVER.IO_CTL = IO_CTL


# Run flask server.
SW_SERVER.app.run(host="localhost", port=5001, debug=False)


while(True):
    # main loop
    time.sleep(100)