from itertools import groupby
from operator import itemgetter
a=[
	{"n": 1, "v": 1},
	{"n": 1, "v": -1},
	{"n": 2, "v": 2}
]
getter = itemgetter("n")
b = sorted(a, key = getter)
result = groupby(b, getter)
for k, v in result:
	print k
	for r in v:
		print r
