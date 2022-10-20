import pyaudio
import math
import numpy
from audio_data_processing import AudioDataProcessing

class InputStreamHandler():
    def __init__(self):
        self.pyAudio = pyaudio.PyAudio()
        self.stream: pyaudio.Stream
        self.microphone_device_index = -1
        self.microphone_sample_rate = -1
        self.CHUNKS = 1024
        self.FFT_FREQUENCY_BINS = 256
        self.audioProcessing = None


    # sets the input of the audio stream, taking a substring of the device name
    def set_input_device(self, name=""):
        host_info = self.pyAudio.get_host_api_info_by_index(0)
        host_devices_number = host_info.get('deviceCount')

        for i in range(0, host_devices_number):
            device_has_input_channels = self.pyAudio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0
            device_name = self.pyAudio.get_device_info_by_host_api_device_index(0, i).get('name')
            print(self.pyAudio.get_device_info_by_host_api_device_index(0, i))

            if device_has_input_channels and name in device_name:
                self.microphone_device_index = i
                self.microphone_sample_rate = math.floor(self.pyAudio.get_device_info_by_host_api_device_index(0, i).get('defaultSampleRate'))
                self.audioProcessing = AudioDataProcessing(self.microphone_sample_rate)
                break


    # creates an audio input stream
    def init_stream(self):
        self.stream = self.pyAudio.open(format=pyaudio.paFloat32,
                                        frames_per_buffer=self.CHUNKS,
                                        channels=1, 
                                        rate=self.microphone_sample_rate, 
                                        input=True, 
                                        input_device_index=self.microphone_device_index)


    # starts the stream
    def stream_start(self):
        self.stream.start_stream()
        while self.stream.is_active():
            data = numpy.fromstring(self.stream.read(self.CHUNKS, exception_on_overflow=False))
            self.stream_callback(data=data)


    # function called with the data received from the live stream
    def stream_callback(self, data=[]):
            fft_matrix = numpy.fft.fft(data, n=self.FFT_FREQUENCY_BINS)
            high_frequency, low_frequency =  self.audioProcessing.get_loudest_frequency_range_from_fft(fft=fft_matrix)
            print(f'{round(low_frequency)} Hz - {round(high_frequency)} Hz')


    # stops the stream
    def stream_end(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyAudio.terminate()  