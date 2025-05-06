#Write a Python program that prints prime numbers less than n which represents the upper limit.
def is_prime(n):
	if n<2:
		return False
	for i in range(2, int(n**0.5)+1):
		if n % i ==0:
			return False
	return True 
num = int (input("Enter upper limit: "))
for j in range (2, num +1):
	loc= is_prime(j)
	if loc == True:
		print(j) 
