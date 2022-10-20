from input_stream_handler import InputStreamHandler

inputStreamHandler = InputStreamHandler()
inputStreamHandler.set_input_device(name="KT USB Audio")
inputStreamHandler.init_stream()
inputStreamHandler.stream_start()