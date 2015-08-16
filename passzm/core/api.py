import core.transformer
import core.io
import core.log

def generate(rawPath):
	try:
		raw = io.readRawFile(rawPath)
	except IOError:
		return IOError

