import unittest
from core import io
from core import sorter
from core import util
from core.tactice import dog

class TestIO(unittest.TestCase):

	def test_read(self):
		raw = open('test/data/simple.txt', 'r').read()
		ioreaded = io.readRawFile('test/data/simple.txt')
		self.assertEqual(raw, ioreaded)

	def test_op2File(self):
		rawtxt = io.readRawFile('test/data/simple.txt')
		config, classify = sorter.pickup(rawtxt)
		rst = dog.run(classify)
		output = '\n'.join(util.unpackStrListRecur(rst))
		io.op2File(output, 'myoutput.txt')

if __name__ == '__main__':
	unittest.main()
