from fn.uniform import map, reduce

def unpackList(lists):
	return list(reduce( (lambda x, y: x + y ), lists))

def unpackStrList(lists):
	def reduceStr(total, s):
		if isinstance(s, list):
				return total + s
		else:
				total.append(s)
				return total
	return list(reduce(reduceStr, lists, []))

def unpackStrListRecur(lists):
	if any(isinstance(s, list) for s in lists):
		return unpackStrListRecur(unpackStrList(lists))
	else:
		return lists
