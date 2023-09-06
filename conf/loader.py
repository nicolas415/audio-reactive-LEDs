import json
# path of the config file is relative to where `start.py` is launched
with open('./config.json') as config_file:
	file_contents = config_file.read()
	config = json.loads(file_contents)