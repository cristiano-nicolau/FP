n = int(input("Number? "))
div_sum = 0
for i in range(1, n):
	if n % i == 0:
		print("{} é um divisor de {}".format(i, n))
		div_sum = div_sum + i
if div_sum < n:
	cat = "deficiente"
elif div_sum == n:
	cat = "perfeito"
else:
	cat = "abundante"

print(n, "é um número", cat)
