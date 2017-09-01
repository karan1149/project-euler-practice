total = 0
for i in range(2, 354294):
	if sum(int(digit)**5 for digit in str(i)) == i:
		print(i)
		total += i
print(total)

