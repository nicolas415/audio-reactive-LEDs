from typing import Any
import pyaudio
from devices_class.audio_input import AudioInputDevice
from data.audio_state import audio_state

class InputAudioStream():
	def __init__(self, pyaudio: pyaudio):
		self.pa = pyaudio
		self.pyAudio = pyaudio.PyAudio()
		self.stream: pyaudio.Stream
		self.DATA_CHUNKS = 256
		self.FFT_FREQUENCY_BINS = 16
		self.SAMPLE_FORMAT = pyaudio.paInt16
		self.AUDIO_CHANNELS = 1
		self.IS_INPUT = True

	def init(self, input_device: AudioInputDevice, audio_state: audio_state):
		audio_state['sample_rate'] = input_device.sample_rate

		def callback(in_data, frame_count, time_info, status):
			audio_state['raw_audio'] = in_data
			return (in_data, self.pa.paContinue)

		self.stream = self.pyAudio.open(format=self.SAMPLE_FORMAT,
										frames_per_buffer=self.DATA_CHUNKS,
										channels=self.AUDIO_CHANNELS,
										rate=input_device.sample_rate,
										input=self.IS_INPUT,
										input_device_index=input_device.index,
										stream_callback=callback)

	def start(self):
		self.stream.start_stream()

	def end(self):
		self.stream.stop_stream()
		self.stream.close()
		self.pyAudio.terminate()  
