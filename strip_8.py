# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
from math import *
from neopixel import *
from numpy import *

# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.  **was 16
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)


#===========================================================================

# the_pixel is the position on the strip and the parameter inside the cosine wave. It
     # controls the brightness, so that the brightness based on the position in the strip
     # goes smoothly between 0 and 255.
def fade_all(the_pixel):                           
	x = -120 * cos(.2 * the_pixel) + 120 
	return x


# this is a square wave of brightness between 0 and 100
# play with the "- 170" to get a fatter stripe of color
def fade_all_2(the_pixel):
	x = -180 * cos(.2 * the_pixel) - 170   
	if x < 0:
		x = 0
	if x > 0:
		x = 100
	return x



def set_colors_on_all_fade_4(strip, wait_ms=50):
	n = 0
	o = 0
	p = 0
	for j in range(400):                  # range is the duration of the loop
		for i in range(1, 30):        # there are 30 pixels on the strip
			x = fade_all(i + n)   # calls the cosine wave of brightness
			y = fade_all_2(i + o)
			z = fade_all_2(i + p) # calls the square wave of brightness
			if z > 0:             # only lets one color through on each pixel
				x = 0 
			strip.setPixelColorRGB(i, int(x), 0, int(z))  # sets the color
			strip.show()          # shows the color
	
		n += 3 * sin(.05 * j)         # moves the pixel position on the strip at variable speed
		o += 3                        # moves the pixel position at a constant rate
		p += 3 * sin(.04 * j)         # moves the pixel position on the strip.
		time.sleep(wait_ms/900.0)     # play with the ".04", that's the period of the sine wave


#===========================================================================================



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print 'Press Ctrl-C to quit.'
	for i in range(1):
		set_colors_on_all_fade_4(strip, wait_ms=50)
		colorWipe(strip, Color(0, 0, 0)) 



