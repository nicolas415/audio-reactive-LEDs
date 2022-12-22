from PIL import Image

class SamusAnimation():
	def __init__(self, matrix):
		self.matrix = matrix
		self.images = [0] * 3
		self.bass_hit_counter = 0
		self.images = [0] * 3
		self.images[0] = Image.open('/home/coneeone/dev/audio_processing/img/sam1.png')
		self.images[1] = Image.open('/home/coneeone/dev/audio_processing/img/sam2.png')
		self.images[2] = Image.open('/home/coneeone/dev/audio_processing/img/sam3.png')
		self.images[1].thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
		self.images[2].thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
		self.images[0].thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
	
	def animate(self, formatted_audio):
		if (formatted_audio[0] > 15) | (self.bass_hit_counter > 0):
			if self.bass_hit_counter > 0:
				self.bass_hit_counter = self.bass_hit_counter - 1

			elif self.bass_hit_counter < 1 :
				self.bass_hit_counter = 80

			self.matrix.SetImage(self.images[2].convert('RGB'))

		else:
			self.matrix.SetImage(self.images[0].convert('RGB'))