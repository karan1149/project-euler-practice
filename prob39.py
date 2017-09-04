from collections import defaultdict
import math

sieve = {}

for a in range(1, 750):
	for b in range(a + 1, 750):
		c = math.sqrt(a**2 + b**2) 
		if c.is_integer():
			if (a, b, c) not in sieve:
				sieve[(a, b, c)] = True
				i = 2
				while c * i < 750:
					sieve[(a * i, b * i, c * i)] = False
					i += 1

print sieve

solutions = [0] * 1001
curr_max = 0
curr_p_max = -1
for p in range(1001):
	for triple in sieve.iterkeys():
		if triple[0] + triple[1] + triple[2] == p:
			solutions[p] += 1
			if solutions[p] > curr_max:
				curr_max = solutions[p]
				curr_p_max = p

print(curr_p_max)


