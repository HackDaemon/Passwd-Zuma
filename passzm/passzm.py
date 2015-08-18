import sys

import core.io as io
import core.zuma as zuma
import core.log

import logging

logger = logging.getLogger('passzm')

def main():
	if len(sys.argv) > 2:
		logger.critical('Invalid number of parameters, the program can not be executed!')
		logger.critical('Program going to exit!')
		sys.exit()

	path = sys.argv[1]
	rawtxt = io.readRawFile(path)
	result = zuma.spiral(rawtxt)


if __name__ == '__main__':
	main()
