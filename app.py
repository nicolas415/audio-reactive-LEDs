from instances import audioInputDevice, inputAudioStream, displayProcessor
from processors.display_processor import DisplayProcessor
from data.audio_state import audio_state

audioInputDevice.set_device_by_name(target_name="Built-in")
inputAudioStream.init(audioInputDevice, audio_state)
displayProcessor.init(audio_state)

inputAudioStream.start()
displayProcessor.animate()