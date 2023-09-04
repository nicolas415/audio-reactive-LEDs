import rgbmatrix
import sys
import math
import inspect
from PIL import Image
from src.data.audio_state import audio_state
from src.animations.loader import loadAnimation
from src.container.stream.audio_formatter import AudioFormatter as AudioFormatterType
from src.animations.spectrum import SpectrumAnimation
from src.animations.samus_anim import SamusAnimation
from src.animations.rotate_square import RotateSquareAnimation

class RgbMatrixDisplay():
    """
    DISPLAY CLASS
    """
    def __init__(self, rgbmatrix: rgbmatrix, AudioFormatterClass: AudioFormatterType, config):
        self.RGBMatrix = rgbmatrix.RGBMatrix
        self.RGBMatrixOptions = rgbmatrix.RGBMatrixOptions
        self.matrix: rgbmatrix.RGBMatrix()
        self.AudioFormatterClass = AudioFormatterClass
        self.audioFormatter: AudioFormatterType
        self.config = config

    def init(self, audio_state):
        self.audio_state = audio_state
        self.audioFormatter = self.AudioFormatterClass(audio_state['sample_rate'])

    def init_layout(self):
        options = self.RGBMatrixOptions()
        options.parallel = 1
        options.rows = self.config['matrix_rows']
        options.cols = self.config['matrix_columns']
        options.chain_length = self.config['matrix_chain_length']
        options.brightness = self.config['matrix_brightness']
        options.hardware_mapping = self.config['matrix_hardware_mapping']  # If you have an Adafruit HAT: 'adafruit-hat'

        self.matrix = self.RGBMatrix(options = options)
    
    def is_audio_stream_ready(self):
        if (len(self.audio_state['raw_audio']) > 0):
            return True
        else:
            return False


    def animate(self):
        self.init_layout()

        Animation = loadAnimation(self.config['animation_name'])
        if (inspect.isclass(Animation) == False):
            print(Animation['error_msg'])
            return # abort animation


        animation = Animation(self.matrix)

        try:
            while True:
                if (self.is_audio_stream_ready()):
                    formatted_audio = self.audioFormatter.get_spectrum(self.audio_state['raw_audio'])
                    ### animate
                    animation.animate(formatted_audio)

        except KeyboardInterrupt:
            sys.exit(0)






