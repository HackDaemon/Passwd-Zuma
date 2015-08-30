import unittest
from core import sorter
from core.io import readRawFile

class TestSorter(unittest.TestCase):
	def test_pickConfig(self):
		rawtxt = readRawFile('test/data/simple.txt')
		config, classify = sorter.pickup(rawtxt)
		self.assertEqual(config['verbose'], 'True')

	def test_pickupClass(self):
		rawtxt = readRawFile('test/data/simple.txt')
		config, classify = sorter.pickup(rawtxt)
		self.assertEqual(classify['place'][0], 'shenzhen')

	def test_abbreviation(self):
		rawtxt = readRawFile('test/data/simpleHasHan.txt')
		config, classify = sorter.pickup(rawtxt)
		rst = sorter.pickupExtra(classify)
		self.assertEqual(len(rst), 2)
		self.assertEqual(rst[0],'mht')

	def test_pickup(self):
		rawtxt = readRawFile('test/data/simpleHasHan.txt')
		config, classify = sorter.pickup(rawtxt)
		print classify['extra']
		self.assertEqual(classify['extra'][0], 'mht')

if __name__ == '__main__':
	unittest.main()
