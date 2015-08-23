# coding=utf-8
from pypinyin import lazy_pinyin

def hasHan(text):
	# for python 2.x, 3.3+
	# sample: ishan(u'一') == True, ishan(u'我&&你') == False
	#http://luopuya.github.io/2014/03/29/Python%20%E5%88%A4%E6%96%AD%E6%B1%89%E5%AD%97%E5%AD%97%E7%AC%A6/
	return all(u'\u4e00' <= char <= u'\u9fff' for char in text)

def han2Pinyin(text):
	return lazy_pinyin(text)
