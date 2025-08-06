#Multiple of Three
first_number=int(input('Enter the initial number to be checked if its even:\n'))
second_number=int(input('Enter the final number to be checked if it is even:\n'))

for number in range (first_number, second_number + 1):
	if number % 3 ==0:
		print(f'The number {number} is a multiple of three')