### Imports ###
from datetime import datetime
import os  # Used for interacting safely with the operating system to access my secret (environmental) variable
import ctypes  # ctypes is used specifically to change the wallpaper

SPI_SETDESKWALLPAPER = 20  # Tells Windows API to perform action 20: set desktop wallpaper

def setWallpaper(imagePath):
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, os.path.abspath(imagePath).encode(), 0)

def getCurrentHour():
    current_datetime = datetime.now()
    return str(current_datetime.time())[0:2]

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

setWallpaper(imagepath)