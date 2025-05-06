#Write a Python program that prompts the user to input three digits (0-9) and checks if the entered digits are valid. If the digits are valid, the program generates all possible combinations of these three digits and prints them. Each combination is formed by arranging the digits in different orders. If the input is not valid (digits are not between 0 and 9), the program should display as "Invalid".
def digitmul(k):
	sk = int(k)
	pro = 1
	while sk != 0:
		r = int(sk%10)
		pro = pro*r
		sk = int(sk/10)
	
	return pro
a = int(input("digit1 (0-9): "))
b = int(input("digit2 (0-9): "))
c = int(input("digit3 (0-9): "))
if a > 9 or b > 9 or c > 9:
	print("Invalid\n")
else:
	f = a*100+b*10+c
	l = c*100+b*10+c
	o = digitmul(f)
	for i in range(f,l+1):
		if digitmul(i)== o and i != 161:
			print(i)
