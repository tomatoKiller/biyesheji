
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
line_num = 0
begin = False

for line in fp:
	line = line.strip('\n')
	term = line.split('\t')
	if term[0] == '0.042':
		begin = True

	if begin == False:
		continue

	throughput += CqiToDataRate[int(term[-2])]
	# if slot == term[0]:
	# 	throughput += CqiToDataRate[int(term[-2])]
		
	if slot != term[0]:
		line_num+=1
			# print throughput
		slot = term[0]
		# throughput = 0

print throughput / line_num
