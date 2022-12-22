import pyaudio
import rgbmatrix
from src.devices.audio_input import AudioInputDevice
from src.display_class.audio_formatter import AudioFormatter
from src.display_class.rgb_matrix_display import RgbMatrixDisplay
from src.stream_class.audio_stream import InputAudioStream

audioInputDevice = AudioInputDevice(pyAudio=pyaudio.PyAudio())
inputAudioStream = InputAudioStream(pyaudio=pyaudio)
displayProcessor = RgbMatrixDisplay(rgbmatrix=rgbmatrix, 
									AudioFormatterClass=AudioFormatter)

