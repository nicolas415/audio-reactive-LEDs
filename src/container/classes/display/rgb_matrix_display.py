import rgbmatrix
import sys
import math
from PIL import Image
from src.data.audio_state import audio_state
from src.container.classes.stream.audio_formatter import AudioFormatter as AudioFormatterType
from src.animations.spectrum import SpectrumAnimation
from src.animations.samus_anim import SamusAnimation
from src.animations.rotate_square import RotateSquareAnimation

class RgbMatrixDisplay():
    """
    DISPLAY CLASS
    """
    def __init__(self, rgbmatrix: rgbmatrix, AudioFormatterClass: AudioFormatterType):
        self.RGBMatrix = rgbmatrix.RGBMatrix
        self.RGBMatrixOptions = rgbmatrix.RGBMatrixOptions
        self.matrix: rgbmatrix.RGBMatrix()
        self.AudioFormatterClass = AudioFormatterClass
        self.audioFormatter: AudioFormatterType
        self.bar_size = 4
        self.bar_padding = 2
        self.bar_color = [0, 0, 0]
        self.COLS = 32
        self.ROWS = 32

    def init(self, audio_state):
        self.audio_state = audio_state
        self.audioFormatter = self.AudioFormatterClass(audio_state['sample_rate'])

    def init_layout(self):
        options = self.RGBMatrixOptions()
        options.rows = self.ROWS
        options.cols = self.COLS
        options.chain_length = 2
        options.parallel = 1
        options.brightness = 100
        options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

        self.matrix = self.RGBMatrix(options = options)
    
    def is_audio_stream_ready(self):
        if (len(self.audio_state['raw_audio']) > 0):
            return True
        else:
            return False


    def animate(self):
        self.init_layout()
        ### instanciate animation
        # animation 1
        # rotateSquareAnimation = RotateSquareAnimation(self.matrix)
        # animation 2
        # samusAnimation = SamusAnimation(self.matrix)
        # animation 3
        spectrumAnimation = SpectrumAnimation(self.matrix)  

        try:
            while True:
                if (self.is_audio_stream_ready()):
                    formatted_audio = self.audioFormatter.get_spectrum(self.audio_state['raw_audio'])
                    ### animate
                    # animation 1
                    # rotateSquareAnimation.animate(formatted_audio)
                    # animation 2
                    # samusAnimation.animate(formatted_audio)
                    # animation 3
                    spectrumAnimation.animate(formatted_audio)


        except KeyboardInterrupt:
            sys.exit(0)






