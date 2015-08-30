
def readRawFile(path):
	f = open(path, 'r').read()
	return f

def op2Console(result):
	print '\n'.join(result)

def op2File(result, filename='output2.txt'):
	f = open(filename, 'w')
	map(f.write, result)
	f.close()
