# AUDIO_PIXEL project structure

## Main files
`app.py`
* set device input name (scan devices, select device etc...)
* set animation settings
* set input/output signal settings
* play/pause program

`settings/ (.json files)`
* audio and animation settings
* input/output devices settings


## Class that handles external devices ✅
`devices_handlers/`
* Search and select devices
* Manipulated by stream_handler


## Classes that processes the audio signal ✅
`display_processing/`
* takes structured data and settings
* converts data for the display device
* passes converted signal to the display device

`audio_processing/`
* takes signal from a stream
* converts it to structured data
* passes structured data to display_processing


## Class handles the input audio stream and feeds the processors with a signal ✅
`stream_handler/`
* manages the audio stream
* creates, plays and stops the stream
* passes the streamed signal to audio_processing