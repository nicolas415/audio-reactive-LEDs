import math
import pyaudio as pa

class AudioInputDevice():
	def __init__(self, pyAudio: pa.PyAudio, config):
		self.pyAudio = pyAudio
		self.name = ''
		self.index = -1
		self.sample_rate = -1
		self.config = config

	def set_device_by_name(self):
		target_name = self.config['input_device_name']
		host_info = self.pyAudio.get_host_api_info_by_index(0)
		host_devices_number = host_info.get('deviceCount')

		# iterate over the devices
		for i in range(0, host_devices_number):
			device = self.pyAudio.get_device_info_by_host_api_device_index(0, i)
			device_name = device.get('name')

			if target_name in device_name:
				device_inputs = device.get('maxInputChannels')
				device_has_inputs = device_inputs > 0
				if device_has_inputs:
					self.index = i
					self.name = device_name
					self.sample_rate = math.floor(device.get('defaultSampleRate'))



		
	