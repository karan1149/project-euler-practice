def get_eras_sieve(int n):
	cdef int sieve[1000001]
	for i in range(2, n + 1):
		if not sieve[i]:
			j = 2
			while j * i <= n:
				sieve[i * j] = True
				j += 1
	return sieve

def get_euler_sieve(n):
	pass

def check_circularity(int n, sieve):
	cdef str string = str(n)
	for i in range(len(string)):
		check_number = int(string[i:] + string[:i])
		if sieve[check_number]:
			return False
	return True