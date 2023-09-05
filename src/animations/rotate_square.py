import math
import numpy as np

class RotateSquareAnimation():
	name = 'rotate_square'
	
	def __init__(self, matrix):
		self.matrix = matrix
		self.cent_x = self.matrix.width / 2
		self.cent_y = self.matrix.height / 2
		self.rotate_square = min(self.matrix.width, self.matrix.height) * 1.41
		self.min_rotate = self.cent_x - self.rotate_square / 2
		self.max_rotate = self.cent_x + self.rotate_square / 2
		self.display_square = min(self.matrix.width, self.matrix.height) * 0.7
		self.min_display = self.cent_x - self.display_square / 2
		self.max_display = self.cent_x + self.display_square / 2
		self.deg_to_rad = 2 * 3.14159265 / 360
		self.rotation = 0
		self.col_table = []

		# Pre calculate colors
		for x in range(int(self.min_rotate), int(self.max_rotate)):
			self.col_table.insert(x, self.scale_col(x, self.min_display, self.max_display))

		self.offset_canvas = self.matrix.CreateFrameCanvas()
		self.matrix.Fill(0,0,0)


	def animate(self, formatted_audio, animation_loop_counter):
		bass = formatted_audio[0] 
		bass_color = np.interp(bass, (0, self.max_display), (0, 255))


		self.rotation += 1
		self.rotation %= 360

		# calculate sin and cos once for each frame
		angle = self.rotation * self.deg_to_rad
		sin = math.sin(angle)
		cos = math.cos(angle)

		for x in range(0, int(self.matrix.width)):
			for y in range(0, int(self.matrix.width)):
				# Our rotate center is always offset by cent_x
				rot_x, rot_y = self.rotate(x - self.cent_x, y - self.cent_x, sin, cos)

				if x >= self.min_display and x < self.max_display and y >= self.min_display and y < self.max_display:
					x_col = self.col_table[x]
					y_col = self.col_table[y]
					self.offset_canvas.SetPixel(rot_x + self.cent_x, rot_y + self.cent_y, round(bass_color/1.5), round(y_col/4), round(x_col/4))
				else:
					self.offset_canvas.SetPixel(rot_x + self.cent_x, rot_y + self.cent_y, 0, 0, 0)
		
		self.offset_canvas = self.matrix.SwapOnVSync(self.offset_canvas)
	
	def scale_col(self, val, lo, hi):
		if val < lo:
			return 0
		if val > hi:
			return 255
		return 255 * (val - lo) / (hi - lo)

	def rotate(self, x, y, sin, cos):
		return x * cos - y * sin, x * sin + y * cos