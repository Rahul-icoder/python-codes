import math
num = int(input("Enter the number for finding it is prime or not "))
if num>1:
	for i in range(2,num):
		if num%i==0:
			print(num," not prime number")
			break
	else:
		print(num,"is a prime number")
else:
	print('It is neither prime nor composite')
