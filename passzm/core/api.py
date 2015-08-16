import .transformer
import .io

def generate(rawPath):
	try:
		raw = io.readRawFile(rawPath)
	except IOError
		return IOError

