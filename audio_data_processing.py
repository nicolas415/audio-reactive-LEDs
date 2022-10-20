import numpy

class AudioDataProcessing():
    def __init__(self, microphone_sample_rate):
        self.microphone_sample_rate = microphone_sample_rate

    # gets the loudest frequency range for a given fft
    # returns the highest frequency of the range and the lowest frequency of the range
    def get_loudest_frequency_range_from_fft(self, fft=[]):
        absolute_fft = numpy.abs(fft)
        hertz_frequencies = self.get_hz_frequencies_array(fft=absolute_fft)
        filtered_fft = self.filter_fft(min_frequency=10,
                                       max_frequency=16000,
                                       abs_fft=absolute_fft,
                                       hz_frequencies=hertz_frequencies)

        loudest_fft_index = numpy.argmax(filtered_fft)
        return self.get_frequency_range(fft_index=loudest_fft_index, hz_frequencies=hertz_frequencies)
         

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
    def get_hz_frequencies_array(self, fft=[]):
        frequencies_array = numpy.fft.rfftfreq(round(len(fft)) * 2 - 1)
        return frequencies_array * self.microphone_sample_rate