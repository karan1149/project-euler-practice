largest = float("-inf")

for i in range(1, 9999):
	curr_n = 2
	curr_str = str(i)
	while len(curr_str) < 9:
		curr_str += str(i * curr_n)
		curr_n += 1
	if len(curr_str) == 9 and len(set(curr_str)) == 9 and '0' not in curr_str:
		print(curr_str, curr_n - 1, i)
		largest = max(largest, int(curr_str))

print(largest)
