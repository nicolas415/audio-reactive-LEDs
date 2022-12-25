import json

with open('conf/config.json') as config_file:
	file_contents = config_file.read()
	config = json.loads(file_contents)