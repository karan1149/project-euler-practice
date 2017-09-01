coins = [200, 100, 50, 20, 10, 5, 2, 1]

# number of ways to count coins to make a certain quantity

def recursive_count(coins):
	cache = {}
	return recursive_count_helper(coins, 0, cache)

def recursive_count_helper(coins_left, index, cache):
	print coins_left, index, cache
	if coins_left == 0:
		return 1
	elif index == len(coins):
		return 0
	total = 0
	for i in range(coins_left / coins[index] + 1):
		args = (coins_left - i * coins[index], index + 1)
		if args not in cache:
			new_args = list(args) + [cache]
			result = recursive_count_helper(*new_args)
			cache[args] = result
		else:
			result = cache[args]
		total += result
		 
	return total

# print recursive_count(200)

def iterative_count(coins_left):
	table = [[None for _2 in range(len(coins) + 1)] for _ in range(coins_left + 1)]
	for i in range(coins_left + 1):
		table[i][len(coins)] = 0
	for i in range(len(coins) + 1):
		table[0][i] = 1
	print(table)

	for i in range()

iterative_count(200)

