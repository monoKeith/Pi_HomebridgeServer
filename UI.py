import time
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class UI_class:
    
    # Splash screen
    def splash(self):
        splash = Image.new('1', (self.WIDTH, self.HEIGHT))
        draw = ImageDraw.Draw(splash)
        draw.text((10,0), "嘿嘿", font=self.FONT_TC, fill=256)
        self.update(splash)

    # Print provided image to screen
    def update(self, image):
        self.DISPLAY.image(image)
        self.DISPLAY.display()

    # Blank screen
    def clear_screen(self):
        self.DISPLAY.clear()
        self.DISPLAY.display()


    def print_text(self, text):
        image = Image.new('1', (self.WIDTH, self.HEIGHT))
        draw = ImageDraw.Draw(image)
        draw.text((10,10), text, font=self.FONT, fill=256)
        self.update(image)


    def check(self):
        self.clear_screen()
        if(self.IO_CTL.relay_on):
            self.print_text("iKEA  ON")
        else:
            self.print_text("iKEA OFF")


    def __init__(self):
        # Initialize display
        self.DISPLAY = Adafruit_SSD1306.SSD1306_128_64(rst=24)
        self.DISPLAY.begin()
        self.clear_screen()
        self.WIDTH  = self.DISPLAY.width
        self.HEIGHT = self.DISPLAY.height
        # Define fonts
        self.FONT    = ImageFont.truetype("Fonts/PTMono.ttc", 23)
        self.FONT_TC = ImageFont.truetype("Fonts/PingFang.ttc", 55)
        self.EMOJI   = ImageFont.truetype("Fonts/AppleEmoji.ttc", 48)
        # variables
        self.IO_CTL = None

