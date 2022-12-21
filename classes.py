import pyaudio
import rgbmatrix
from devices_class.audio_input import AudioInputDevice
from display_class.audio_formatter import AudioFormatter
from display_class.rgb_matrix_display import RgbMatrixDisplay
from stream_class.audio_stream import InputAudioStream

audioInputDevice = AudioInputDevice(pyAudio=pyaudio.PyAudio())

inputAudioStream = InputAudioStream(pyaudio=pyaudio)

displayProcessor = RgbMatrixDisplay(rgbmatrix=rgbmatrix, 
									AudioFormatterClass=AudioFormatter)

