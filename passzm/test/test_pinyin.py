# coding=utf-8
import unittest
from core import pinyin
from core.io import readRawFile
from core.sorter import pickup



class TestPinyin(unittest.TestCase):

	def test_hasHan(self):
			self.assertEqual(True, pinyin.hasHan(u'狗'))
			self.assertEqual(False, pinyin.hasHan(u'dog'))

	def test_han2Pinyin(self):
			self.assertEqual(pinyin.han2Pinyin(u'猫'), u'mao')
			self.assertEqual(pinyin.han2Pinyin(u'狗'), u'gou')
			self.assertEqual(pinyin.han2Pinyin(u'狼'), u'lang')
			self.assertEqual(pinyin.han2Pinyin(u'cat'), u'cat')

	def test_classPinyinify(self):
		rawtxt = readRawFile('test/data/simpleHasHan.txt')

		config, classify = pickup(rawtxt)
		rst = pinyin.classPinyinify(classify)
		self.assertEqual(rst[0][3], 'chaozhao')


if __name__ == '__main__':
	unittest.main()

