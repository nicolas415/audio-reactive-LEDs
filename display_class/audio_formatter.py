import math
import numpy as np

class AudioProcessor():
	def __init__(self, sample_rate):
		self.FFT = np.array([])
		self.SAMPLE_RATE = sample_rate
		self.BUFFER_SIZE = np.int16
		self.DATA_WIDTH = 16
		self.DATA_HEIGHT = 8
	
	def get_formatted_fft(self, in_data):
		data_array = np.frombuffer(in_data, dtype=self.BUFFER_SIZE)
		fft = np.fft.rfft(data_array)
		formatted_fft = self.format_fft(abs(fft))
		return formatted_fft

	def format_fft(self, fft):
		formatted_bin_size = math.floor(len(fft) / self.DATA_WIDTH)
		counter = 0
		accumulator = 0
		formatted_fft = np.array([])

		for index in range(fft.size):
			accumulator = accumulator + fft[index]
			counter = counter + 1

			if counter == formatted_bin_size:
				formatted_fft = np.append(formatted_fft, accumulator)
				formatted_fft = np.append(formatted_fft, accumulator)

				accumulator = 0
				counter = 0
		
		formatted_fft = np.interp(formatted_fft, (0, self.SAMPLE_RATE), (0, self.DATA_HEIGHT))
		return np.round(formatted_fft)

	
		