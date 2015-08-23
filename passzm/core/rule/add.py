from fn import _

strs = [
	'123',
	'1234',
	'123456',
	'456',
	'789',
	'abc',
	'111',
	'234'
	'qwerty'
	'qwe'
	'888'
	'666'
	'555',
	'444',
	'333',
	'222',
	'999',
	'000',
	'abab',
	'bbbb',
	'ccc',
	'bbb',
]

def addAfter(mate):
	return list(map(mate + _, strs))

def addBefore(mate):
	return list(map(_ + mate, strs))

