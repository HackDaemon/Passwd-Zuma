from core.rule.rulemap import rulemap
from core.util import unpackList, unpackStrListRecur

from fn.uniform import map, reduce

def run(classify):
	def applyTransformRule(rule):
		def mapClass(className):
			return list(map(rule, classify[className]))
		return list(map(mapClass, classify))
	def applyAddRule(rule):
		return list(map(rule, unpackStrListRecur(list(map(applyTransformRule, rulemap['transform'])))))
	return list(map(applyAddRule, rulemap['add']))

if __name__ == '__main__':
	print rules

