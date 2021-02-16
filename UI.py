import time
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Initialize display
DISPLAY = Adafruit_SSD1306.SSD1306_128_64(rst=24)
DISPLAY.begin()
DISPLAY.clear()
DISPLAY.display()
# Fonts
FONT    = ImageFont.truetype("Fonts/PTMono.ttc", 23)
FONT_TC = ImageFont.truetype("Fonts/PingFang.ttc", 55)
EMOJI   = ImageFont.truetype("Fonts/AppleEmoji.ttc", 48)

WIDTH  = DISPLAY.width
HEIGHT = DISPLAY.height


# Splash screen
splash = Image.new('1', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(splash)
draw.text((10,0), "奕翔", font=FONT_TC, fill=128)


def update(image):
    DISPLAY.image(image)
    DISPLAY.display()

#update(splash)

update(splash.convert('1'))