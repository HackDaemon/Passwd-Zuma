from core.rule.rulemap import rulemap
from core.util import unpackList

from fn.uniform import map, reduce


rules =[
	rulemap['add'],
]

def run(classify):
	def applyRule(rule):
		def mapClass(className):
			return list(map(rule, classify[className]))
		return list(map(mapClass, classify))
	return list(map(applyRule ,unpackList(rules)))


if __name__ == '__main__':
	print rules

