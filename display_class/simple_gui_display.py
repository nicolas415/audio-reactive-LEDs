import PySimpleGUI
from data.audio_state import audio_state
from display_class.audio_formatter import AudioProcessor as AudioProcessorType

class SimpleGuiDisplay():
	"""
	DISPLAY PROCESSOR
	"""
	def __init__(self, PySimpleGUI: PySimpleGUI, AudioProcessorClass: AudioProcessorType):
		self.sg = PySimpleGUI
		self.window: PySimpleGUI.Window
		self.AudioProcessorClass = AudioProcessorClass
		self.audioProcessor: AudioProcessorType
		
		self.audio_state: audio_state
		self.layout_width = 1000
		self.layout_height = 500
		self.frame_timeout = 5
		self.bar_size = 10
		self.bar_padding = 2
		self.bar_color = 'white'
		self.amplitude: int
		self.column: int

	def init(self, audio_state):
		self.audio_state = audio_state
		self.audioProcessor = self.AudioProcessorClass(audio_state['sample_rate'])

	def init_layout(self):
		layout = [[self.sg.Graph(canvas_size=(self.layout_width, self.layout_height),
                    graph_bottom_left=(0, 0),
                    graph_top_right=(200, 100),
                    background_color='#809AB6',
                    key='graph')]]
		self.window = self.sg.Window('Mic to waveform plot + Max Level', layout, finalize=True)

	def animate(self):
		self.init_layout()

		while True:
			event, values = self.window.read(timeout=self.frame_timeout)
			self.window['graph'].erase()
			self.process_formatted_audio()

	def process_formatted_audio(self):
		formatted_audio = self.audioProcessor.get_formatted_fft(self.audio_state['raw_audio'])
		
		for col, val in enumerate(formatted_audio):
			self.column = col

			for bar in range(0, int(val)):
				self.amplitude = val
				
				if bar < 3:
					self.bar_color = '#00FF0E'
				elif bar < 6:
					self.bar_color = 'yellow'
				elif bar < 9:
					self.bar_color = 'orange'
				else:
					self.bar_color = 'red'

				self.render_animation(col, bar)


	def render_animation(self, col, val):
		barStep = self.bar_size
		pad = self.bar_padding
		# col = self.display['bars']['column']
		# bar = self.display['bars']['amplitude']
		# color = self.display['bars']['color']
		

		self.window['graph'].draw_rectangle(top_left=((col*barStep)+pad, barStep*(val+1)),
											bottom_right=((col*barStep)+barStep,(val*barStep)+pad),
											fill_color=self.bar_color)  # Conditional
