#Write a program to print the sum of digits of a number.
sum = 0
n = int(input("num: "))
while n!= 0:
	r = int(n%10)
	sum = sum + r
	n = int(n/10)
print(f"sum: {sum}\n")
