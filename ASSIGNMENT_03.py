numbers = (input("Enter number series separated by spaces:"))
num = numbers.split( )

even_count, odd_count = 0, 0
for numbers in num:
	num = int(numbers)
	if num % 2 == 0:
		even_count += 1
	else:
		odd_count  += 1

print("Number of even numbers :  ", even_count)
print("Number of odd numbers :  ", odd_count)