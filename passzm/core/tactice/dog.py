from core.rule.rulemap import rulemap
from core.util import unpackList

from fn.uniform import map, reduce


rules =[
	rulemap['add'],
]

def run(classify):
	return list(map(map(unpackList, rules), classify))


if __name__ == '__main__':
	print rules

