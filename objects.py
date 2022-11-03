import pyaudio
import PySimpleGUI
from devices_class.audio_input import AudioInputDevice
from display_class.audio_formatter import AudioProcessor
from display_class.simple_gui_display import SimpleGuiDisplay
from stream_class.audio_stream import InputAudioStream

audioInputDevice = AudioInputDevice(pyAudio=pyaudio.PyAudio())

inputAudioStream = InputAudioStream(pyaudio=pyaudio)

displayProcessor = SimpleGuiDisplay(PySimpleGUI=PySimpleGUI, 
									AudioProcessorClass=AudioProcessor)

