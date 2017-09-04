def get_divisors(num):
	i = 1
	divisors = set()
	while i * i <= num:
		if num % i == 0:
			divisors.add(i)
			divisors.add(num / i)
		i += 1
	return divisors


def get_denominator(num, denom):
	print(num, denom)
	num_divisors = get_divisors(num)
	denom_divisors = get_divisors(denom)
	common_divisors = num_divisors & denom_divisors
	print(num_divisors, denom_divisors, common_divisors)
	while True:
		try:
			divisor = common_divisors.pop()
			if divisor != 1:
				break
		except:
			return denom
	return get_denominator(num / divisor, denom / divisor)





final_numerator = 1.0
final_denominator = 1.0

for numerator in range(10, 100):
	for denominator in range(numerator + 1, 100):
		if '0' not in str(numerator) and '0' not in str(denominator):
			if numerator / float(denominator) == float(str(numerator)[0]) / float(str(denominator)[1]) and str(numerator)[1] == str(denominator)[0] or numerator / float(denominator) == float(str(numerator)[1]) / float(str(denominator)[0]) and str(numerator)[1] == str(denominator)[0]:
				print(numerator, denominator)
				final_numerator *= numerator
				final_denominator *= denominator

print(get_denominator(final_numerator, final_denominator))


