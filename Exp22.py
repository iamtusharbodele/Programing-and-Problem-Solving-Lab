#Take an integer n from the user. Your task is to Write a program to find out the sum of the digits of the given number using the process of recursion. Print the result as shown in the Test cases. 
'''
Complete the given function using recursive approach,
and also write the driver code test the functionality,
and pass all the visible and hidden test cases.

'''
def Sumof(n):
	sum = 0
	while n!= 0:
		r = int(n%10)
		sum = sum +r
		n = int(n/10)
	return sum
a = int(input())
b = Sumof(a)
print(f"{b}\n")# take user input and add the function call
