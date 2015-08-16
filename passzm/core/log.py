import logging
import sys

LOGGER = logging.getLogger('passzm')

LOGGER_HANDLER = None
try:
		from thirdparty.ansistrm import ColorizingStreamHandler

		disableColor = False

		if disableColor:
				LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
		else:
				LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
except ImportError:
		LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FORMATTER = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")

LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(logging.INFO)
