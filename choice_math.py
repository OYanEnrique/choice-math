#Math program

n1 = int(input('Enter a number:\n'))
n2 = int(input('Enter a number:\n'))

option = 0
result = 0

while option != 5:
	print('''    
[ 1 ] sum
[ 2 ] multiplication
[ 3 ] greater than
[ 4 ] new numbers
[ 5 ] exit''')
	option=int(input('Choose an option:\n'))
	
	if option == 1:
		result = n1 + n2
		print("the sum between", n1 ,"+", n2, "is", result)
		
	elif option == 2:
		result = n1 * n2
		print("The result between", n1, "x", n2, "is", result)
	
	elif option == 3:
		if n1 > n2:
			print(n1, "is greater than", n2)
		elif n2 > n1:
			print(n2, "is greater than", n1)
		else:
			print(n1, "is equal to", n2)
			
	elif option == 4:
		print("Choose the numbers again:\n")
		
		n1 = int(input('Enter a number:\n'))
		n2 = int(input('Enter a number:\n'))
		
	elif option == 5:
		print("Program closed successfully")
	
	else:
		print("Invalid option!")
