def isPrime(n):
	if n == 0 or n == 1:
		return False
	if n == 2 or n == 3 or n == 5 or n == 7 or n == 9:
		return True
	for i in [2, 3, 5, 7, 9]:
		if n % i == 0:
			return False
	return True
	
def main():
	for r in range(1, 101):
		print("{} is prime: {}".format(r, isPrime(r)))

main()
