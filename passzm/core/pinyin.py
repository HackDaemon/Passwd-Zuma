# coding=utf-8
from pypinyin import lazy_pinyin



def hasHan(text):
	if isinstance(text, unicode):
		xtext = text
	else:
		xtext = unicode(text,'utf-8')
	return all(u'\u4e00' <= char <= u'\u9fff' for char in xtext)

def han2Pinyin(text):
	if hasHan(text):
		if isinstance(text, unicode):
			xtext = text
		else:
			xtext = unicode(text,'utf-8')
		return lazy_pinyin(xtext)[0]
	else:
		return text


def classPinyinify(classify):
	def han2PinyinArr(className):
		return list(map(han2Pinyin, classify[className]))
	return list(map(han2PinyinArr, classify))
