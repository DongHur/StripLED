import time
import random
from neopixel import Adafruit_NeoPixel, Color

LED_COUNT = 60
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0


"""
* note: rain code travels at different speed as well
G1, G2, G3, G4, G5, W
G1 - G4 => Dark Green to Green
G5 => Mixture of Green and White
W = > Pure White

G1: scale = 0.2; Color(0, 255*scale, 0)
G2: scale = 0.3; Color(0, 255*scale, 0)
G3: scale = 0.5; Color(0, 255*scale, 0)
G4: scale = 0.8; Color(0, 255*scale, 0)
G5: scale = 1; Color(0, 255, 0)
W: Color(255, 255, 255)
2 4
3 5
4 6
"""
def stepByStep(strip, color, wait_ms=500):
	for i in range(0,15,1):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000)
		strip.setPixelColor(i, Color(0, 0, 0))
		strip.show()

def drop(strip, R_color, G_color, B_color, wait_ms=500):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(R_color, G_color, B_color))
		count = i
		fade_factor = 0.5
		while(count > 0):
			count-=1
			strip.setPixelColor(count, Color(R_color*fade_factor, G_color*fade_factor, B_color*fade_factor))
			fade_factor *= 0.5
		strip.show()
		time.sleep(wait_ms/1000)
		# if i is not - dim the light before i

def rainFall1(strip, scale=0.2, wait_ms=5000, iterations=10):
	for k in range(iterations):
		strip.setPixelColor(0, Color(0, 255, 0))
		strip.show()
		time.sleep(wait_ms/1000.0)
		for j in range(strip.numPixels() - 1):
			for i in range(strip.numPixels() - 1):
				p_color = strip.getPixelColor(i)
				green = int((p_color-255)*scale+255)
				strip.setPixelColor(i, Color(0, green, 0))
				strip.setPixelColor(i+1, p_color)
			strip.show()
			time.sleep(wait_ms/1000.0)

def clearAll(strip):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0, 0, 0))
	strip.show()

if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	strip.begin()
	drop(strip, 0, 0, 150)
	time.sleep(1)
	clearAll(strip)
	# stepByStep(strip, Color(255, 0, 0))
	# clearAll(strip)
