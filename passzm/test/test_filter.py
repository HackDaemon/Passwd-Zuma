import unittest
from core import pfilter

class TestFilter(unittest.TestCase):

	def test_filterRepeat(self):
		testData = [
			'123456',
			'1234',
			'123456',
			'abcabc'
		]
		rst = pfilter.filterRepeat(testData)
		self.assertEqual( len(rst), 3)

if __name__ == '__main__':
	unittest.main()
