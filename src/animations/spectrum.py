class SpectrumAnimation():
	name = 'spectrum'
	
	def __init__(self, matrix):
		self.matrix = matrix

	def animate(self, formatted_audio):
		amplitude = 0
		
		for x in range(self.matrix.width):
			for y in range(self.matrix.height):
				if x >= self.matrix.width/2:
					amplitude = self.get_mirror_pixel_amplitude(formatted_audio, x+1)
				else:
					amplitude = formatted_audio[x]
				
				if amplitude < y:
					#black pixel
					red = 0
					green = 0
					blue = 0
				else:
					#colored pixel
					red = self.getColorValue1(amplitude)
					green = self.getColorValue2(x)
					blue = self.getColorValue3(y)
				
				reversed_Y = (self.matrix.height - 1) - y
				self.matrix.SetPixel(x, reversed_Y, red, green, blue)

	def get_mirror_pixel_amplitude(self, formatted_audio, x):
		return formatted_audio[self.matrix.width - x]
	
	def getColorValue1(self, value):
		if value * 5 + 100 > 255:
			return 255
		else:
			return value*5 + 10

	def getColorValue2(self, value):
		if value * 2 - 20 < 0:
			return 0
		else:
			return value * 2 - 20

	def getColorValue3(self, value):
		if value * 5 + 100 > 255:
			return 255
		else:
			return value * 5 + 100
