# Import standard python modules.
import os
import board
import neopixel
from Adafruit_IO import MQTTClient
from sys import exit
from time import sleep

# attach DIN of neopixel to DMA pin of Rpi
PIXEL_PIN = board.D18
ORDER = neopixel.GRB

# defined using device variables on balena dashboard
NUM_PIXELS = int(os.environ.get('NUM_PIXELS'))
BRIGHTNESS = float(os.environ.get('BRIGHTNESS'))

ADAFRUIT_IO_KEY = os.environ.get('ADAFRUIT_IO_KEY')
ADAFRUIT_IO_USERNAME = os.environ.get('ADAFRUIT_IO_USERNAME')
FEED_ID = os.environ.get('FEED_ID')

pixels = neopixel.NeoPixel(
    PIXEL_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=True, pixel_order=ORDER
)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow(wait):
    for j in range(255):
        for i in range(NUM_PIXELS):
            pixel_index = (i * 256 // NUM_PIXELS) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        sleep(wait)

# Define callback functions which will be called when certain events happen.
def connected(client):
    print('Subscribing to Feed {0}'.format(FEED_ID))
    client.subscribe(FEED_ID)
    print('Waiting for feed data...')

def disconnected(client):
    exit(1)

def message(client, feed_id, payload):
    if payload == "rainbow":
        print('Feed {0} received new value: {1}'.format(feed_id, payload))
        rainbow(0.0001)
    else:
        print('Feed {0} received new value: {1}'.format(feed_id, payload))
        RGB = [x.strip() for x in payload.split('#')]
        val = int(RGB[1], 16)
        pixels.fill(val)
        pixels.show()
        sleep(0.1)

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

# Connect to the Adafruit IO server.
client.connect()
client.loop_blocking()