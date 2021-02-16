import time
import IO
import UI
import switchServer as SW_SERVER

try:
    # Setup
    UI_CTL = UI.UI_class()
    IO_CTL = IO.IO_class()

    IO_CTL.UI_CTL = UI_CTL

    SW_SERVER.IO_CTL = IO_CTL
    UI_CTL.IO_CTL = IO_CTL


    # Splash screen
    UI_CTL.splash()

    # Run flask server, block until quit.
    SW_SERVER.app.run(host="localhost", port=5001, debug=False)

finally:
    UI_CTL.clear_screen()