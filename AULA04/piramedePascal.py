def piramede():
	while True:
		num = input("NUMBER:\n")
		try:
			var = num.find(".")
			var1 = num.find(",")
			if (var != -1):
				print('ENTER AN INTEGER')
				return piramede()
			if (var1 != -1):
				print('ENTER AN INTEGER')
				return piramede()
			num = int(num)
			if num < 0:
				print('ENTER A POSITIVE')
				return piramede()
			break
		except:
			print("ERROR")

	for i in range(1, num + 1):
		for j in range(0, num - i + 1):
			print(' ', end='')

		count = 1
		for j in range(1, i + 1):
			print(' ', count, sep='', end='')
			count = count * (i - j) // j
		print()
	print('\n')
	return piramede()

if __name__ == '__main__':
	piramede()