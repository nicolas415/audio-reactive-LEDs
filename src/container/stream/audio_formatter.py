import math
import numpy as np

'''
Takes an audio signal and processes it.
Returns an array the size of the leds matrix.
Lengths of the array matchs the matrix length (x axis)
Values of the array vary between 0 and the matrix height (y axis)
'''
class AudioFormatter():
	def __init__(self, sample_rate, matrix_rows):
		self.FFT = np.array([])
		self.SAMPLE_RATE = sample_rate
		self.BUFFER_SIZE = np.int16
		self.ROWS = matrix_rows

	def prepare_fft(self, in_data):
		data_array = np.frombuffer(in_data, dtype=self.BUFFER_SIZE)
		fft = np.fft.rfft(data_array)
		return abs(fft)

	def get_amplitude(self, fft, frequency_index):
		return fft[frequency_index]

	def decrease_lower_frequency(self, fft, frequency_index):
		return fft[frequency_index]


	def get_spectrum(self, in_data):
		fft = self.prepare_fft(in_data)
		formatted_fft = np.array([])
		for frequency_index in range(fft.size):
			### if we itarated over all the matrix's columns, break out the loop
			if frequency_index > self.ROWS:
				break
			amplitude = self.get_amplitude(fft, frequency_index)
			formatted_fft = np.append(formatted_fft, amplitude)
		
		formatted_fft = np.interp(formatted_fft, (0, self.SAMPLE_RATE), (0, self.ROWS))
		return np.round(formatted_fft)


	
		
