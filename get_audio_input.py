import pyaudio
import math
import numpy
import time
import librosa

class AudioHandler():
    def __init__(self):
        self.pyAudio = pyaudio.PyAudio()
        self.stream: pyaudio.Stream
        self.microphone_device_index = -1
        self.microphone_sample_rate = -1
        self.CHUNKS = 8192

    def set_input_device(self, name=""):
        host_info = self.pyAudio.get_host_api_info_by_index(0)
        host_devices_number = host_info.get('deviceCount')

        for i in range(0, host_devices_number):
            device_has_input_channels = self.pyAudio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0
            device_name = self.pyAudio.get_device_info_by_host_api_device_index(0, i).get('name')

            if device_has_input_channels and name in device_name:
                self.microphone_device_index = i
                self.microphone_sample_rate = math.floor(self.pyAudio.get_device_info_by_host_api_device_index(0, i).get('defaultSampleRate'))
                break
    
    def stream_callback(in_data, frame_count, time_info, status):
        print(in_data)
        return (in_data, pyaudio.paContinue)

    def init_stream(self):
        self.stream = self.pyAudio.open(format=pyaudio.paFloat32,
                                        frames_per_buffer=self.CHUNKS,
                                        channels=1, 
                                        rate=self.microphone_sample_rate, 
                                        input=True, 
                                        input_device_index=self.microphone_device_index)

    def stream_start(self):
        self.stream.start_stream()
        while self.stream.is_active():
            data = numpy.fromstring(self.stream.read(self.CHUNKS, exception_on_overflow=False))
            stft_matrix = numpy.abs(librosa.stft(data))
            print(stft_matrix)
            time.sleep(0.5)


    def stream_end(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyAudio.terminate()  

audioHandler = AudioHandler()
audioHandler.set_input_device(name="Jabra EVOLVE LINK: USB Audio")
audioHandler.init_stream()
audioHandler.stream_start()
