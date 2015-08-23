import unittest
from core.rule import add

class TestRule(unittest.TestCase):

	def test_addAfter(self):
		rst = add.addAfter('feng')
		self.assertEqual(rst[0], 'feng123')

	def test_addBefore(self):
		rst = add.addBefore('junzi')
		rst = add.addBefore('123junzi')

if __name__ == '__main__':
	unittest.main()
