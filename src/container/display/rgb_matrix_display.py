import rgbmatrix
import sys
import inspect
from src.data.audio_state import audio_state
from src.animations.loader import loadAnimation
from src.container.stream.audio_formatter import AudioFormatter as AudioFormatterType

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
        self.animation_loop_counter = 0
        self.increase_counter = True

    # sets the reference to the audio state
    def init(self, audio_state):
        self.audio_state = audio_state
        self.audioFormatter = self.AudioFormatterClass(
            audio_state['sample_rate'],
            self.config["matrix_rows"]
        )

    #sets the matrix options provided in config.json
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

    # launches the animation loop
    def animate(self):
        self.init_layout()

        Animation = loadAnimation(self.config['animation_name'])
        if (inspect.isclass(Animation) == False):
            print(Animation['error_msg'])
            return # abort animation


        animation = Animation(self.matrix, self.config)

        try:
            while True:
                if (self.is_audio_stream_ready()):
                    formatted_audio = self.audioFormatter.get_spectrum(self.audio_state['raw_audio'])
                    animation.animate(formatted_audio, self.animation_loop_counter)
                    self.set_animation_loop_counter()
        
        except KeyboardInterrupt:
            sys.exit(0)

    def set_animation_loop_counter(self):
        if (self.animation_loop_counter <= 0):
            self.increase_counter = True
        
        if (self.animation_loop_counter > self.config["animation_iterations_nb"]):
            self.increase_counter= False
        
        if (self.increase_counter == True):
            self.animation_loop_counter = self.animation_loop_counter + 1
        else:
            self.animation_loop_counter = abs(self.animation_loop_counter - 1)






