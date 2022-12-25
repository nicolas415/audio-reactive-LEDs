from src.container.index import audioInputDevice, inputAudioStream, displayProcessor
from src.data.audio_state import audio_state

class App():
	def __init__(self):
		audioInputDevice.set_device_by_name()
		inputAudioStream.init(audioInputDevice, audio_state)
		displayProcessor.init(audio_state)
	

	def start(self):
		inputAudioStream.start()
		displayProcessor.animate()