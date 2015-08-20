# coding=utf-8
import unittest
from core import pinyin

class TestPinyin(unittest.TestCase):

	def test_hasHan(self):
		self.assertEqual(True, pinyin.hasHan(u'狗'))
		self.assertEqual(False, pinyin.hasHan(u'dog'))

	def test_han2Pinyin(self):
		self.assertEqual(pinyin.han2Pinyin(u'猫')[0], u'mao')
		self.assertEqual(pinyin.han2Pinyin(u'狗')[0], u'gou')
		self.assertEqual(pinyin.han2Pinyin(u'狼')[0], u'lang')
		self.assertEqual(pinyin.han2Pinyin(u'cat')[0], u'cat')


if __name__ == '__main__':
	unittest.main()

