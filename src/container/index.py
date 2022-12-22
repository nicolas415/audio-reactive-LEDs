import pyaudio
import rgbmatrix
from src.container.classes.devices.audio_input import AudioInputDevice
from src.container.classes.display.rgb_matrix_display import RgbMatrixDisplay
from src.container.classes.stream.audio_formatter import AudioFormatter
from src.container.classes.stream.audio_stream import InputAudioStream

audioInputDevice = AudioInputDevice(pyAudio=pyaudio.PyAudio())
inputAudioStream = InputAudioStream(pyaudio=pyaudio)
displayProcessor = RgbMatrixDisplay(rgbmatrix=rgbmatrix, 
									AudioFormatterClass=AudioFormatter)

