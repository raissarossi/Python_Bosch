def numBinario():
    binX = list(input("BINARY NUMBER:\n"))
    value = 0

    for i in range(len(binX)):
        num = binX.pop()
        if num != '0':
            if num != '1':
                print("ERRO")
                break

        if num == '1':
            value = value + pow(2, i)
    print("The decimal value of the number is:", value)

if __name__ == '__main__':
    numBinario()


#OR ---------------------------------------------------------

def binary_to_decimal(number: int) -> int:
	number = (str(number))[::-1]
	length = len(number)
	total = 0
	for i in range(0, length):
		total += int(number[i]) * 2 ** i
	return total


def decimal_to_binary(number: int) -> int:
	rest_div_list = []
	while number != 0:
		rest_division = number % 2
		number = number // 2
		rest_div_list.append(rest_division)
	binary_revers = reversed(rest_div_list)
	binary_str = [str(i) for i in binary_revers]
	total = int(''.join(binary_str))
	return total


while True:
	menu = input("""Conversion:
- binary to decimal [1]
- decimal to binary [2]
- close [3]

YOUR CHOICE:
""")
	if menu == '3':
		quit()
	elif menu not in ['1', '2']:
		print('Select one of the options [1] [2] [3]')
		print('\n-------------------------------------\n')

	if menu == '1':
		binary = int(input('Binary number: '))
		decimal = binary_to_decimal(binary)
		print(f'{binary} binary = {decimal} decimal')

	if menu == '2':
		decimal = int(input('Decimal number (positive): '))
		binary = decimal_to_binary(decimal)
		print(f'{decimal} decimal = {binary} binary')
