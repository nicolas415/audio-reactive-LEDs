from typing import Any
import pyaudio
from src.container.devices.audio_input import AudioInputDevice
from src.data.audio_state import audio_state

class InputAudioStream():
	def __init__(self, pyaudio: pyaudio, config):
		self.pa = pyaudio
		self.pyAudio = pyaudio.PyAudio()
		self.stream: pyaudio.Stream
		self.DATA_CHUNKS = config['stream_data_chunks']
		self.FFT_FREQUENCY_BINS = config['fft_frequency_bins']
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
