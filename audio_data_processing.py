import numpy

class AudioDataProcessing():
    def __init__(self, microphone_sample_rate):
        self.microphone_sample_rate = microphone_sample_rate
        self.AMPLITUDE_REFERENCE = 5.25e-05
        self.fft = []
        self.FILTER_MAX = 16000
        self.FILTER_MIN = 20

    
    def set_fft(self, fft=[]):
        self.fft = fft
        self.absolute_fft = numpy.abs(fft)
        self.hz_frequencies_array = self.get_hz_frequencies_array()
        self.filtered_fft = self.filter_fft(max_frequency=self.FILTER_MAX, 
                                            min_frequency=self.FILTER_MIN, 
                                            abs_fft=self.absolute_fft, 
                                            hz_frequencies=self.hz_frequencies_array)

    # gets the loudest frequency range for a given fft
    # returns the highest frequency of the range and the lowest frequency of the range
    def get_loudest_frequency_range_from_fft(self):
        loudest_fft_index = numpy.argmax(self.filtered_fft)
        return self.get_frequency_range(fft_index=loudest_fft_index, hz_frequencies=self.hz_frequencies_array)
    

    def get_loudest_volume_from_fft(self):
        # return numpy.max(self.filtered_fft)
        loudest_amplitude = numpy.max(self.filtered_fft)
        loudest_decibel = 20 * numpy.log10(loudest_amplitude / self.AMPLITUDE_REFERENCE)
        return round(loudest_decibel)

    def get_volume_of_fft_index(self, index=0):
        fft_amplitude = self.filtered_fft[index]

        if fft_amplitude == 0:
            return -500
        else:
            return 20 * numpy.log10(fft_amplitude / self.AMPLITUDE_REFERENCE)

    def get_frequency_of_fft_index(self, index=0):
        return self.filtered_fft[index]


    # filters a fft, given a minimum frequency, a maximum frequency, an absolute fft
    # and a mapping array of the fft fequencies in hertz
    def filter_fft(self, min_frequency=20, max_frequency=16000, abs_fft=[], hz_frequencies=[]):
        return numpy.where(numpy.logical_and(hz_frequencies > min_frequency, hz_frequencies < max_frequency), abs_fft, 0)


    # gets the frequency range of a given fft index and a mapping array of the fft frequencies in hertz
    def get_frequency_range(self, fft_index=0, hz_frequencies=[]):
        low_frequency = hz_frequencies[fft_index]

        if fft_index != len(hz_frequencies) -1:
            high_frequency = hz_frequencies[fft_index + 1]
        else:
            hz_frequencies = hz_frequencies[len(hz_frequencies) - 1]

        return high_frequency, low_frequency

    # gets a mapping array of the fft frequencies in hertz, given an fft and it corresponding sample rate
    def get_hz_frequencies_array(self):
        absolute_fft = numpy.abs(self.fft)
        frequencies_array = numpy.fft.rfftfreq(round(len(absolute_fft)) * 2 - 1)
        return frequencies_array * self.microphone_sample_rate
