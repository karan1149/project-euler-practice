import math

def log_pow(n, e):
	if e == 0:
		return 1
	elif e == 1:
		return n
	half = log_pow(n, e / 2)
	if e % 2 == 0:
		return half * half
	else:
		return half * half * n

def is_prime(n):
	# if n in [1, 4, 6, 8, 9]:
	# 	return False
	# elif n in [2, 3, 5, 7]:
	# 	return True
	# return log_pow(3, n - 1) % n == 1 and log_pow(5, n - 1) % n == 1 and log_pow(7, n - 1) % n == 1
	if n == 1:
		return False
	if n == 2:
		return True
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def truncations_right_prime(n):
	n /= 10
	while n:
		if not is_prime(n):
			return False
		n /= 10
	return True

def get_last_digits(n):
	remaining_str = str(n)[1:]
	if remaining_str:
		return int(remaining_str)
	return 0

def truncations_left_prime(n):
	n = get_last_digits(n)
	while n:
		if not is_prime(n):
			return False
		n = get_last_digits(n)
	return True

total = 0
count = 0
i = 11
while True:
	if i % 10000 == 0:
		print(i)
	if is_prime(i) and truncations_right_prime(i) and truncations_left_prime(i):
		print(i)
		total += i
		count += 1
		if count == 11:
			break
	# elif is_prime(i):
	# 	print("rejected", i)
	i += 1

print(total)