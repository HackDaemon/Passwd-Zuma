
def pickup(filestr):
	lines = filestr.split('\n')
	config = pickupConfig(lines)
	classify = pickupClass(lines)
	print config
	print classify
	# return config, classify

def pickupConfig(lines):
	for line in lines:
		if line.strip() == '[config]':
			pass


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




