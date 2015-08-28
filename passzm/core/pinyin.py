# coding=utf-8
from pypinyin import lazy_pinyin

def hasHan(text):
	return all(u'\u4e00' <= char <= u'\u9fff' for char in text.decode("utf-8"))

def han2Pinyin(text):
	if hasHan(text):
		return lazy_pinyin(text)[0]
	else:
		return text


def classPinyinify(classify):
	def han2PinyinArr(className):
		return list(map(han2Pinyin, classify[className]))
	return list(map(han2PinyinArr, classify))
