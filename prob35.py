import time
import prob35


def get_eras_sieve(n):
	sieve = [False] * (n + 1)
	for i in range(2, n + 1):
		if not sieve[i]:
			j = 2
			while j * i <= n:
				sieve[i * j] = True
				j += 1
	return sieve

def get_euler_sieve(n):
	pass

def check_circularity(n, sieve):
	string = str(n)
	for i in range(len(string)):
		check_number = int(string[i:] + string[:i])
		if sieve[check_number]:
			return False
	return True


def run_python():
	a = time.time()
	sieve = get_eras_sieve(1000000)


	total = 0
	for i in range(2, 1000000):
		if check_circularity(i, sieve):
			total += 1
	print(total, time.time() - a)

def run_cython():
	a = time.time()
	sieve = prob35.get_eras_sieve(1000000)

	b = time.time()
	print(b - a)
	total = 0
	for i in range(2, 1000000):
		if prob35.check_circularity(i, sieve):
			total += 1
	print(total, time.time() - a)

run_python()
run_cython()

