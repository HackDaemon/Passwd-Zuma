import unittest
from core.tactice import dog
from core.io import readRawFile
from core.sorter import pickup
from core.tactice import dog

class TestDog(unittest.TestCase):

	def test_run(self):
		rawtxt = readRawFile('test/data/simple.txt')
		config, classify = pickup(rawtxt)
		rst = dog.run(classify)
		self.assertEqual(rst[1][2][0][1], 'mahuafeng1234')


if __name__ == '__main__':
	unittest.main()
