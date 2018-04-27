# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
from colorsys import hsv_to_rgb, rgb_to_hsv

import Adafruit_GPIO.SPI as SPI
# Import the WS2801 module.
import Adafruit_WS2801
import RPi.GPIO as GPIO
# Configure the count of pixels:
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from webcolors import name_to_rgb, CSS3_NAMES_TO_HEX, rgb_to_name

from lights.models import Lighting

PIXEL_COUNT = 52

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)
blink = False
color = (255, 255, 255)
brightness = 1.0


@receiver(pre_save, sender=Lighting)
def enrich_lighting(sender, instance, **kwargs):
    Lighting.objects.filter(active=True).update(active=False)
    instance.active = True

    if instance.color_r is None and instance.color_g is None and instance.color_b is None and instance.color_name is None:
        instance.color_name = 'white'
        instance.color_r = 255
        instance.color_g = 255
        instance.color_b = 255
    elif instance.color_r and instance.color_g and instance.color_b:
        rgb = (instance.color_r, instance.color_g, instance.color_b)
        try:
            color_name = rgb_to_name(rgb)
            instance.color_name = color_name
        except ValueError:
            color_name = None
    elif instance.color_name:
        color_name = instance.color_name.lower()
        instance.color_name = color_name
        if color_name in CSS3_NAMES_TO_HEX.keys():
            r, g, b = name_to_rgb(color_name)
            instance.color_r = r
            instance.color_g = g
            instance.color_b = b


@receiver(post_save, sender=Lighting)
def lighting_added(sender, instance, **kwargs):
    lighting_type = instance.type

    # Clear all the pixels to turn them off.
    pixels.clear()
    pixels.show()  # Make sure to call show() after changing any pixels!
    global blink
    if lighting_type.name.lower() in ['color', 'blink']:
        global color
        # move_out()
        color = init_color(instance)
        if color is None:
            return

        if lighting_type.name.lower() == 'color':
            blink = False
            glow_color()
        elif lighting_type.name.lower() == 'blink':
            blink = True
            blink_color()
    else:
        blink = False
        if lighting_type.name.lower() == 'rainbow':
            rainbow_cycle_successive(wait_time=0.1)
            rainbow_cycle()
            rainbow_colors()
        elif lighting_type.name.lower() == 'off':
            # move_out()
            pixels.clear()
            pixels.show()


def init_color(lighting):
    global color
    global brightness
    if lighting.color_name is not None:
        color = name_to_rgb(lighting.color_name)
        if lighting.brightness is not None:
            brightness = lighting.brightness
            set_brightness()
    elif lighting.color_r is not None and lighting.color_g is not None and lighting.color_b is not None:
        color = (lighting.color_r, lighting.color_g, lighting.color_b)
        if lighting.brightness is not None:
            brightness = lighting.brightness
            set_brightness()
    return color


def set_brightness():
    global color
    global brightness
    if color is None:
        return

    h, s, v = rgb_to_hsv(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)
    s = brightness
    r, g, b = hsv_to_rgb(h, s, v)

    color = (int(r * 255), int(g * 255), int(b * 255))


# Define the wheel function to interpolate between different hues.
def wheel(pos):
    if pos < 85:
        return Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Adafruit_WS2801.RGB_to_color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Adafruit_WS2801.RGB_to_color(0, pos * 3, 255 - pos * 3)


# Define rainbow cycle function to do a cycle of all hues.
def rainbow_cycle_successive(wait_time=0.1):
    for i in range(pixels.count()):
        # tricky math! we use each pixel as a fraction of the full 96-color wheel
        # (thats the i / strip.numPixels() part)
        # Then add in j which makes the colors go around per pixel
        # the % 96 is to make the wheel cycle around
        pixels.set_pixel(i, wheel((i * 256 // pixels.count()) % 256))
        pixels.show()
        if wait_time > 0:
            time.sleep(wait_time)


def rainbow_cycle(wait_time=0.1):
    for j in range(256):  # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((i * 256 // pixels.count()) + j) % 256))
        pixels.show()
        if wait_time > 0:
            time.sleep(wait_time)


def rainbow_colors(wait_time=0.1):
    for j in range(256):  # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel((256 // pixels.count() + j) % 256))
        pixels.show()
        if wait_time > 0:
            time.sleep(wait_time)


def brightness_decrease(wait_time=0.1, step=1):
    for j in range(int(256 // step)):
        for i in range(pixels.count()):
            r, g, b = pixels.get_pixel_rgb(i)
            r = int(max(0, r - step))
            g = int(max(0, g - step))
            b = int(max(0, b - step))
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(r, g, b))
        pixels.show()
        if wait_time > 0:
            time.sleep(wait_time)


def glow_color():
    pixels.clear()
    # move_in()
    pixels.set_pixels_rgb(Adafruit_WS2801.RGB_to_color(*color))
    pixels.show()


def blink_color(wait_time=0.25):
    pixels.clear()
    # move_in()
    while blink:
        time.sleep(wait_time)
        pixels.clear()
        pixels.show()
        time.sleep(wait_time)

        pixels.set_pixels(Adafruit_WS2801.RGB_to_color(*color))
        pixels.show()


def move_in(wait_time=0.05):
    for i in range(pixels.count()):
        for j in reversed(range(i, pixels.count())):
            pixels.clear()
            # first set all pixels at the begin
            for k in range(i):
                pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color(*color))
            # set then the pixel at position j
            pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color(*color))
            pixels.show()
            time.sleep(wait_time)


def move_out(wait_time=0.05):
    for i in range(pixels.count()):
        for j in reversed(xrange(i)):
            pixels.clear()
            # first set all pixels at the end
            for k in range(i, pixels.count()):
                pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color(*color))
            # set then the pixel at position j
            pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color(*color))
            pixels.show()
            time.sleep(wait_time)
