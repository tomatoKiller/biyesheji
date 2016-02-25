
import sys

CqiToDataRate = [
	0, 
	25.59, 
	39.38, 
	63.34, 
	101.07, 
	147.346, 
	197.53, 
	248.07, 
	321.57, 
	404.26,
	458.72,
	558.15,
	655.59,
	759.93,
	859.35,
	933.19
]


fp = open(sys.argv[1])

throughput = 0
slot = 0

for line in fp:
	line = line.strip('\n')
	term = line.split('\t')
	if slot == term[0]:
		throughput += CqiToDataRate[int(term[-2])]
	else:
		slot = term[0]
		if slot != 0:
			print throughput
		throughput = 0

