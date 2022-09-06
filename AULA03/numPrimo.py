def numPrimos():
	x = int(input("ENTER DIVISOR VALUE:\n"))
	mult = 0

	for count in range(2, x):
		if (x % count == 0):
			print(f"DIVISIBLE BY {count}")
			mult += 1

	if (mult == 0):
		print("PRIME NUMBER")





if __name__ == '__main__':
	numPrimos()