import pyaudio
import PySimpleGUI
from devices.audio_input import AudioInputDevice
from processors.audio_processor import AudioProcessor
from processors.display_processor import DisplayProcessor
from stream.audio_stream import InputAudioStream

audioInputDevice = AudioInputDevice(pyAudio=pyaudio.PyAudio())
inputAudioStream = InputAudioStream(pyaudio=pyaudio, AudioProcessor=AudioProcessor)
displayProcessor = DisplayProcessor(PySimpleGUI=PySimpleGUI)