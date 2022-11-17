def fatorial():
	while True:
		n = input("Number:\n")
		try:
			n = int(n)
			break
		except:
			print("You didn't enter a number!")

	n_aux = n
	result = 1
	while (n_aux >= 1):
		result * n_aux
		n_aux = n_aux -1
		print(result)