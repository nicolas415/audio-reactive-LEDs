import pyaudio
import rgbmatrix
from src.container.devices.audio_input import AudioInputDevice
from src.container.display.rgb_matrix_display import RgbMatrixDisplay
from src.container.stream.audio_formatter import AudioFormatter
from src.container.stream.audio_stream import InputAudioStream

audioInputDevice = AudioInputDevice(pyAudio=pyaudio.PyAudio())
inputAudioStream = InputAudioStream(pyaudio=pyaudio)
displayProcessor = RgbMatrixDisplay(rgbmatrix=rgbmatrix, AudioFormatterClass=AudioFormatter)

