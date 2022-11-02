import PySimpleGUI
from data.audio_state import audio_state

class DisplayProcessor():
	"""
	DISPLAY PROCESSOR
	"""
	def __init__(self, PySimpleGUI: PySimpleGUI):
		self.sg = PySimpleGUI
		self.window: PySimpleGUI.Window
		self.audio_state: audio_state
		self.layout_width = 1000
		self.layout_height = 500
		self.frame_timeout = 5
		self.display = { 'bars': { 'column': 0, 'color': '', 'amplitude': 0}, 'bar_size': 10, 'bar_padding': 2 }

	def init(self, audio_state):
		self.audio_state = audio_state

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
		for col, val in enumerate(self.audio_state['formatted_audio']):
			self.display['bars']['column'] = col

			for bar in range(0, int(val)):
				self.display['bars']['amplitude'] = val
				
				if bar < 3:
					self.display['bars']['color'] = '#00FF0E'
				elif bar < 6:
					self.display['bars']['color'] = 'yellow'
				elif bar < 9:
					self.display['bars']['color'] = 'orange'
				else:
					self.display['bars']['color'] = 'red'

				self.render_animation(col, bar)


	def render_animation(self, col, val):
		barStep = self.display['bar_size']
		pad = self.display['bar_padding']
		# col = self.display['bars']['column']
		# bar = self.display['bars']['amplitude']
		color = self.display['bars']['color']
		

		self.window['graph'].draw_rectangle(top_left=((col*barStep)+pad, barStep*(val+1)),
											bottom_right=((col*barStep)+barStep,(val*barStep)+pad),
											line_color='black',
											line_width=2,
											fill_color='white')  # Conditional
