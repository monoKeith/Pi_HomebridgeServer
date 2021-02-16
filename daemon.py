import time
import IO
import UI
import switchServer as SW_SERVER


# Setup
UI_CTL = UI.UI_class()
IO_CTL = IO.IO_class()
SW_SERVER.IO_CTL = IO_CTL

# Splash screen
UI_CTL.splash()

# Run flask server.
SW_SERVER.app.run(host="localhost", port=5001, debug=False)


while(True):
    # main loop
    time.sleep(100)