
total = set()
for a in range(1, 9999):
	for b in range(a, 9999):
		if a < 999 or b < 999:
			product = a * b
			combined = str(product) + str(a) + str(b)
			if len(combined) == 9 and len(set(combined)) == 9 and '0' not in combined:
				print(a, b, product)
				total.add(product)
print(sum(total))