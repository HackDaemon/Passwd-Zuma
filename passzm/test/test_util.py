import unittest
from core import util

class TestUtil(unittest.TestCase):

	def test_unpackList(self):
		lists = [
			[1, 2, 3, 4],
			[1, 2, 3],
			[1, 2],
			[1]
		]
		rst = util.unpackList(lists)
		print rst
		self.assertEqual(len(rst), 10)


if __name__ == '__main__':
	unittest.main()
