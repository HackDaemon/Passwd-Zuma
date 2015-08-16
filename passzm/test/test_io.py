import unittest
from core import io

class TestIO(unittest.TestCase):

	def test_read(self):
		raw = open('test/data/simple.txt', 'r').read()
		ioreaded = io.readRawFile('test/data/simple.txt')
		self.assertEqual(raw, ioreaded)


if __name__ == '__main__':
	unittest.main()
