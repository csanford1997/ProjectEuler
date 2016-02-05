#For Fibonacci numbers below 4million, find the sum of all even numbers. 
#1,2,3,5,8,... 

# Get all fibonacci numbers up to 4 million, and store them in a list. 
# Sum only the even numbers. 

a = 1
b = 2
ab = 0
fibs = [1,2]
while ab <= 4000000: 
	ab = a + b
	a = b
	b = ab
	if ab < 4000000: 
		fibs.append(ab)

print(fibs)