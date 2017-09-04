def get_base_10_digit(n, digit):
	return n / 10**digit % 10

def get_base_10_length(n):
	length = 0
	while n:
		n /= 10
		length += 1
	return length

def check_base_10(n):
	length = get_base_10_length(n)
	left = length - 1
	right = 0

	while right < left:
		if get_base_10_digit(n, right) != get_base_10_digit(n, left):
			return False
		right += 1
		left -= 1
	return True

def get_base_2_digit(n, digit):
	return (n >> digit) & 1

def get_base_2_length(n):
	length = 0
	while n:
		n >>= 1
		length += 1
	return length

def check_base_2(n):
	length = get_base_2_length(n)
	left = length - 1
	right = 0

	while right < left:
		if get_base_2_digit(n, right) != get_base_2_digit(n, left):
			return False
		right += 1
		left -= 1
	return True


total = 0
for i in range(1, 1000000):
	if check_base_10(i) and check_base_2(i):
		total += i
print(total)
