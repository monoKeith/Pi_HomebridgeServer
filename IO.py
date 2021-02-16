import RPi.GPIO as GPIO
import time

# IO class, controls relay and buttons
class IO_class:


    def on(self):
        self.relay_on = True
        self.relay_update()


    def off(self):
        self.relay_on = False
        self.relay_update()


    def dim_screen(self):
        self.UI_CTL.clear_screen()
        

    def relay_update(self):
        GPIO.output(self.PIN_Relay, self.relay_on)
        self.UI_CTL.check()


    def handle_press(self, channel):
        if(not self.thread_lock):
            self.thread_lock = True
            if   (channel == self.PIN_Black):
                # print("Black.")
                self.dim_screen()
            elif (channel == self.PIN_Grey):
                # print("Grey.")
                self.off()
            elif (channel == self.PIN_White):
                # print("White.")
                self.on()
            # debounce
            time.sleep(self.PIN_Bouncetime / 100)
            self.thread_lock = False


    def __init__(self):
        # Define button pins
        self.PIN_Black = 17
        self.PIN_Grey  = 27
        self.PIN_White = 22
        # Define repay pin
        self.PIN_Relay = 23
        # Button Debounce = 200ms
        self.PIN_Bouncetime = 200
        # Status
        self.relay_on = False
        # Init button pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_Black, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.PIN_Grey,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.PIN_White, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # Init relay pin
        GPIO.setup(self.PIN_Relay, GPIO.OUT)
        # Register event handler
        GPIO.add_event_detect(self.PIN_Black, GPIO.RISING, callback=self.handle_press, bouncetime=self.PIN_Bouncetime)
        GPIO.add_event_detect(self.PIN_Grey,  GPIO.RISING, callback=self.handle_press, bouncetime=self.PIN_Bouncetime)
        GPIO.add_event_detect(self.PIN_White, GPIO.RISING, callback=self.handle_press, bouncetime=self.PIN_Bouncetime)
        # Class vars
        self.thread_lock = False
        self.UI_CTL = None