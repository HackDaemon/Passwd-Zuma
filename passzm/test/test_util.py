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
		self.assertEqual(len(rst), 10)

	def test_unpackListRecur(self):
		lists = [
			[88, 2, 3, 4],
			[1, 2, 3],
			[1, 2],
			[1],
			[5],
			[11,[
				12, 13, 14, 15, [
					's', 'b'
				]
			]]
		]
		rst = util.unpackStrListRecur(lists)
		self.assertEqual(len(rst), 18)


if __name__ == '__main__':
	unittest.main()
