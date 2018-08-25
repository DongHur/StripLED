import time
import random
from neopixel import Adafruit_NeoPixel, Color

LED_COUNT = 60
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255


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

if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_BRIGHTNESS)
	strip.begin()
	strip.setPixelColor(0, Color(0, 255, 0))
	time.sleep(30)
	strip.setPixelColor(0, Color(0, 0, 0))
	# rainFall1(strip)

