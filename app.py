from classes import audioInputDevice, inputAudioStream, displayProcessor
from data.audio_state import audio_state

audioInputDevice.set_device_by_name(target_name="KT USB Audio")
inputAudioStream.init(audioInputDevice, audio_state)
displayProcessor.init(audio_state)

inputAudioStream.start()
displayProcessor.animate()