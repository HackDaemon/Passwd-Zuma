from fn import _, iters
from fn.uniform import map
from core import pinyin

def pickup(filestr):
	lines = filestr.split('\n')
	config = pickupConfig(lines)
	classify = pickupClass(lines)
	extra = pickupExtra(classify)
	classify['extra'] = extra
	return config, classify

def pickupConfig(lines):
	start = False
	config = {}
	for line in lines:
		line = line.strip()
		if line == '':
			continue
		if line == '[config]':
			start = True
		else:
			if line[0] == '[':
				break
			elif start is True:
				kv = line.split('=')
				key = kv[0].strip()
				value = kv[1].strip()
				config[key] = value
	return config


def pickupClass(lines):
	currentClass = ''
	classify = {}
	for line in lines:
		if line.strip() != '':
			if line.strip()[0] == '[':
				if line.strip() != '[config]':
					currentClass = line.strip()[1:-1]
					classify[currentClass] = []
			elif currentClass != '':
				classify[currentClass].append(line.strip())
	return classify

def pickupExtra(classify):
	return list(filter
							(_ != None, list(map(abbreviation, [name for name in classify['name']]))))

def abbreviation(name):
	def takeFirst(chichar):
		return chichar[0]
	if pinyin.hasHan(name) is True:
		return ''.join(list(map(_[0], pinyin.segmentation(name))))
