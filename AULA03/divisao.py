def divisao():
	a = int(input("ENTER DIVISOR VALUE:\n"))
	b = int(input("ENTER DIVIDEND VALUE:\n"))
	result = a/b
	print("THE RESULT IS: ", result)
	print("THE TYPE IS: ", type(result))

	result_i = a // b
	print("THE RESULT IS: ", result_i)
	print("THE TYPE IS: ", type(result_i))

if __name__ == '__main__':
    divisao()