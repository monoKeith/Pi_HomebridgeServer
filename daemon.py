import time
import threading
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

    # Run sw server in new thread
    sw_server_thread = threading.Thread(target = SW_SERVER.run)
    sw_server_thread.start()


    # Display spash screen delay
    time.sleep(5)

    while(True):
        # Main loop
        UI_CTL.refresh()
        time.sleep(0.2)


finally:
    UI_CTL.clear_screen()