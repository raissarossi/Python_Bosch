

num = int(input('DECIMAL NUMBER:\n'))
print('''CHOOSE ONE:
[1] BINARY
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('YOUR CHOICE:\n'))
if opcao == 1:
	print('{} in binary is {}'.format(num,bin(num)[2:]))
elif opcao == 2:
	print('{} in octal is {}'.format(num, oct(num)[2:]))
elif opcao == 3:
	print('{} in octal is {}'.format(num, hex(num)[2:]))
else:
	print('TRY AGAIN W/ A VALID OPTION')