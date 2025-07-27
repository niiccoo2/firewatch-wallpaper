### Imports ###
from datetime import datetime
import os  # Used for interacting safely with the operating system to access my secret (environmental) variable
import ctypes  # ctypes is used specifically to change the wallpaper
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

SPI_SETDESKWALLPAPER = 20  # Tells Windows API to perform action 20: set desktop wallpaper

def setWallpaper(imagePath):
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, os.path.abspath(imagePath).encode(), 0)

def getCurrentHour():
    current_datetime = datetime.now()
    return str(current_datetime.time())[0:2]

def add_quote(imagepath):
    img = Image.open(imagepath)
    draw = ImageDraw.Draw(img)
    quotes = []
    with open("quotes.txt", "r", encoding="utf-8") as quote_file:
        for i in range(104):
            line = quote_file.readline()
            if not line:
                break
            quotes.append(line.strip())

    #print("quotes.txt path:", os.path.abspath("quotes.txt"))
    #print("quotes loaded:", quotes)

    if not quotes:
        quote_to_print = ""
    else:
        quote_to_print = quotes[random.randint(0, len(quotes) - 1)]
    font = ImageFont.truetype("Roboto-VariableFont_wdth,wght.ttf", 80)
    draw.text((100, 2500), quote_to_print, (255, 255, 255), font=font)
    #print(quotes)

    # saving the image
    img.save('done.jpg')

# Generate a message to add to the wallpaper based on the current time
hour = int(getCurrentHour())
if hour > 0 and hour < 5: # Night
    imagepath = "./night.jpg"
elif hour < 8: # Sunrise
    imagepath = "./sun.jpg"
elif hour < 19: # Daytime
    imagepath = "./day.jpg"
elif hour < 21: # Sunset
    imagepath = "./sun.jpg"
else: # Night
    imagepath = "./night.jpg"

add_quote(imagepath)
setWallpaper("./done.jpg")
