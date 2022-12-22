from src.container.classes import audioInputDevice, inputAudioStream, displayProcessor
from src.data.audio_state import audio_state

class AudioProcessor():
	def __init__(self):
		audioInputDevice.set_device_by_name(target_name="KT USB Audio")
		inputAudioStream.init(audioInputDevice, audio_state)
		displayProcessor.init(audio_state)
	

	def start(self):
		inputAudioStream.start()
		displayProcessor.animate()