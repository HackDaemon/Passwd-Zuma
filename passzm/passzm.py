import sys

import core.io as io
import core.zuma as zuma
import core.log

import logging

logger = logging.getLogger('passzm')

def main():
	if len(sys.argv) > 2 or len(sys.argv) == 1:
		logger.error('Invalid number of parameters, the program can not be executed!')
		logger.error('Program going to exit!')
		sys.exit()
	try:
		path = sys.argv[1]
		rawtxt = io.readRawFile(path)
		result = zuma.spiral(rawtxt)
	except IOError:
		logger.error('Not such data file!')


if __name__ == '__main__':
	main()
