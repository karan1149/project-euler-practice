import math

total = 0

cache = {}
for i in range(0, 100):
	cache[i] = math.factorial(int(str(i)[0]))
	if len(str(i)) > 1:
		cache[i] += math.factorial(int(str(i)[1]))
print("done caching")

for i in range(3, 2540160):
	curr_total = 0
	num_string = str(i)
	j = 0
	while j < len(num_string):
		curr_total += cache[int(num_string[j:j + 2])]
		j += 2
	if i == curr_total:
		total += i

print total