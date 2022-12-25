import pyaudio
import rgbmatrix
from src.container.devices.audio_input import AudioInputDevice
from src.container.display.rgb_matrix_display import RgbMatrixDisplay
from src.container.stream.audio_formatter import AudioFormatter
from src.container.stream.audio_stream import InputAudioStream
from conf.loader import config

audioInputDevice = AudioInputDevice(pyAudio=pyaudio.PyAudio(), config=config)
inputAudioStream = InputAudioStream(pyaudio=pyaudio, config=config)
displayProcessor = RgbMatrixDisplay(rgbmatrix=rgbmatrix, AudioFormatterClass=AudioFormatter, config=config)

