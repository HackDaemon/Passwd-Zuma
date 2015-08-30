import unittest
from core.io import readRawFile
from core.sorter import pickup
from core.tactice import cat

class TestCat(unittest.TestCase):
	def test_run(self):
		rawtxt = readRawFile('test/data/simple.txt')
		config, classify = pickup(rawtxt)
		rst = cat.run(classify)
		self.assertEqual(rst[0][1][0], '123tnecnet')

if __name__ == '__main__':
	unittest.main()
