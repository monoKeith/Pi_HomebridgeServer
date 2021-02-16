import time
import Adafruit_SSD1306

from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class UI_class:


    def __init__(self):
        self.ON = True
        # Initialize display
        self.DISPLAY = Adafruit_SSD1306.SSD1306_128_64(rst=24)
        self.WIDTH  = self.DISPLAY.width
        self.HEIGHT = self.DISPLAY.height
        self.DISPLAY.begin()
        self.clear_screen()
        # Define fonts
        self.FONT    = ImageFont.truetype("Fonts/PTMono.ttc", 23)
        self.FONT_LG = ImageFont.truetype("Fonts/PTMono.ttc", 35)
        self.FONT_TC = ImageFont.truetype("Fonts/PingFang.ttc", 30)
        self.EMOJI   = ImageFont.truetype("Fonts/AppleEmoji.ttc", 48)
        # IO class reference
        self.IO_CTL = None
        # Splash screen on start
        self.image = self.splash()
        self.update()
        # Temporary message (Image type)
        self.have_tmp_message = False
        self.tmp_message = None

    # Returns a new Image of appropriate size
    def new_image(self):
        # returns a new image
        return Image.new('1', (self.WIDTH, self.HEIGHT))

    # Turn on the Display and Resume content
    def on(self):
        self.ON = True
        self.update()

    # Turn off the Display
    def off(self):
        self.ON = False
        self.DISPLAY.clear()
        self.DISPLAY.display()
    
    # Toggle ON/ OFF
    def toggle(self):
        if (self.ON):
            self.off()
        else:
            self.on()

    # Returns a Splash screen Image
    def splash(self):
        splash = self.new_image()
        draw = ImageDraw.Draw(splash)
        draw.text((5,15), "亦可赛艇", font=self.FONT_TC, fill=256)
        return splash

    # Display self.image (by default) on screen immediatelly
    def update(self, image=None):
        if (self.ON):
            self.DISPLAY.image(self.image if image is None else image)
            self.DISPLAY.display()

    # Replace self.image with a new image
    def clear_screen(self):
        self.image = self.new_image()

    # Print text to self.image (by default)
    def print_text(self, text, row=1, image=None):
        draw = ImageDraw.Draw(self.image if image is None else image)
        draw.text((10,10 if row == 1 else 37), text, font=self.FONT, fill=256)

    # Print large text immediatelly
    def print_fullscreen(self, text):
        self.clear_screen()
        draw = ImageDraw.Draw(self.image)
        draw.text((15,20), text, font=self.FONT_LG, fill=256)
        self.update()

    # Request a tmp message showing current status
    def request_tmp_msg(self):
        self.tmp_message = self.new_image()
        self.print_text("iKEA", row=1, image=self.tmp_message)
        self.print_text(
            "Lamp  ON" if self.IO_CTL.relay_on else "Lamp OFF", 
            row=2, image=self.tmp_message)

        self.have_tmp_message = True
            
        
    # add time to display
    def print_time(self):
        now = datetime.now()
        cur_time = now.strftime("%H:%M")
        self.print_fullscreen(cur_time)

    # display new information
    def refresh(self):
        # At max holds one additional tmp message when displaying
        while (self.have_tmp_message):
            self.have_tmp_message = False
            # Display tmp message for 3s if any
            self.update(image=self.tmp_message)
            time.sleep(3)
        # Display time
        self.print_time()