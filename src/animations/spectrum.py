
'''
Animation that displays a colored spectrum reacting to the audio signal
'''
class SpectrumAnimation():
	name = 'spectrum'
	
	# set the rgb LEDs matrix in the contructor
	def __init__(self, matrix, config):
		self.config = config
		self.matrix = matrix

	# method called at each iteration of the animation loop
	def animate(self, formatted_audio, animation_loop_counter):
		amplitude = 0
		
		for x in range(self.matrix.width):
			for y in range(self.matrix.height):

				# mirrors frequencies on the matrix
				if x >= self.matrix.width/2:
					amplitude = self.get_mirror_pixel_amplitude(formatted_audio, x+1)
				else:
					amplitude = formatted_audio[x]
				
				if amplitude < y:
					# set black pixel
					red = 0
					green = 0
					blue = 0
					
				else:
					# gets red, green, blue colors for the pixel to display
					red = self.getColorValue1(amplitude)
					green = self.getColorValue2(x, animation_loop_counter)
					blue = self.getColorValue3(y)

					# modify green and blue color, to get time related color changes
					green = self.get_counter_relative_color(green, animation_loop_counter, 0.01)
					blue = self.get_counter_relative_color(blue, animation_loop_counter, 0.005)

				# displays the bottom left of the animation at x=0,y=0
				reversed_Y = (self.matrix.height - 1) - y
				self.matrix.SetPixel(x, reversed_Y, red, green, blue)

	# displays symetric pixels on the matrix
	def get_mirror_pixel_amplitude(self, formatted_audio, x):
		return formatted_audio[self.matrix.width - x]
	
	def getColorValue1(self, value):
		if value * 8 + 100 > 255:
			return 255
		else:
			return value * 8 + 100

	def getColorValue2(self, value, animation_loop_counter):
		print(animation_loop_counter)
		if (animation_loop_counter != 0):
			counter_value = animation_loop_counter / self.config['animation_iterations_nb']
		else:
			return 0
		
		if value * counter_value * 10 < 0:
			return 0
		else:
			return abs(value * counter_value * 10)

	def getColorValue3(self, value):
		if value * 5 + 100 > 255:
			return 255
		else:
			return value * 5 + 100

	# modifies a color relatively to the animation loop counter
	def get_counter_relative_color(self, color, count, ratio):
		color = round(color + count * ratio)
		
		if (color < 0):
			color = 0

		if (color > 255):
			color = 255

		return color
