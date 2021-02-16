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


    def on(self):
        self.ON = True
        self.update()


    def off(self):
        self.ON = False
        self.blank_screen()
    

    def toggle(self):
        if (self.ON):
            self.off()
        else:
            self.on()

    # Splash screen
    def splash(self):
        splash = Image.new('1', (self.WIDTH, self.HEIGHT))
        draw = ImageDraw.Draw(splash)
        draw.text((5,15), "亦可赛艇", font=self.FONT_TC, fill=256)
        return splash

    # Print provided image to screen
    def update(self):
        if (self.ON):
            self.DISPLAY.image(self.image)
            self.DISPLAY.display()

    # Turn off screen
    def blank_screen(self):
        self.DISPLAY.clear()
        self.DISPLAY.display()

    # new image
    def clear_screen(self):
        self.image = Image.new('1', (self.WIDTH, self.HEIGHT))


    def print_text(self, text, row=1):
        draw = ImageDraw.Draw(self.image)
        draw.text((10,10 if row == 1 else 37), text, font=self.FONT, fill=256)
        self.update()


    def print_fullscreen(self, text):
        self.clear_screen()
        draw = ImageDraw.Draw(self.image)
        draw.text((15,20), text, font=self.FONT_LG, fill=256)
        self.update()


    def check(self):
        self.clear_screen()
        if(self.IO_CTL.relay_on):
            self.print_text("iKEA  ON")
        else:
            self.print_text("iKEA OFF")
        
    # add time to display
    def show_time(self):
        now = datetime.now()
        cur_time = now.strftime("%H:%M")
        self.print_fullscreen(cur_time)

